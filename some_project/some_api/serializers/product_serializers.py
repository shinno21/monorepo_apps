# coding: utf-8
from rest_framework import serializers
from ..models import Product
from db.models import BaseModel
from messages.error import NUM_RANGE_ERROR


class ProductSerializer(serializers.ModelSerializer):
    """ProductのSerializer"""

    manufacturer_name = serializers.CharField(
        source="manufacturer.name", read_only=True
    )

    class Meta:
        model = Product
        fields = [
            "cd",
            "name",
            "price",
            "manufacturer",
            "manufacturer_name",
        ] + [base_field.name for base_field in BaseModel._meta.get_fields()]

    def validate_price(self, value):
        MIN = 0
        MAX = 100000
        if value < MIN or value > MAX:
            raise serializers.ValidationError(
                NUM_RANGE_ERROR.format(attr="値段", min=0, max=100000)
            )
        return value
