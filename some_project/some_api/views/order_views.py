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
from ..services.order_services import create_order, update_order
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

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = Order(
            order_person=serializer.validated_data["order_person"],
            order_day=serializer.validated_data["order_day"],
            description=serializer.validated_data["description"],
            is_express=serializer.validated_data["is_express"],
            status=serializer.validated_data["status"],
            cre_user_id=serializer.validated_data["cre_user_id"],
            upd_user_id=serializer.validated_data["upd_user_id"],
        )

        order_details = []
        for s_od in serializer.validated_data["order_details"]:
            od = OrderDetail(
                order=order,
                product=s_od["product"],
                num=s_od["num"],
                cre_user_id=order.cre_user_id,
                upd_user_id=order.upd_user_id,
            )
            order_details.append(od)

        order = create_order(order, order_details)
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
        order.upd_user_id = serializer.validated_data["upd_user_id"]

        order_details = []
        for s_od in serializer.validated_data["order_details"]:
            od = OrderDetail(
                order=order,
                product=s_od["product"],
                num=s_od["num"],
                cre_user_id=order.cre_user_id,
                upd_user_id=order.upd_user_id,
            )
            order_details.append(od)
        order = update_order(order, order_details)

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
