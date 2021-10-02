from django.db import models
from django.utils import timezone


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

    cre_user_id = models.CharField("作成者ユーザID", max_length=20, blank=True, null=True)
    cre_dt = models.DateTimeField("作成日時", auto_now_add=True)
    upd_user_id = models.CharField("最終更新者ユーザID", max_length=20)
    upd_dt = UpdateDateTimeField("更新日時", auto_now_add=True)

    @classmethod
    def base_fields_as_dict(cls):
        """管理項目をリストで返す"""
        return [base_field.name for base_field in cls._meta.get_fields()]

    class Meta:
        abstract = True
