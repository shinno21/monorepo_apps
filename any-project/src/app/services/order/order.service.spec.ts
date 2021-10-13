import { TestBed } from '@angular/core/testing';

import { OrderService } from './order.service';

describe('OrderService', () => {
  let service: OrderService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(OrderService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('Order一覧が取得できること', () => {
    // S1. 受注一覧のテストコードが失敗すること
    // S2. service.getOrderListの結果がOrderインスタンスの配列となっていること
    // S3. Orderインスタンス配列のうち、先頭1つに然るべき値が設定されていること
    const orderList: Order[] = service.getOrderList();
    const order = orderList.shift();
    expect(order.id).not.toBeNull();
    expect(order.order_day).not.toBeNull();
    expect(order.cre_user_id).not.toBeNull();
    /**
     * "id": 3,
      "order_person": "テストの人3",
      "order_day": null,
      "description": "なるべく普通でお願いします",
      "is_express": false,
      "status": "20",
      "version": 1,
      "cre_user_id": "1",
      "cre_dt": null,
      "upd_user_id": "1",
      "upd_dt": null
      */
  });
});
