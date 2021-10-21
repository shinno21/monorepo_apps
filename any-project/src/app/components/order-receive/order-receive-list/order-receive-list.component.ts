import { Component, OnInit, AfterViewInit, ViewChild } from '@angular/core';
import { OrderService } from '../../../services/order/order.service';
import { Order } from '../../../interfaces/order';
import { Observable } from 'rxjs';
import { tablePageSizeOptions } from 'src/app/consts';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-order-receive-list',
  templateUrl: './order-receive-list.component.html',
  styleUrls: ['./order-receive-list.component.scss']
})
export class OrderReceiveListComponent implements OnInit, AfterViewInit {
  // orderList?: Order[];
  orderList?: MatTableDataSource<Order>;
  tablePageSizeOptions: number[] = tablePageSizeOptions;
  orderExtractCount = 200;
  orderListColumn: string[] = [
    'checkbox',
    'id',
    'order_day',
    'order_person',
    'status',
    'is_express',
    'description',
    'edit'
  ];
  @ViewChild(MatPaginator) paginator: MatPaginator | undefined | null;
  constructor(private orderService: OrderService) {}

  ngOnInit(): void {}
  ngAfterViewInit() {
    this.orderService
      .getOrderList(this.orderExtractCount)
      .subscribe((orderList) => {
        this.orderList = new MatTableDataSource<Order>(orderList);
        if (this.paginator) {
          this.orderList.paginator = this.paginator;
        }
        console.log(this.orderList);
      });
  }

  onPageIndexChanged() {
    console.log(this.paginator?.pageIndex);
  }
}
