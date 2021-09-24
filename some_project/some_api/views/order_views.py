from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import Order, OrderDetail
from ..serializers.order_serializers import (
    OrderSerializer,
    RetrieveNestedOrderSerializer,
    CreateNestedOrderSerializer,
)
from db.exceptions import TargetRecordDoesNotExist
from utils.helpers import (
    add_fields_to_data,
    add_fields_to_create_data,
    resolve_view_name,
)


class OrderViewSet(viewsets.ModelViewSet):
    """OrderのViewSet
    一番シンプルなViewset(ModelViewsetのデフォルト機能のみ)
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def _create_details(self, order, order_datails):
        """注文配下の注文詳細を全登録する"""

        for s_od in order_datails:
            od = OrderDetail(order=order, product=s_od["product"], num=s_od["num"])
            od.fill_base_fields(order.upd_user_id, order.upd_pgm_id)
            od.save()

    @action(detail=False, methods=["post"])
    def create_nested(self, request):
        """注文と注文詳細を登録"""

        serializer = CreateNestedOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = Order(
            order_person=serializer.validated_data["order_person"],
            order_day=serializer.validated_data["order_day"],
            description=serializer.validated_data["description"],
            is_express=serializer.validated_data["is_express"],
            status=serializer.validated_data["status"],
        )
        order.fill_base_fields(request.user.username, resolve_view_name(request))
        order.save()
        self._create_details(order, serializer.validated_data["order_details"])
        headers = self.get_success_headers(serializer.data)
        added_data = add_fields_to_create_data(order, serializer.data)

        return Response(
            added_data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    @action(detail=True, methods=["get", "put"])
    def nested(self, request, pk):
        """注文と注文詳細を参照/更新"""

        if request.method == "GET":
            order = get_object_or_404(
                Order.objects.prefetch_related("order_details")
                .prefetch_related("order_details__product")
                .prefetch_related("order_details__product__manufacturer"),
                pk=pk,
            )
            # instance = self.get_object()
            serializer = RetrieveNestedOrderSerializer(order)
            return Response(serializer.data)

        if request.method == "PUT":
            order = get_object_or_404(Order, pk=pk)
            serializer = CreateNestedOrderSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            order.order_person = serializer.validated_data["order_person"]
            order.order_day = serializer.validated_data["order_day"]
            order.description = serializer.validated_data["description"]
            order.is_express = serializer.validated_data["is_express"]
            order.status = serializer.validated_data["status"]
            order.upd_dt = serializer.validated_data["upd_dt"]
            try:
                order.fill_base_fields(
                    request.user.username, resolve_view_name(request), update=True
                )
                order.save_exclusive()
            except TargetRecordDoesNotExist:
                return Response(status=status.HTTP_423_LOCKED)

            OrderDetail.objects.filter(order__id=order.id).delete()
            self._create_details(order, serializer.validated_data["order_details"])
            added_data = add_fields_to_data(order, serializer.data)
            headers = self.get_success_headers(serializer.data)
            return Response(added_data, status=status.HTTP_201_CREATED, headers=headers)
