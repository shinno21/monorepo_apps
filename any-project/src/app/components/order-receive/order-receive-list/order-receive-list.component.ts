import { SelectionModel } from '@angular/cdk/collections';
import {
  Component,
  OnInit,
  OnDestroy,
  AfterViewInit,
  ViewChild
} from '@angular/core';
import { OrderService } from '../../../services/order/order.service';
import { Order } from '../../../entities/order';
import { Observable, Subscription } from 'rxjs';
import { tablePageSizeOptions } from 'src/app/consts';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';
import { MatSort, Sort } from '@angular/material/sort';
import { LiveAnnouncer } from '@angular/cdk/a11y';

@Component({
  selector: 'app-order-receive-list',
  templateUrl: './order-receive-list.component.html',
  styleUrls: ['./order-receive-list.component.scss']
})
export class OrderReceiveListComponent
  implements OnInit, OnDestroy, AfterViewInit
{
  // orderList?: Order[];
  orderList!: MatTableDataSource<Order>;
  orderSubscription?: Subscription;
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
  selection = new SelectionModel<Order>(true, []);
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;
  constructor(
    private orderService: OrderService,
    private router: Router,
    private _liveAnnouncer: LiveAnnouncer
  ) {}

  ngOnInit(): void {
    this.orderSubscription = this.orderService
      .getOrderList(this.orderExtractCount)
      .subscribe((orderList) => {
        this.orderList = new MatTableDataSource<Order>(orderList);

        this.orderList.paginator = this.paginator;
        this.orderList.sort = this.sort;
        // this.orderList.sortingDataAccessor = (item: Order, header: string) => {
        //   switch (header) {
        //     case 'id':
        //       return item.id;
        //     default:
        //       return 0;
        //   }
        // };
      });
  }
  ngAfterViewInit() {}

  ngOnDestroy() {
    if (this.orderSubscription) {
      this.orderSubscription.unsubscribe();
    }
  }

  onPageIndexChanged() {
    console.log(this.paginator);
  }

  isAllSelected() {
    const numSelected = this.selection.selected.length;
    // const pageSize = this.paginator.pageSize;
    const numRows = this.orderList.data.length;
    return numSelected === numRows;
  }

  toggleTopCheckBox() {
    console.log(this.paginator.pageSize);
    this.isAllSelected()
      ? this.selection.clear()
      : this.orderList?.data.forEach((row) => this.selection.select(row));
  }

  announceSortChange(sortState: Sort) {
    if (sortState.direction) {
      this._liveAnnouncer.announce(`Sorted ${sortState.direction}ending`);
    } else {
      this._liveAnnouncer.announce(`Sorting cleared`);
    }
  }

  onEditOrderReceiveButtonClicked(event: any, order: Order) {
    const currentOrder = order;
    // 明細画面で利用する
    this.router.navigate(["detail", order.id]);
  }
}
