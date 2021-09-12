# coding: utf-8
from rest_framework import viewsets
from ..models import Manufacturer
from ..serializers.manufacturer_serializers import ManufacturerSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """ManufacturerのViewSet
    一番シンプルなViewset(ModelViewsetのデフォルト機能のみ)
    """

    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
