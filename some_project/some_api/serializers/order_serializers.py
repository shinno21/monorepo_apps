from rest_framework import serializers

from db.models import BaseModel

from ..models import Order, OrderDetail
from .product_serializers import RetrieveProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    """OrderのSerializer"""

    version = serializers.IntegerField(required=False)

    class Meta:
        model = Order
        fields = [
            "id",
            "order_person",
            "order_day",
            "description",
            "is_express",
            "status",
            "version",
        ] + BaseModel.base_fields_as_dict()


class RetrieveOrderDetailSerializer(serializers.ModelSerializer):
    """OrderDetailのSerializer(データ取得用)"""

    product = RetrieveProductSerializer(read_only=True)

    class Meta:
        model = OrderDetail
        fields = [
            "id",
            "order",
            "product",
            "num",
        ] + BaseModel.base_fields_as_dict()


class CreateOrderDetailSerializer(serializers.ModelSerializer):
    """OrderDetailのSerializer(データ登録用)"""

    class Meta:
        model = OrderDetail
        fields = [
            "id",
            "product",
            "num",
        ]


class RetrieveNestedOrderSerializer(serializers.ModelSerializer):
    """Order, OrderDetail 親子関係のSerializer(データ取得用)"""

    order_details = RetrieveOrderDetailSerializer(many=True)

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
            "version",
        ] + BaseModel.base_fields_as_dict()


class CreateNestedOrderSerializer(serializers.ModelSerializer):
    """Order, OrderDetail 親子関係のSerializer(データ登録用)"""

    order_details = CreateOrderDetailSerializer(many=True)
    version = serializers.IntegerField(required=False)

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
            "version",
        ] + BaseModel.base_fields_as_dict()
