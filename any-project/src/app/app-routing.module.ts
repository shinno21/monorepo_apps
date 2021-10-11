import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OrderReceiveListComponent } from './components/order-receive/order-receive-list/order-receive-list.component';
import { DummyComponent } from './components/dummy/dummy.component';

export const routes: Routes = [
  { path: '', component: OrderReceiveListComponent },
  { path: 'dummy', component: DummyComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
