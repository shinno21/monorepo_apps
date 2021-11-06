import { Injectable } from '@angular/core';
import {
  HttpClient,
  HttpErrorResponse,
  HttpResponse
} from '@angular/common/http';
import { Order } from '../../entities/order';
import { Observable, of } from 'rxjs';
import { environment } from '../../../environments/environment';
import { map, tap } from 'rxjs/operators';
import { orderParser } from '../../utils/entity_parsers';

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
          return res.results;
        }),
        map((results: any) => {
          let parsedResults = results.map((result: Order) => {
            // ステータスコードや日付を画面表示用に整形・変換する
            return orderParser(result);
          });
          return parsedResults;
        })
      );
  }
  // Orderデータを取得する
  getOrder(id: number): Observable<Order> {
    return this.http.get<Order>(`${environment.apiEndpoint}/order/${id}/`).pipe(
      map((order: Order) => {
        let results = orderParser(order);
        console.log(results);
        return results;
      })
    );
  }
}
