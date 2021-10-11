import { Component, OnInit, Input } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MENU_ITEM_LIST } from '../../consts';
import { MenuItem } from '../../interfaces/menu-item';
import { Router } from '@angular/router';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss']
})
export class MenuComponent implements OnInit {
  currentPageUrl: string;
  menuItemList: MenuItem[];

  formGroupOptions: FormGroup;

  constructor(private formBuilder: FormBuilder, private router: Router) {
    this.menuItemList = MENU_ITEM_LIST;
    this.currentPageUrl = router.url;
    console.log(this.currentPageUrl);
    this.formGroupOptions = formBuilder.group({
      bottom: 0,
      fixed: false,
      top: 0
    });
  }

  ngOnInit(): void {}
}
