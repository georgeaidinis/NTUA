import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { ApplicationComponent } from './application/application.component'
import { AdminComponent } from './admin/admin.component'
import { AdminGuard } from './admin.guard'
import { AuthGuard } from './auth.guard';



const routes: Routes = [
  {path: "login", component: LoginComponent},
  {path: "home", component: ApplicationComponent, canActivate: [AuthGuard]},
  {path: "admin", component: AdminComponent, canActivate: [AdminGuard]},
  // {path: "admin", component: AdminComponent},

  {path: "**", redirectTo: "/home", pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
