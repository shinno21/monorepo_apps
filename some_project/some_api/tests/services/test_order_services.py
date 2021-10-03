import datetime
import pytest
from some_api.services.order_services import create_order
from some_api.models import Order, OrderDetail
from some_api.tests.factories import ProductFactory


@pytest.mark.django_db
class TestCreateOrder:
    """create_order のテスト"""

    @pytest.fixture
    def param_order_parent(self):
        order = Order(
            order_person="Tarou Test",
            order_day=datetime.date(2021, 10, 1),
            description="test",
            is_express=True,
            status="10",
            version=0,
        )
        p1 = ProductFactory()
        p2 = ProductFactory()
        od1 = OrderDetail(order=order, product=p1, num=100)
        od2 = OrderDetail(order=order, product=p2, num=200)
        order_details = [od1, od2]
        return order, order_details

    def test_create_parent(self, param_order_parent):
        order, order_details = param_order_parent
        cre_order = create_order(order, order_details)
        assert cre_order.order_person == "Tarou Test"
