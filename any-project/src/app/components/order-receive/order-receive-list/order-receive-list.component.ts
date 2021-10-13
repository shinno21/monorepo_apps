import { Component, OnInit } from '@angular/core';
import { OrderService } from '../../../services/order/order.service';
import { Order } from '../../../interfaces/order';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-order-receive-list',
  templateUrl: './order-receive-list.component.html',
  styleUrls: ['./order-receive-list.component.scss']
})
export class OrderReceiveListComponent implements OnInit {
  orderList?: Order[];
  orderListColumn: string[] = [
    "checkbox",
    'id',
    'order_day',
    'order_person',
    'status',
    'is_express',
    'description',
    "edit"
  ];
  constructor(private orderService: OrderService) {}

  ngOnInit(): void {
    this.orderService.getOrderList().subscribe((orderList) => {
      this.orderList = orderList;
      console.log(this.orderList);
    });
  }
}
