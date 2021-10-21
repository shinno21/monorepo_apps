from concurrency.fields import AutoIncVersionField
from django.db import models

from db.models import BaseModel


class Manufacturer(BaseModel):
    """製造元"""

    cd = models.CharField("コード", primary_key=True, max_length=10)
    name = models.CharField(
        "名称",
        unique=True,
        max_length=40,
    )
    is_foreign = models.BooleanField("国外企業フラグ", default=False)

    class Meta:
        verbose_name = verbose_name_plural = "製造元"

    def __str__(self):
        return self.name


class Product(BaseModel):
    """製品"""

    cd = models.CharField("コード", primary_key=True, max_length=20)
    name = models.CharField("名称", unique=True, max_length=40)
    price = models.IntegerField("価格")
    version = AutoIncVersionField(verbose_name="バージョン")
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name="product_manufacturer",
        verbose_name="製造元",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = verbose_name_plural = "製品"

    def __str__(self):
        return self.name


ORDER_STATUS_CHOICES = (("10", "受注済"), ("20", "発送準備中"), ("30", "発送中"), ("90", "発送済"))


class Order(BaseModel):
    """注文"""

    order_person = models.CharField("発注者氏名", max_length=20)
    order_day = models.DateTimeField("発注日")
    description = models.CharField("備考", max_length=1000, blank=True, null=True)
    is_express = models.BooleanField("お急ぎ便フラグ")
    status = models.CharField("ステータス", choices=ORDER_STATUS_CHOICES, max_length=2)
    version = AutoIncVersionField(verbose_name="バージョン")

    class Meta:
        verbose_name = verbose_name_plural = "注文"

    def __str__(self):
        return self.order_person


class OrderDetail(BaseModel):
    """注文明細"""

    order = models.ForeignKey(
        Order,
        related_name="order_details",
        verbose_name="注文",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        related_name="ordered_product",
        verbose_name="製造元",
        on_delete=models.CASCADE,
    )
    num = models.IntegerField("数量")
