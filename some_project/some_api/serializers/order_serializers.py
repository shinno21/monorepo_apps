# coding: utf-8
from rest_framework import serializers
from ..models import Order
from db.models import BaseModel


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
