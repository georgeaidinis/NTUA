import { Component, OnInit } from '@angular/core';
import { SearchDataService } from '../search-data.service'
import { CompleterService, CompleterData } from 'ng2-completer'
import { Router } from '@angular/router';
 
@Component({
  selector: 'app-application',
  templateUrl: './application.component.html',
  styleUrls: ['./application.component.scss']
})
export class ApplicationComponent implements OnInit {

  username = localStorage.getItem("username")
  role = localStorage.getItem("role")
  displayUserMenu = false;

  dataset = "ActualTotalLoad"
  AreaName = ""
  Resolution = ""
  ProductionType = ""
  DateType = "date"
  Year = ""
  Month = ""
  Day = ""
  ListOfDatasets = ["Actual Total Load", "Aggregated Generation Per Type", "Day Ahead Total Load Forecast", "Actual VS Forecast Total Load"]
  ListOfAreas = {}
  ListOfResCodes = {}
  ListOfTypes = {}
  ListOfYears = []
  ListOfMonths = []
  ListOfDays = []
  MyList = ["jsdfsdf", "slkdfjlksjd"]
  AreaKeyword = ""
  DatasetShown = ""
  DateShown = ""

  Records = {}

  mapper = {
    "Actual Total Load": "ActualTotalLoad", 
    "Aggregated Generation Per Type": "AggregatedGenerationPerType", 
    "Day Ahead Total Load Forecast": "DayAheadTotalLoadForecast", 
    "Actual VS Forecast Total Load":"ActualvsForecast"

  }

  noSort(){}

  CreateYears(){
    for(let i=2000; i<2021; i++){
      this.ListOfYears.push(i.toString())
    }
  }
  CreateMonths(){
    for(let i=1; i<13; i++){
      if (i<10){
        let j = i.toString()
        j = "0"+i
        this.ListOfMonths.push(j)  
      }
      else {
        this.ListOfMonths.push(i.toString())
      }
    }
  }
  CreateDays(){
    let endDay = 0
    endDay = this.computeDays()
    for(let i=1; i<endDay+1; i++){
      if (i<10){
        let j = i.toString()
        j = "0"+i
        this.ListOfDays.push(j)  
      }
      else {
        this.ListOfDays.push(i.toString())
      }
    }
  }


  computeDays(){
    if (this.Month == "","1","3","5","7","8","10","12"){
      return 31
    }
    else if (this.Month == "2"){
      return 28
    }
    else{
      return 30
    }
  }

  getAreas(){
    console.log("dataset = " + this.dataset);
    
    let AreaNamesObservable = this._service.getAreas({"dataset":this.dataset})
    AreaNamesObservable.subscribe(AreasResults => {
      this.ListOfAreas = AreasResults
    })
  }

  checkDates(){
    if ((this.DateType == 'date' && this.Day =="" && this.Month == "" && this.Year=="") || (this.DateType == 'month' && this.Month == "" && this.Year=="") || (this.DateType == 'month'&& this.Year=="")){
      return false
   }
  }

  canPerformSearch(){

    if (this.DateType ==""){
      return false
    }
    else{
      if (!this.checkDates){
        return false
      }
    }
    
    if (this.dataset == ""){
      console.log("empty dataset");
      
      return false
    }
    else{
      if (this.AreaName != "" && this.Resolution !=""){
        if (this.dataset !="AggregatedGenerationPerType"){
          console.log("complete not type");
          
          return true
        }
        else{
          if (this.ProductionType !=""){
             console.log("complete type");
              
            return true
          }
          else {
            console.log("missing type");
            
            return false
          }
        }
      }
    else {
      console.log("something missing");
      
      return false
    }
  }
}

  search(){
    if (this.canPerformSearch()){
      let ResultsObservable = this._service.perfomSearch(this.dataset, this.AreaName, this.Resolution, this.ProductionType, this.DateType, this.Year, this.Month, this.Day)

      ResultsObservable.subscribe(Results => {
        this.Records = Results
        console.log("records = "+ this.Records)
      })
      this.DatasetShown = this.dataset
      this.DateShown = this.DateType
    }  
  }

  logout() {
    localStorage.removeItem("username");
    localStorage.removeItem("role");
    localStorage.removeItem("token");
    localStorage.removeItem("uid");
    // localStorage.removeItem("email");
    this._router.navigate(['/', 'login']);
  }

  onClickOutside() {
    if (this.displayUserMenu) {
      this.displayUserMenu = false;
    }
  }



  constructor(private _service: SearchDataService, private _router: Router) {
    let AreaNamesObservable = this._service.getAreas({"dataset":this.dataset})
    let ResCodesObservable = this._service.getResCodes()
    let TypesObservable = this._service.getTypes()

    AreaNamesObservable.subscribe(AreasResults => {
      ResCodesObservable.subscribe(ResCodesResults => {
        TypesObservable.subscribe(TypesResults => {
        this.ListOfAreas = AreasResults
        this.ListOfResCodes = ResCodesResults
        this.ListOfTypes = TypesResults
        })
      })
    })

    this.CreateYears()
    this.CreateMonths()
    this.CreateDays()
   }

  ngOnInit() {
  }

}
