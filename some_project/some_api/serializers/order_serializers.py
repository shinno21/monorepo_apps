# coding: utf-8
from rest_framework import serializers
from ..models import Order, OrderDetail
from db.models import BaseModel
from .product_serializers import ProductSerializer


class OrderDetailSerializer(serializers.ModelSerializer):
    """OrderDetailのSerializer"""

    # TODO N+1問題がある.
    # product_name = serializers.CharField(source="product.name", read_only=True)
    product = ProductSerializer()

    class Meta:
        model = OrderDetail
        fields = [
            "id",
            "product",
            # "product_name",
            "num",
        ] + [base_field.name for base_field in BaseModel._meta.get_fields()]


class NestedOrderSerializer(serializers.ModelSerializer):
    """Order, OrderDetail のSerializer"""

    order_details = OrderDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "order_person",
            "order_day",
            "description",
            "is_express",
            "status",
            "order_details",
        ] + [base_field.name for base_field in BaseModel._meta.get_fields()]


class OrderSerializer(serializers.ModelSerializer):
    """OrderのSerializer"""

    class Meta:
        model = Order
        fields = [
            "id",
            "order_person",
            "order_day",
            "description",
            "is_express",
            "status",
        ] + [base_field.name for base_field in BaseModel._meta.get_fields()]
