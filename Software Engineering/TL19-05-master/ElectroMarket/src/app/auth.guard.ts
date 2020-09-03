import { Injectable } from '@angular/core';
import { CanActivate } from '@angular/router';
import { LoginService } from './login.service';
import { Router } from '@angular/router';
import { Observable, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators'


@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  validToken:any;

  constructor(private _login: LoginService, private _router: Router) {}

  canActivate(): Observable<boolean> {
    return this._login.checkToken().pipe(map((res) => {
      if (res === true) {
        return true;
      } 

      this._router.navigate(['/','login']);
      return false;
    }, catchError((err) => {
      console.log("Err: ", err);
      this._router.navigate(['/','login']);
      return of(false);
    })));
  }

}
