import { MenuItem } from './entities/menu-item';

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

export const tablePageSizeOptions: number[] = [5, 10, 25, 100, 200, 500, 1000];

export const PAGE_TYPE_NEW = 'new';
export const PAGE_TYPE_UPDATE = 'update';

export const ORDER_STATUS_LIST = [
  { status_cd: '10', status_name: '受注済' },
  { status_cd: '20', status_name: '発送準備中' },
  { status_cd: '30', status_name: '発送中' },
  { status_cd: '90', status_name: '発送済' }
];

export const EXPRESS_NAME_TRUE = "はい";
export const EXPRESS_NAME_FALSE = "いいえ";
