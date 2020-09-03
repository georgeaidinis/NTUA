import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { JwtHelperService } from '@auth0/angular-jwt';
import { forkJoin,EMPTY,Observable } from 'rxjs';
import { environment } from '../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class AdminService {

  constructor(private _http: HttpClient) { }

  addUser(params?: any ){
    const path = environment.apiEndpoint + '/Admin/users';
    // return this._http.post(path, params, { observe: 'response' })
    return this._http.post(path, params)
  }

  getUsers(){
    const path = environment.apiEndpoint + '/Admin/getUsers';
    return this._http.get(path)
  }

  getUserInfo(username, params){
    const path = environment.apiEndpoint + '/Admin/users/' + username;
    return this._http.get(path, {params:params})
  }

  saveUserChanges(username, params?: any ){
    const path = environment.apiEndpoint + '/Admin/users/' + username;
    // return this._http.post(path, params, { observe: 'response' })
    return this._http.put(path, params)
  }


}
