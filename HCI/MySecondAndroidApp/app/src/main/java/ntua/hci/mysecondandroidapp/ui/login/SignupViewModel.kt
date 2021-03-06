package ntua.hci.mysecondandroidapp.ui.login

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import android.util.Patterns
import ntua.hci.mysecondandroidapp.data.LoginRepository
import ntua.hci.mysecondandroidapp.data.Result

import ntua.hci.mysecondandroidapp.R

class SignupViewModel(private val loginRepository: LoginRepository) : ViewModel() {

    private val _signupForm = MutableLiveData<SignupFormState>()
    val signupFormState: LiveData<SignupFormState> = _signupForm

    private val _signupResult = MutableLiveData<LoginResult>()
    val signupResult: LiveData<LoginResult> = _signupResult


    fun login(username: String, password: String) {
        // can be launched in a separate asynchronous job
        val result = loginRepository.login(username, password)

        if (result is Result.Success) {
            _signupResult.value = LoginResult(success = LoggedInUserView(displayName = result.data.displayName))
        } else {
            _signupResult.value = LoginResult(error = R.string.login_failed)
        }
    }

    fun signupDataChanged(name: String, username: String, password: String, retype_password: String) {

        if (name.isBlank())  {
            _signupForm.value = SignupFormState(nameError=R.string.empty_name)
        } else if (!isUserNameValid(username)) {
            _signupForm.value = SignupFormState(usernameError = R.string.invalid_username)
        } else if (!isPasswordValid(password)) {
            _signupForm.value = SignupFormState(passwordError = R.string.invalid_password)
        } else if (!isPasswordValid((retype_password))) {
            _signupForm.value = SignupFormState(retypePasswordError = R.string.invalid_password)
        } else if (!passwordsMatch(password, retype_password)) {
            _signupForm.value = SignupFormState(passwordMismatchError = R.string.password_mismatch)
        } else {
            _signupForm.value = SignupFormState(isDataValid = true)
        }
    }

    // A placeholder username validation check
    private fun isUserNameValid(username: String): Boolean {
        return if (username.contains('@')) {
            Patterns.EMAIL_ADDRESS.matcher(username).matches()
        } else {
            false
        }
    }

    // A placeholder password validation check
    private fun isPasswordValid(password: String): Boolean {
        return password.length > 5
    }

    // Check if password and retype password fields are equal
    private fun passwordsMatch(password: String, retype_password: String): Boolean {
        return password == retype_password
    }

}