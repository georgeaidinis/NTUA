import { Component, OnInit } from '@angular/core';
import { AdminService } from '../admin.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.scss']
})
export class AdminComponent implements OnInit {

  public activeCard: string = 'Εισαγωγή νέου χρήστη'
  public AdminActions:object = 
  {
    "Εισαγωγή νέου χρήστη":{
      "expanded" : true
    },
    "Προβολή στοιχείων υπάρχοντος χρήστη":{
      "expanded" : false
    },
    "Εισαγωγή αρχείου csv":{
      "expanded" : false
    },
    "Επιστροφή στην Αρχική Σελίδα":{
      "expanded": false
    }
  }

  UserInfo = {
    "username":'',
    "password": '',
    "role":'',
    "quota":'',
    "email":'',
    "uid": localStorage.getItem('uid')
  }

  UserShown = {}

  Usernames = {}
  selectedUser = ''
  disabledButton = true

  saved = false
  editing = false

  disableSaveButton(){
    console.log(this.UserInfo['username'] , this.UserInfo['password'] , this.UserInfo['role'] , this.UserInfo['daily_quotas'] , this.UserInfo['email'])
    // if (this.UserInfo['type']==='' || this.UserInfo['university'] ==='' || this.UserInfo['department'] ==='' || typeof this.UserInfo['grade'] === 'string'){
    if (this.UserInfo['username']==='' || this.UserInfo['password'] ==='' || this.UserInfo['role'] ==='' || this.UserInfo['daily_quotas'] ==='' || this.UserInfo['email'] ===''){
      this.disabledButton = true
    }
    else{
      this.disabledButton = false
    }
  }

  noSort(){}

  setCurrentCard(card){
    // this.saved = false
    switch (card){
      case  Object.keys(this.AdminActions)[0]:{
        this.activeCard = Object.keys(this.AdminActions)[0];
        this.AdminActions[card]['expanded'] = !this.AdminActions[card]['expanded']
        break;
      }
      case  Object.keys(this.AdminActions)[1]:{
        this.activeCard = Object.keys(this.AdminActions)[1];
        this.getUsernames()
        this.AdminActions[card]['expanded'] = !this.AdminActions[card]['expanded']
        break;
      }
      case  Object.keys(this.AdminActions)[2]:{
        this.activeCard = Object.keys(this.AdminActions)[2];
        this.AdminActions[card]['expanded'] = !this.AdminActions[card]['expanded']
        break;
      }
      case  Object.keys(this.AdminActions)[3]:{
        this._router.navigate(['/','home']);
        break;
      }
     default: {
        this.activeCard = Object.keys(this.AdminActions)[0];
        this.AdminActions[card]['expanded'] = !this.AdminActions[card]['expanded']
        break;
      }
    }
    console.log("Selected: "+ this.activeCard);
  }

  showingUser(){
    if (Object.keys(this.UserShown).length == 0){
      return false
    }
    else {
      return true
    }
  }

  getUsernames(){
    let UsersObservables = this._service.getUsers()

    UsersObservables.subscribe(results => {
      this.Usernames = results
    })
  }

  getUserInfo(){
    let UserInfoObservables = this._service.getUserInfo(this.selectedUser, {"role": localStorage.getItem("role")})

    UserInfoObservables.subscribe(results => {
      this.UserShown = results
    })
  }

  saveNewUser(){
    console.log(JSON.stringify({"new_user":this.UserInfo, "role": localStorage.getItem("role")}));
    let POST = this._service.addUser({"new_user":this.UserInfo, "role": localStorage.getItem("role")})
    POST.subscribe(posted => {
      let result = posted
    })
    this.saved = true
  }

  saveChanges(){
    // this.UserInfo["quοta"] = this.UserInfo[""]
    console.log(JSON.stringify(this.UserInfo));
    
    let POST = this._service.saveUserChanges(this.selectedUser,{"edited_user":this.UserInfo, "role": localStorage.getItem("role")})
    POST.subscribe(posted => {
      let result = posted
      // this.selectedUser = this.UserInfo['username']
      this.getUserInfo()
    })
    this.saved = true
  }


  constructor(private _service: AdminService, private _router: Router) { }

  ngOnInit() {
  }

}
