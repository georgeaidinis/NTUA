package ntua.hci.mysecondandroidapp.ui.login

import android.app.Activity
import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.widget.EditText
import android.widget.Toast
import android.content.ContentValues.TAG
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.FirebaseUser
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase


import ntua.hci.mysecondandroidapp.R
import ntua.hci.mysecondandroidapp.ui.main.MainActivity

class LoginActivity : AppCompatActivity() {
    private lateinit var auth: FirebaseAuth

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        auth = Firebase.auth

        setContentView(R.layout.activity_login)
        setTitle(R.string.app_name)
    }
    public override fun onStart() {
        super.onStart()

        // If the user is logged in display the Main Activity
        if (auth.currentUser != null) {
            updateUI()
        }
    }

    fun login(username: String, password: String) {
        auth.signInWithEmailAndPassword(username, password)
            .addOnCompleteListener(this) { task ->
                if (task.isSuccessful) {
                    // Sign in success, update UI with the signed-in user's information
                    Log.d(TAG, "signInWithEmail:success")

                    updateUI()
                } else {
                    // If sign in fails, display a message to the user.
                    Log.w(TAG, "signInWithEmail:failure", task.exception)
                    Toast.makeText(baseContext, R.string.login_failed,
                        Toast.LENGTH_SHORT).show()
                }
            }
    }

    fun signup(username: String, password: String) {
        auth.createUserWithEmailAndPassword(username, password)
            .addOnCompleteListener(this) { task ->
                if (task.isSuccessful) {
                    // Sign in success, update UI with the signed-in user's information
                    Log.d(TAG, "createUserWithEmail: success")
                    val currentUser = auth.currentUser

                    sendEmailVerification(currentUser)
                    updateUI()
                } else {
                    // If sign in fails, display a message to the user.
                    Log.w(TAG, "createUserWithEmail: failure", task.exception)
                    Toast.makeText(baseContext, R.string.signup_failed,
                        Toast.LENGTH_SHORT).show()
                }
            }
    }
    private fun sendEmailVerification(user: FirebaseUser?) {
        user!!.sendEmailVerification().addOnCompleteListener(this) { task ->
            if (task.isSuccessful) {
                Log.d(TAG, "sendEmailVerification: success")
                Toast.makeText(baseContext, getString(R.string.email_sent) + " " + user.email,
                    Toast.LENGTH_SHORT).show()
            } else {
                Log.w(TAG, "sendEmailVerification: failure", task.exception)
                Toast.makeText(baseContext, R.string.email_failed,
                    Toast.LENGTH_SHORT).show()
            }
        }
    }
    private fun updateUI() {
        val main = Intent(this, MainActivity::class.java)
        startActivity(main)

        this.setResult(Activity.RESULT_OK)

        //Complete and destroy login activity once successful
        this.finish()
    }


}

/**
 * Extension function to simplify setting an afterTextChanged action to EditText components.
 */
fun EditText.afterTextChanged(afterTextChanged: (String) -> Unit) {
    this.addTextChangedListener(object : TextWatcher {
        override fun afterTextChanged(editable: Editable?) {
            afterTextChanged.invoke(editable.toString())
        }

        override fun beforeTextChanged(s: CharSequence, start: Int, count: Int, after: Int) {}

        override fun onTextChanged(s: CharSequence, start: Int, before: Int, count: Int) {}
    })
}
