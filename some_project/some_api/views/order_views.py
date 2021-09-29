from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    ListAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from ..models import Order, OrderDetail
from ..serializers.order_serializers import (
    OrderSerializer,
    RetrieveNestedOrderSerializer,
    CreateNestedOrderSerializer,
)
from utils.helpers import (
    add_fields_to_data,
    add_fields_to_create_data,
)


class ListOrderView(ListAPIView):
    """1件のOrderをOrderDetailを含めて取得する"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CreateOrderView(CreateAPIView):
    """OrderとOrderDetailを登録する"""

    serializer_class = CreateNestedOrderSerializer

    def _create_details(self, order, order_datails):
        """注文配下の注文詳細を全登録する"""

        for s_od in order_datails:
            od = OrderDetail(order=order, product=s_od["product"], num=s_od["num"])
            od.fill_base_fields(order.upd_user_id)
            od.save()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = Order(
            order_person=serializer.validated_data["order_person"],
            order_day=serializer.validated_data["order_day"],
            description=serializer.validated_data["description"],
            is_express=serializer.validated_data["is_express"],
            status=serializer.validated_data["status"],
        )
        order.fill_base_fields(request.user.username)
        order.save()
        self._create_details(order, serializer.validated_data["order_details"])
        headers = self.get_success_headers(serializer.data)
        added_data = add_fields_to_create_data(order, serializer.data)
        added_data["version"] = order.version
        return Response(
            added_data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class UpdateOrderView(UpdateAPIView):
    """Orderを更新して、OrderDetailを登録する"""

    queryset = Order.objects.all()
    serializer_class = CreateNestedOrderSerializer

    def _create_details(self, order, order_datails):
        """注文配下の注文詳細を全登録する"""
        for s_od in order_datails:
            od = OrderDetail(order=order, product=s_od["product"], num=s_od["num"])
            od.fill_base_fields(order.upd_user_id)
            od.save()

    def put(self, request, *args, **kwargs):
        order = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order.order_person = serializer.validated_data["order_person"]
        order.order_day = serializer.validated_data["order_day"]
        order.description = serializer.validated_data["description"]
        order.is_express = serializer.validated_data["is_express"]
        order.status = serializer.validated_data["status"]
        order.version = serializer.validated_data["version"]
        order.fill_base_fields(request.user.username, update=True)
        order.save()
        OrderDetail.objects.filter(order__id=order.id).delete()
        self._create_details(order, serializer.validated_data["order_details"])
        added_data = add_fields_to_data(order, serializer.data)
        added_data["version"] = order.version
        return Response(added_data, status=status.HTTP_200_OK)


class RetrieveOrderView(RetrieveAPIView):
    """1件のOrderをOrderDetailを含めて取得する"""

    queryset = (
        Order.objects.prefetch_related("order_details")
        .prefetch_related("order_details__product")
        .prefetch_related("order_details__product__manufacturer")
    )
    serializer_class = RetrieveNestedOrderSerializer


class DestroyOrderView(DestroyAPIView):
    """1件のOrderを削除する"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
