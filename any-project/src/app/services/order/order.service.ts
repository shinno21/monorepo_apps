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
  getOrderList(): Observable<Order[]> {
    return this.http
      .get<Order[]>(`${environment.apiEndpoint}/order/list/`)
      .pipe(
        map((res: any) => {
          return res.results;
        })
      );
  }
}
