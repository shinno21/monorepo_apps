from some_api.models import Order, OrderDetail

order_list = []
order_detail_list = []
for i in range(100):
    order = Order(
        order_person=f"テストの人{i+1}",
        description="なるべく早めにお願いします",
        is_express=True,
        status="10",
        version=1,
        cre_user_id=1,
        upd_user_id=1
    )
    for j in range(3):
        order_detail = OrderDetail(
            num=1,
            product_id="RPG-JS-MZ001",
            cre_user_id=1,
            upd_user_id=1,
            order=order
        )
        order_detail_list.append(order_detail)
    order_list.append(order)

Order.objects.bulk_create(order_list)
OrderDetail.objects.bulk_create(order_detail_list)
