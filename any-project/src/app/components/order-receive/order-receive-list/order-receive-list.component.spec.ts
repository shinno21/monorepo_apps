import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OrderReceiveListComponent } from './order-receive-list.component';

describe('OrderReceiveListComponent', () => {
  let component: OrderReceiveListComponent;
  let fixture: ComponentFixture<OrderReceiveListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OrderReceiveListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OrderReceiveListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
