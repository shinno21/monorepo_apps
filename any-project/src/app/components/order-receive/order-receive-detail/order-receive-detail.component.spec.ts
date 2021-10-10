import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OrderReceiveDetailComponent } from './order-receive-detail.component';

describe('OrderReceiveDetailComponent', () => {
  let component: OrderReceiveDetailComponent;
  let fixture: ComponentFixture<OrderReceiveDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OrderReceiveDetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OrderReceiveDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
