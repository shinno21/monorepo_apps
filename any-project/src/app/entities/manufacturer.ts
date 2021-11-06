import {SystemColumnItem} from '../interfaces/system-column-item';

export interface Manufacturer extends SystemColumnItem {
  cd: string;
  name: string;
  is_foreign: boolean;
}
