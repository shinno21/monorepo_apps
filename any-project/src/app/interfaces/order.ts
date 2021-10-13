/***
 * Order(注文)
 */
// インスタンスにふるまいをもたせる必要がない場合、interfaceを利用しよう
export interface Order {
  id: number;
  order_person: string;
  order_day: Date;
  description: string;
  is_express: boolean;
  status: string;
  version: number;
  cre_user_id: number;
  cre_dt: Date;
  upd_user_id: number;
  upd_dt: Date;
}
