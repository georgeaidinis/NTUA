import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { forkJoin, EMPTY, Observable } from 'rxjs';
import { retry, catchError, shareReplay } from 'rxjs/operators';
import { environment } from '../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class SearchDataService {

  constructor(private _http: HttpClient) { }


  getAreas(parameters){
    const path = environment.apiEndpoint + '/get_areas';
    return this._http.get(path, {params: parameters}).pipe(
      retry(4),
      catchError(() => {
        return EMPTY;
      }),
      shareReplay()
    );
 };


  getResCodes(){
    const path = environment.apiEndpoint + '/get_resCodes';
    return this._http.get(path).pipe(
      retry(4),
      catchError(() => {
        return EMPTY;
      }),
      shareReplay()
    );
  }

  getTypes(){
    const path = environment.apiEndpoint + '/get_types';
    return this._http.get(path).pipe(
      retry(4),
      catchError(() => {
        return EMPTY;
      }),
      shareReplay()
    );
  }

  perfomSearch(dataset, AreaName, Resolution, ProductionType, DateType, Year, Month, Day){
    // let headers = new HttpHeaders().set("token", localStorage.getItem('token'))
    // console.log(headers.get("token"));
    // console.log(JSON.stringify(headers));
    
    // headers.append("token", localStorage.getItem('token'))
    // console.log("headers = "+ JSON.stringify(headers))
    let req_path = "/" + dataset + "/" + AreaName + "/"
    if (dataset == "AggregatedGenerationPerType"){
      req_path = req_path + ProductionType + "/"
    }
    req_path = req_path + Resolution + "/" + DateType + "/" + Year
    if (DateType == "year"){}
    else if (DateType == "month"){
      req_path = req_path + "-" + Month
    }
    else if (DateType == "date"){
      req_path = req_path + "-" + Month + "-" + Day
    }
    let parameters = {"format": "json", "uid": localStorage.getItem('uid')}
    const path = environment.apiEndpoint + req_path
    console.log(path);
    return this._http.get(path, {params: parameters}).pipe(
      retry(4),
      catchError(() => {
        return EMPTY;
      }),
      shareReplay()
    );
  }
}