from rest_framework import serializers
from ..models import Product
from db.models import BaseModel
from messages.error import NUM_RANGE_ERROR
from .manufacturer_serializers import ManufacturerSerializer


class ProductSerializer(serializers.ModelSerializer):
    """ProductのSerializer"""

    version = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        fields = [
            "cd",
            "name",
            "price",
            "manufacturer",
            "version",
        ] + BaseModel.base_fields_as_dict()

    def validate_price(self, value):
        MIN = 0
        MAX = 100000
        if value < MIN or value > MAX:
            raise serializers.ValidationError(
                NUM_RANGE_ERROR.format(attr="値段", min=0, max=100000)
            )
        return value


class RetrieveProductSerializer(serializers.ModelSerializer):
    """ProductのSerializer"""

    manufacturer = ManufacturerSerializer(read_only=True)
    version = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        fields = [
            "cd",
            "name",
            "price",
            "manufacturer",
            "version",
        ] + BaseModel.base_fields_as_dict()
