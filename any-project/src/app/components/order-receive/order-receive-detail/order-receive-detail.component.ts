import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { GenericDetailComponent } from '../../../classes/generic-detail-component';
import { OrderService } from '../../../services/order/order.service';
import { Observable, Subscription } from 'rxjs';
import { Order } from '../../../entities/order';
import { ORDER_STATUS_LIST } from "../../../consts";

@Component({
  selector: 'app-order-receive-detail',
  templateUrl: './order-receive-detail.component.html',
  styleUrls: ['./order-receive-detail.component.scss']
})
export class OrderReceiveDetailComponent
  extends GenericDetailComponent
  implements OnInit
{
  orderDetailSubscription!: Subscription;
  orderData$?: Observable<Order>;
  orderData!: Order;
  orderDay!: Date;
  orderStatusList = ORDER_STATUS_LIST;
  orderStatusSelected!: String;
  // ページ種類。その他
  constructor(
    private route: ActivatedRoute,
    private orderService: OrderService
  ) {
    super(Number(route.snapshot.paramMap.get('id')));
  }

  ngOnInit(): void {
    // orderIdが渡された場合、更新画面として利用。それ以外は新規画面とする

    // new
    console.log(this.pageType, this.id);

    // 更新ページの場合、this.idを元にサービスから明細情報を取得する
    if (!this.isNewPage()) {
      this.orderData$ = this.orderService.getOrder(this.id);
      this.orderData$.subscribe((orderData) => {
        this.orderData = orderData;
        this.orderDay = new Date(orderData.order_day);
        this.orderStatusSelected = orderData.status;
      });
    }

    // update
  }
}
