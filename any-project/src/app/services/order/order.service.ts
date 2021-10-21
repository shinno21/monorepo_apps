import { Injectable } from '@angular/core';
import {
  HttpClient,
  HttpErrorResponse,
  HttpResponse
} from '@angular/common/http';
import { Order } from '../../interfaces/order';
import { Observable, of } from 'rxjs';
import { environment } from '../../../environments/environment';
import { map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class OrderService {
  constructor(private http: HttpClient) {}

  // Orderデータ一覧を取得する
  getOrderList(limit: number = 100, offset: number = 0): Observable<Order[]> {
    return this.http
      .get<Order[]>(
        `${environment.apiEndpoint}/order/list/?limit=${limit}&offset=${offset}`
      )
      .pipe(
        map((res: any) => {
          console.log(res.results);
          return res.results;
        }),
        map((results: any) => {
          results.map((result: Order) => {
            result.order_day = new Date(result.order_day).toLocaleDateString();
          });
          return results;
        })
        // ステータスの変換
        // お急ぎ便の変換
      );
  }
}
