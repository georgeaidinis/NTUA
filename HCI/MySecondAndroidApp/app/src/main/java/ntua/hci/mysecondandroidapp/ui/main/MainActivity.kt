package ntua.hci.mysecondandroidapp.ui.main

import android.app.Activity
import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase

import ntua.hci.mysecondandroidapp.R
import ntua.hci.mysecondandroidapp.ui.list.ListActivity
import ntua.hci.mysecondandroidapp.ui.login.SplashFragment
import ntua.hci.mysecondandroidapp.ui.login.LoginActivity

class MainActivity : AppCompatActivity() {
    private lateinit var auth: FirebaseAuth

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        auth = Firebase.auth

        if (auth.currentUser?.isEmailVerified == false) {
            Toast.makeText(baseContext, R.string.verify_email,
                    Toast.LENGTH_SHORT).show()
            auth.signOut()
            val test = Intent(this, LoginActivity::class.java)
            startActivity(test)
            this.setResult(Activity.RESULT_OK)
            this.finish()
        }
        setContentView(R.layout.activity_main)
        setTitle(R.string.app_name)
        val welcome: TextView = findViewById<TextView>(R.id.txtNames) as TextView
        val email = auth.currentUser?.email
        val maskedEmail = email?.replace(Regex("@.*"), "")
        val welcomeMsg: String = getString(R.string.txtName) + " " + maskedEmail +"!"
        welcome.text = welcomeMsg


        findViewById<Button>(R.id.btnTerminate).setOnClickListener {
            val test = Intent(this, LoginActivity::class.java)
            startActivity(test)
            auth.signOut()
            this.setResult(Activity.RESULT_OK)
            this.finish()
        }

        findViewById<Button>(R.id.btnOwner).setOnClickListener {
            val list = Intent(this, SplashFragment::class.java)
            startActivity(list)
            this.setResult(Activity.RESULT_OK)
            this.finish()
        }
        findViewById<Button>(R.id.btnSitter).setOnClickListener {
            val list = Intent(this, ListActivity::class.java)
            startActivity(list)

            this.setResult(Activity.RESULT_OK)
            this.finish()
        }


    }
}
