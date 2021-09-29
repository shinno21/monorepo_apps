from django.db import models
from django.utils import timezone


def fill_base_fields(obj, username, update=False):
    """共通管理項目(BaseModel)の値を埋める関数
    :param obj: 共通管理項目のカラムを持つモデルのインスタンス
    :param username: ユーザ名(OA番号)
    :param funcname: 実行関数名(最上位の関数を設定する)
    :param update: 更新の場合はTrueを指定する
    """
    obj.upd_user_id = username
    if not update:
        obj.cre_user_id = obj.upd_user_id


class UpdateDateTimeField(models.DateTimeField):
    """更新日時フィールド
    auto_now=True相当の動作をする
    """

    def __init__(self, *args, **kwargs):
        super(UpdateDateTimeField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        """auto_nowを指定しなくても現在日時にする"""
        value = timezone.now()
        setattr(model_instance, self.attname, value)
        return value


class BaseModel(models.Model):
    """共通管理項目のフィールドを実装するための抽象モデル"""

    cre_user_id = models.CharField("作成者ユーザID", max_length=20, editable=False)
    cre_dt = models.DateTimeField("作成日時", auto_now_add=True)
    upd_user_id = models.CharField("最終更新者ユーザID", max_length=20, editable=False)
    upd_dt = UpdateDateTimeField("更新日時", auto_now_add=True)

    def fill_base_fields(self, username, update=False):
        """リクエストオブジェクトを使って共通管理項目を埋めるショートカットメソッド"""
        fill_base_fields(self, username, update)

    @classmethod
    def base_fields_as_dict(cls):
        """管理項目をリストで返す"""
        return [base_field.name for base_field in cls._meta.get_fields()]

    class Meta:
        abstract = True
