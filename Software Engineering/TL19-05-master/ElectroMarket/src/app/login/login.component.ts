import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { LoginService } from '../login.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  loginForm: FormGroup;
  password :string="";
  username: string="";
  wrongCredentials: boolean = false;
  loading: boolean = false;
  token: string = '';

  constructor(private _fb: FormBuilder, private _login: LoginService, private _router: Router) { 
    this.loginForm = _fb.group({
      username: [null, Validators.required],
      password: [null, Validators.required]
    });
  }

  allowUserIn() {
    this._login.setJWT(this.token);
    this._router.navigate(['/', 'home']);
  }

  // termsDeclined() {
  //   this._router.navigate(['/', 'login']);
  // }

  async callLoginUser(form) {
    this.loading = true;
    let loginResult: any = await this._login.loginUser(form);
    this.loading = false;
    if (loginResult !== false) {
      this.token = loginResult['Token'];
      // const element: HTMLElement = document.getElementById('modalButton') as HTMLElement;
      // element.click();
      console.log(this.token);
      this.allowUserIn()
      
    }
    else {
      this.wrongCredentials = true;
    }
  }



  ngOnInit() {
  }

}
