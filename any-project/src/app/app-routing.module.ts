import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OrderReceiveListComponent } from './components/order-receive/order-receive-list/order-receive-list.component';
import { DummyComponent } from './components/dummy/dummy.component';
import {OrderReceiveDetailComponent} from "./components/order-receive/order-receive-detail/order-receive-detail.component";

export const routes: Routes = [
  { path: '', component: OrderReceiveListComponent },
  { path: "detail/:id", component: OrderReceiveDetailComponent},
  { path: 'dummy', component: DummyComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
