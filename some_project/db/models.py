# coding: utf-8
from django.db import models
from django.utils import timezone
from django.db.models import signals
from django.db import router

from .exceptions import NoReferenceToUpdatedDateTime
from .exceptions import TargetRecordDoesNotExist

VIEW_CLASS_ATTRIBUTE_NAME = "view_class_name"
UPDATE_DATETIME_FIELD_NAME = "upd_dt"


def save_exclusive(
    obj, using=None, update_datetime_field_name=UPDATE_DATETIME_FIELD_NAME
):
    """更新日時を使った排他操作、更新に成功した場合Trueを返す。モデルはRsiCommonInfoを継承していることを想定"""

    cls = obj.__class__
    meta = cls._meta
    non_pks = [f for f in meta.local_concrete_fields if not f.primary_key]
    pk_val = obj._get_pk_val(meta)
    pk_set = pk_val is not None

    if len(non_pks) == 0:
        # モデルにPK以外の項目が指定されていない場合、PKを含める
        non_pks = [f for f in meta.local_concrete_fields]

    if pk_set:
        # 主キーが指定された場合
        base_qs = cls._base_manager.using(using)
        # 元の更新日時を取得
        if not hasattr(obj, UPDATE_DATETIME_FIELD_NAME):
            raise NoReferenceToUpdatedDateTime
        upd_dt = getattr(obj, UPDATE_DATETIME_FIELD_NAME)
        if upd_dt is None:
            # 更新日時が指定されない場合は新規追加とみなして通常の保存処理
            obj.save()
            return True
        # 更新する値のペア(auto_nowはここで更新される)
        values = [(f, None, f.pre_save(obj, False)) for f in non_pks]
        # 更新日時でフィルタ
        filtered = base_qs.filter(**{UPDATE_DATETIME_FIELD_NAME: upd_dt, "pk": pk_val})

        # QuerySet._update() ではシグナルが送られないので、手動で送信
        signals.pre_save.send(
            sender=obj.__class__,
            instance=obj,
            update_fields=None,
            raw=False,
            using=using or router.db_for_write(obj.__class__, instance=obj),
        )

        updated_cnt = filtered._update(values)
        # 更新が1件の場合は成功
        if updated_cnt == 1:
            signals.post_save.send(
                sender=obj.__class__,
                instance=obj,
                created=False,
                update_fields=None,
                raw=False,
                using=(using or router.db_for_write(obj.__class__, instance=obj)),
            )
            return True
        else:
            raise TargetRecordDoesNotExist

    # 主キーが指定されない場合は新規なので通常の保存と同じ
    obj.save()
    return True


def resolve_view_name(request):
    """リクエストオブジェクトからviewの名前を返す関数
    :param request: リクエスト
    :return: viewの名前
    """

    # ViewSetの場合は属性を参照する
    if hasattr(request, VIEW_CLASS_ATTRIBUTE_NAME):
        return getattr(request, VIEW_CLASS_ATTRIBUTE_NAME)

    func = request.resolver_match.func
    if hasattr(func, "__self__"):
        view_real = func.__self__.__class__
    else:
        view_real = func

    return u"{}.{}".format(view_real.__module__, view_real.__name__)


def fill_common_info(obj, request, update=False):
    """共通管理項目(BaseModel)の値を埋める関数
    :obj: 共通管理項目のカラムを持つモデルのインスタンス
    :request: リクエストオブジェクト
    :update: 更新の場合はTrueを指定する
    """
    if request.user:
        # TODO is_authenticated があると認証が必要になるためコメント（テストの時も困りそう）
        # if request.user and request.user.is_authenticated():
        # 更新ユーザーID
        obj.upd_user_id = request.user.username
        if not update:
            # 作成ユーザーID
            obj.cre_user_id = obj.upd_user_id
    if request.resolver_match:
        # 更新プログラムIDはviewの名前
        obj.upd_pgm_id = resolve_view_name(request)
        if not update:
            # 作成プログラムID
            obj.cre_pgm_id = obj.upd_pgm_id


class UpdateDateTimeField(models.DateTimeField):
    """更新日時フィールド(排他制御用)
    auto_now=True相当の動作をするがeditable=TrueでデフォルトはHiddenInput
    """

    def __init__(self, *args, **kwargs):
        kwargs["editable"] = True
        kwargs["blank"] = True
        super(UpdateDateTimeField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        """auto_nowを指定しなくても現在日時にする"""
        value = timezone.now()
        setattr(model_instance, self.attname, value)
        return value


class BaseModel(models.Model):
    """共通管理項目のフィールドを実装するための抽象モデル"""

    cre_user_id = models.CharField("作成者ユーザID", max_length=20, editable=False)
    cre_pgm_id = models.CharField("作成プログラムID", max_length=100, editable=False)
    cre_dt = models.DateTimeField("作成日時", auto_now_add=True)
    upd_user_id = models.CharField("最終更新者ユーザID", max_length=20, editable=False)
    upd_pgm_id = models.CharField("最終更新プログラムID", max_length=100, editable=False)
    upd_dt = UpdateDateTimeField("更新日時")

    def fill_common_info(self, request, update=False):
        """リクエストオブジェクトを使って共通管理項目を埋めるショートカットメソッド"""
        fill_common_info(self, request, update)

    def save_exclusive(self, request=None, using=None):
        """排他制御付きの保存メソッド
        :request: 共通管理項目に必要なカラムを埋めるために使用、省略した場合は埋めない
        :using: default以外のデータベースに保存する場合には指定する
        """
        # request引数が指定されているなら共通管理項目の設定も呼ぶ
        if request is not None:
            if self.pk is None:
                # 主キーが指定されない場合は新規扱い
                update = False
            else:
                # 主キーが指定される場合は作成日時が空なら新規扱い
                update = self.cre_dt is not None
            self.fill_common_info(request, update=update)
        return save_exclusive(self, using=using)

    @classmethod
    def base_fields_as_dict(cls):
        return [base_field.name for base_field in cls._meta.get_fields()]

    class Meta:
        abstract = True
