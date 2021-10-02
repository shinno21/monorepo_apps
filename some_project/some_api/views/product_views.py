from rest_framework import viewsets
from ..models import Product
from ..serializers.product_serializers import (
    ProductSerializer,
    RetrieveProductSerializer,
)
from rest_framework.generics import ListAPIView, RetrieveAPIView


class ListProductView(ListAPIView):
    """Productのリストを取得する"""

    queryset = Product.objects.select_related("manufacturer")
    serializer_class = RetrieveProductSerializer


class RetrieveProductView(RetrieveAPIView):
    """1件のProductを取得する"""

    queryset = Product.objects.select_related("manufacturer")
    serializer_class = RetrieveProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """ProductのViewSet
    一番シンプルなViewset(ModelViewsetのデフォルト機能のみ)
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
