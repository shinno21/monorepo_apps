import json
import pytest
import datetime
import pytz
from rest_framework.test import APIRequestFactory
from rest_framework import status
from ...views.order_views import CreateOrderView
from ..factories import ProductFactory
from ...models import Order, OrderDetail


@pytest.mark.django_db
class TestCreateOrderView:
    def test_create_order_ok(self):
        ProductFactory(cd="01")
        ProductFactory(cd="02")
        factory = APIRequestFactory()
        view = CreateOrderView.as_view()
        data = {
            "order_person": "Tarou Test",
            "order_day": "2021-09-30T09:00:00+09:00",
            "description": "description1",
            "is_express": False,
            "status": "10",
            "cre_user_id": "7406198",
            "upd_user_id": "8406198",
            "order_details": [
                {"product": "01", "num": 20},
                {"product": "02", "num": 30},
            ],
        }
        payload = json.dumps(data)
        request = factory.post(
            "/some_api/order/create/",
            payload,
            content_type="application/json",
        )
        response = view(request)
        order_queryset = Order.objects.all()

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] == 1
        assert response.data["cre_user_id"] == "7406198"
        assert order_queryset.count() == 1

        order_details_queryset = OrderDetail.objects.filter(order__id=1)
        assert order_details_queryset.count() == 2

        order = order_queryset.get(pk=1)
        assert order.pk == 1
        assert order.order_person == "Tarou Test"
        assert order.order_day == datetime.datetime(
            2021, 9, 30, 0, 0, tzinfo=pytz.timezone("UTC")
        )
