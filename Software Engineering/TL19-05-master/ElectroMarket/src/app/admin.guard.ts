import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree } from '@angular/router';
import { LoginService } from './login.service';
import { Router } from '@angular/router';
import { Observable, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators'

@Injectable({
  providedIn: 'root'
})
export class AdminGuard implements CanActivate {

  constructor(private _login: LoginService, private _router: Router) {}

  canActivate(): Observable<boolean> {
    return this._login.checkToken().pipe(map((res) => {
      if ((res == true && localStorage.getItem('role') === '1')) {
        return true;
      }

      this._router.navigate(['/','home']);
      return false;
    }, catchError((err) => {
      console.log("Err: ", err);
      this._router.navigate(['/','home']);
      return of(false);
    })));
  }
  
}
