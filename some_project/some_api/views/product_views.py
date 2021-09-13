# coding: utf-8
from rest_framework import viewsets
from ..models import Product
from ..serializers.product_serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """ProductのViewSet
    一番シンプルなViewset(ModelViewsetのデフォルト機能のみ)
    """

    queryset = Product.objects.select_related()
    serializer_class = ProductSerializer
