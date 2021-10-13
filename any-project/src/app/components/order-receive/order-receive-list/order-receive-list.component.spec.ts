import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OrderReceiveListComponent } from './order-receive-list.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { OrderService } from '../../../services/order/order.service';

describe('OrderReceiveListComponent', () => {
  let component: OrderReceiveListComponent;
  let fixture: ComponentFixture<OrderReceiveListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HttpClientModule],
      declarations: [OrderReceiveListComponent]
    }).compileComponents();
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
