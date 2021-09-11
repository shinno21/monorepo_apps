# coding: utf-8
from django.db import models
from db.models import BaseModel


class Manufacturer(BaseModel):
    """製造元"""

    cd = models.CharField("コード", max_length=10)
    name = models.CharField("名称", max_length=40)

    class Meta:
        verbose_name = verbose_name_plural = "製造元"

    def __str__(self):
        return self.name


class Product(BaseModel):
    """製品"""

    cd = models.CharField("コード", max_length=20)
    name = models.CharField("名称", max_length=40)
    price = models.IntegerField("価格")
    made_by = models.ForeignKey(
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

    ordered_by = models.CharField("発注者氏名", max_length=20)
    ordered_at = models.DateTimeField("発注日")
    description = models.CharField("備考", max_length=1000)
    is_express = models.BooleanField("お急ぎ便フラグ")
    status = models.CharField("ステータス", choices=ORDER_STATUS_CHOICES, max_length=2)

    class Meta:
        verbose_name = verbose_name_plural = "注文"

    def __str__(self):
        return self.name


class OrderDetail(BaseModel):
    """注文明細"""

    product = models.ForeignKey(
        Product,
        related_name="orderdetail_product",
        verbose_name="製造元",
        on_delete=models.CASCADE,
    )
    num = models.IntegerField("数量")
