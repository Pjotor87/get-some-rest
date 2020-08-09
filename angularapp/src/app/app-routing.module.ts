import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { MusiciansComponent } from './musicians/musicians.component';

const routes: Routes = [
  { path: 'musicians', component: MusiciansComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
