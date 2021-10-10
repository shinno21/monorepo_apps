import { Component, OnInit, Input } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MENU_ITEM_LIST } from '../../consts';
import { MenuItem } from '../../interfaces/menu-item';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss']
})
export class MenuComponent implements OnInit {
  @Input() currentPageId?: string;

  menuItemList: MenuItem[];

  formGroupOptions: FormGroup;

  constructor(private formBuilder: FormBuilder) {
    this.menuItemList = MENU_ITEM_LIST;
    this.formGroupOptions = formBuilder.group({
      bottom: 0,
      fixed: false,
      top: 0
    });
  }

  ngOnInit(): void {}
}
