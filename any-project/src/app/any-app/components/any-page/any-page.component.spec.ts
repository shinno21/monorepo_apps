import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AnyPageComponent } from './any-page.component';

describe('AnyPageComponent', () => {
  let component: AnyPageComponent;
  let fixture: ComponentFixture<AnyPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AnyPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AnyPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
