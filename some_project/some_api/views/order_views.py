# coding: utf-8
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import Order, OrderDetail
from ..serializers.order_serializers import (
    OrderSerializer,
    NestedOrderSerializer,
)


class OrderViewSet(viewsets.ModelViewSet):
    """OrderのViewSet
    一番シンプルなViewset(ModelViewsetのデフォルト機能のみ)
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=["post"])
    def create_nested(self, request):
        """注文と注文詳細を登録"""

        serializer = NestedOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # TODO もっと綺麗に移し替える方法がある気がする.
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

    @action(detail=True, methods=["get", "post"])
    def nested(self, request, pk):
        """注文と注文詳細を参照/更新"""
        # 最下層までN+1を発生させずに取得したい
        order = get_object_or_404(Order.objects.select_related(), pk=pk)

        if request.method == "GET":
            # instance = self.get_object()
            serializer = NestedOrderSerializer(order)
            return Response(serializer.data)

        if request.method == "POST":
            order = get_object_or_404(Order, pk=pk)
            serializer = NestedOrderSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # TODO もっと綺麗に移し替える方法がある気がする.
            order.order_person = serializer.validated_data["order_person"]
            order.order_day = serializer.validated_data["order_day"]
            order.description = serializer.validated_data["description"]
            order.is_express = serializer.validated_data["is_express"]
            order.status = serializer.validated_data["status"]
            for od in serializer.validated_data["order_details"]:
                OrderDetail.objects.create(
                    order=order, product=od["product"], num=od["num"]
                )

            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
