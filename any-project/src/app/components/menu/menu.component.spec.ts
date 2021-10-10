import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MenuComponent } from './menu.component';

describe('MenuComponent', () => {
  let component: MenuComponent;
  let fixture: ComponentFixture<MenuComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [MenuComponent]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MenuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
  it('表示対象のMenuItemオブジェクトが存在するかどうか', () => {
    const menuItemList = component.menuItemList;
    expect(menuItemList.length).not.toBe(0);
    expect(menuItemList[0].pageId).not.toBeNull();
    expect(menuItemList[0].displayName).not.toBeNull();
    expect(menuItemList[0].pageId).not.toBeNull();
  });
});
