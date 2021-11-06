import { SystemColumnItem } from '../interfaces/system-column-item';
import { Product } from './product';

/***
 * Order(注文)
 */
// インスタンスにふるまいをもたせる必要がない場合、interfaceを利用しよう
export interface Order extends SystemColumnItem {
  id: number;
  order_person: string;
  order_day: string;
  description: string;
  is_express: boolean;
  // お急ぎ便表示名
  is_express_name: string;
  status: string;
  // ステータス表示名
  status_name: string;
  order_details: OrderDetail[];
  version: number;
}

export interface OrderDetail extends SystemColumnItem {
  id: number;
  order: number;
  product: Product[];
  num: number;
}
