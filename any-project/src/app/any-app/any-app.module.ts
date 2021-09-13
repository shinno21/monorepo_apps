import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AnyPageComponent } from './components/any-page/any-page.component';

@NgModule({
  declarations: [AnyPageComponent],
  exports: [AnyPageComponent],
  imports: [CommonModule]
})
export class AnyAppModule {}
