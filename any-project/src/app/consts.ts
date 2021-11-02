import { MenuItem } from './interfaces/menu-item';

export const MENU_ITEM_LIST: MenuItem[] = [
  {
    displayName: '受注管理',
    pageUrl: '/',
    routerLink: ''
  },
  {
    displayName: 'XX管理',
    pageUrl: '/dummy',
    routerLink: 'dummy'
  }
];


export const tablePageSizeOptions: number[] = [5, 10, 25, 100, 200, 500, 1000]

export const PAGE_TYPE_NEW = "new";
export const PAGE_TYPE_UPDATE = "update"
