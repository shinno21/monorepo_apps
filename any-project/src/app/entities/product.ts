import { SystemColumnItem } from '../interfaces/system-column-item';
import { Manufacturer } from './manufacturer';

export interface Product extends SystemColumnItem {
  cd: string;
  name: string;
  price: number;
  manufacturer: Manufacturer[];
  version: number;
}
