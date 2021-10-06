from django.conf import settings
from django.contrib.auth import models as auth_models
from django.db import models

from db.models import BaseModel


class Role(BaseModel):
    """ロール"""

    cd = models.CharField("コード", max_length=20)
    name = models.CharField("名称", max_length=40)
    description = models.CharField("説明", max_length=40, blank=True, null=True)

    class Meta:
        verbose_name = verbose_name_plural = "ロール"

    def __str__(self):
        return self.name


class User(BaseModel, auth_models.AbstractUser):
    """ユーザのモデル"""

    roles = models.ManyToManyField(Role, through="UserRole")
    email = models.EmailField("メールアドレス")
    last_name = models.CharField("姓", max_length=9)
    first_name = models.CharField("名", max_length=9)

    class Meta:
        verbose_name = verbose_name_plural = "ユーザ"

    def __str__(self):
        return "{user.last_name} {user.first_name}<{user.username}>".format(user=self)


class UserRole(BaseModel):
    """ユーザロール"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="userrole_user",
        verbose_name="ユーザID",
        on_delete=models.CASCADE,
    )
    role = models.ForeignKey(
        Role,
        related_name="userrole_role",
        verbose_name="ロールコード",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = verbose_name_plural = "ユーザロール"
