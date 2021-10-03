from some_api.models import Order, OrderDetail
from typing import List


def create_order(order: Order, order_details: List[OrderDetail]) -> Order:
    order.save()
    for od in order_details:
        od.save()
    return order


def update_order(order: Order, order_details: List[OrderDetail]) -> Order:
    order.save()
    OrderDetail.objects.filter(order__id=order.id).delete()
    for od in order_details:
        od.save()
    return order
