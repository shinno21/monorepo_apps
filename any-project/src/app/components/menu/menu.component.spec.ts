import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MenuComponent } from './menu.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { routes } from '../../app-routing.module';

describe('MenuComponent', () => {
  let component: MenuComponent;
  let fixture: ComponentFixture<MenuComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [MenuComponent],
      imports: [FormsModule, ReactiveFormsModule, RouterModule.forRoot(routes)],
      providers: []
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
    expect(menuItemList[0].pageUrl).not.toBeNull();
    expect(menuItemList[0].displayName).not.toBeNull();
    expect(menuItemList[0].routerLink).not.toBeNull();
  });
});
