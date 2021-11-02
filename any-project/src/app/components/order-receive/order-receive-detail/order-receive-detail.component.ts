import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { GenericDetailComponent } from '../../../classes/generic-detail-component';

@Component({
  selector: 'app-order-receive-detail',
  templateUrl: './order-receive-detail.component.html',
  styleUrls: ['./order-receive-detail.component.scss']
})
export class OrderReceiveDetailComponent
  extends GenericDetailComponent
  implements OnInit
{
  // ページ種類。その他
  constructor(private route: ActivatedRoute) {
    super(Number(route.snapshot.paramMap.get('id')));
  }

  ngOnInit(): void {
    // orderIdが渡された場合、更新画面として利用。それ以外は新規画面とする

    // new
    console.log(this.pageType, this.id);

    // 更新ページの場合、this.idを元にサービスから明細情報を取得する
    if (!this.isNewPage()) {
    }

    // update
  }
}
