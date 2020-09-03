import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { JwtHelperService } from '@auth0/angular-jwt';
import { forkJoin,EMPTY,Observable } from 'rxjs';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private _http: HttpClient) { }

  // async loginUser(params){
  //   const helper = new JwtHelperService();
  //   console.log(params);
  //   let token = ""
  //   token = helper.
  //   helper.tokenGetter(params)
  //   console.log(params);

  //   const path = environment.apiEndpoint + '/Login';
  //   console.log(JSON.stringify(params))
  //   // let loginPromise = await this._http.get(path,{params: params}).toPromise();
  //   // let login = Promise.resolve(loginPromise);
  //   return path;
  // }


  async loginUser(params){
    const helper = new JwtHelperService();
    
    // let jwt_par = helper.(params)
    // console.log(jwt_par);
    // let token = {}
    // token = {"token": jwt_par}
    const path = environment.apiEndpoint + '/Login';
    let loginPromise = await this._http.post(path,params).toPromise();
    console.log(params);
    let login = Promise.resolve(loginPromise);
    return login;
  }



  setJWT(token){
    localStorage.setItem('token',token);
    this.decodeJWT(token);
  }

  decodeJWT (token) {
    const helper = new JwtHelperService();
    let decodedToken: Object = helper.decodeToken(JSON.stringify(token));
    console.log(decodedToken);
    localStorage.setItem('username', decodedToken['username']);
    localStorage.setItem('role', decodedToken['role']);
    localStorage.setItem('uid', decodedToken['uid']);
    localStorage.setItem('email', decodedToken['email']);
    return decodedToken;
  }

  checkToken(){
    let token = localStorage.getItem('token');
    console.log("From checkToken(): ",token);
    let params = new HttpParams()
    .set('token',token)
    console.log("Params: ", params);
    const path = environment.apiEndpoint + '/check';
    return this._http.get(path,{params:params});
  }
}
