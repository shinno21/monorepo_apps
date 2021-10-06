from factory import Faker, Sequence, SubFactory, fuzzy
from factory.django import DjangoModelFactory

from some_api.models import (
    ORDER_STATUS_CHOICES,
    Manufacturer,
    Order,
    OrderDetail,
    Product,
)


class ManufacturerFactory(DjangoModelFactory):
    class Meta:
        model = Manufacturer

    cd = fuzzy.FuzzyText(length=10, chars="0123456789")
    name = Sequence(lambda n: "manu{0}".format(n))


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    cd = fuzzy.FuzzyText(length=20, chars="0123456789")
    name = Sequence(lambda n: "product{0}".format(n))
    price = 100
    version = 0
    manufacturer = SubFactory(ManufacturerFactory)


class OrderDetailFactory(DjangoModelFactory):
    class Meta:
        model = OrderDetail

    product = SubFactory(ProductFactory)
    num = 100


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    order_person = Faker("name", locale="ja_JP")
    order_day = Faker("date")
    is_express = Faker("boolean")
    status = fuzzy.FuzzyChoice(ORDER_STATUS_CHOICES)
    version = 0
