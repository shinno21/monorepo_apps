import { PAGE_TYPE_NEW, PAGE_TYPE_UPDATE } from '../consts';

export class GenericDetailComponent {
  protected pageType!: string;
  protected id!: number;

  constructor(id: number) {
    this.decidePageType(id);
    this.id = id;
  }

  decidePageType(id: number) {
    if (id) {
      this.pageType = PAGE_TYPE_UPDATE;
    } else {
      this.pageType = PAGE_TYPE_NEW;
    }
  }

  isNewPage() {
    return this.pageType === PAGE_TYPE_NEW;
  }
}
