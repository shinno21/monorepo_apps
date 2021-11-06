import { Order } from '../entities/order';
import {
  EXPRESS_NAME_FALSE,
  EXPRESS_NAME_TRUE,
  ORDER_STATUS_LIST
} from '../consts';

/***
 * ステータス名からステータスコードを取得します
 * @param status_cd
 * @return {string}
 */
export function getStatusNameFromCd(status_cd: string): string {
  let result = '';
  for (let status of ORDER_STATUS_LIST) {
    if (status.status_cd === status_cd) {
      result = status.status_name;
      break;
    }
  }
  return result;
}

/***
 * ステータスコードから、ステータス名を取得します
 * @param status_name
 * @return {string}
 */
export function getStatusCdFromName(status_name: string): string {
  let result = '';
  for (let status of ORDER_STATUS_LIST) {
    if (status.status_name === status_name) {
      result = status.status_name;
      break;
    }
  }
  return result;
}

/***
 * お急ぎ便区分の画面表示名を取得します
 * @param is_express
 * @return {string}
 */
export function getExpressName(is_express: boolean): string {
  return is_express ? EXPRESS_NAME_TRUE : EXPRESS_NAME_FALSE;
}

/***
 * 画面表示用にOrderデータの整形・変換を行います
 * @param order
 * @return {Order}
 */
export function orderParser(order: Order): Order {
  return {
    ...order,
    order_day: new Date(order.order_day).toLocaleDateString(),
    status_name: getStatusNameFromCd(order.status),
    is_express_name: getExpressName(order.is_express)
  };
}
