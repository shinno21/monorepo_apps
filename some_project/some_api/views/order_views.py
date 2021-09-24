# coding: utf-8
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from ..models import Order, OrderDetail
from ..serializers.order_serializers import OrderSerializer, NestedOrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """OrderのViewSet
    一番シンプルなViewset(ModelViewsetのデフォルト機能のみ)
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class NestedOrderView(CreateAPIView):
    serializer_class = NestedOrderSerializer

    def post(self, request, *args, **kwargs):
        """登録API"""
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = Order.objects.create(
            order_person=serializer.validated_data["order_person"],
            order_day=serializer.validated_data["order_day"],
            description=serializer.validated_data["description"],
            is_express=serializer.validated_data["is_express"],
            status=serializer.validated_data["status"],
        )
        for od in serializer.validated_data["order_details"]:
            OrderDetail.objects.create(
                order=order, product=od["product"], num=od["num"]
            )

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
