package ntua.hci.mysecondandroidapp.ui.login

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.view.inputmethod.EditorInfo
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.annotation.StringRes
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import ntua.hci.mysecondandroidapp.R

class SignupFragment : Fragment() {
    private lateinit var signupViewModel: SignupViewModel

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.activity_signup, container, false)
    }
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val name = view.findViewById<EditText>(R.id.name)
        val username = view.findViewById<EditText>(R.id.username)
        val password = view.findViewById<EditText>(R.id.password)
        val retype_password = view.findViewById<EditText>(R.id.retype_password)
        val signup = view.findViewById<Button>(R.id.signup)

        signupViewModel = ViewModelProvider(this, SignupViewModelFactory())
            .get(SignupViewModel::class.java)

        signupViewModel.signupFormState.observe(viewLifecycleOwner, Observer {
            val signupState = it ?: return@Observer

            // disable signup button unless all text input fields are valid
            signup.isEnabled = signupState.isDataValid

            if (signupState.nameError != null) {
                name.error = getString(signupState.nameError)
            }
            if (signupState.usernameError != null) {
                username.error = getString(signupState.usernameError)
            }
            if (signupState.passwordError != null) {
                password.error = getString(signupState.passwordError)
            }
            if (signupState.retypePasswordError != null) {
                retype_password.error = getString(signupState.retypePasswordError)
            }
            if (signupState.passwordMismatchError != null) {
                retype_password.error = getString(signupState.passwordMismatchError)
            }
        })

        signupViewModel.signupResult.observe(viewLifecycleOwner, Observer {
            val signupResult = it ?: return@Observer

            if (signupResult.error != null) {
                showSignupFailed(signupResult.error)
            }
            if (signupResult.success != null) {
                (activity as LoginActivity).signup(username.text.toString(), password.text.toString())
            }
        })

        name.afterTextChanged {
            signupViewModel.signupDataChanged(
                name.text.toString(),
                username.text.toString(),
                password.text.toString(),
                retype_password.text.toString()
            )
        }

        username.afterTextChanged {
            signupViewModel.signupDataChanged(
                name.text.toString(),
                username.text.toString(),
                password.text.toString(),
                retype_password.text.toString()
            )
        }

        password.afterTextChanged {
            signupViewModel.signupDataChanged(
                name.text.toString(),
                username.text.toString(),
                password.text.toString(),
                retype_password.text.toString()
            )
        }

        retype_password.apply {
            afterTextChanged {
                signupViewModel.signupDataChanged(
                    name.text.toString(),
                    username.text.toString(),
                    password.text.toString(),
                    retype_password.text.toString()
                )
            }

            setOnEditorActionListener { _, actionId, _ ->
                when (actionId) {
                    EditorInfo.IME_ACTION_DONE ->
                        signupViewModel.login(
                            username.text.toString(),
                            password.text.toString()
                        )
                }
                false
            }

            signup.setOnClickListener {
                signupViewModel.login(
                    username.text.toString(),
                    password.text.toString())
            }
        }
    }

    private fun showSignupFailed(@StringRes errorString: Int) {
        Toast.makeText(activity?.applicationContext, errorString, Toast.LENGTH_SHORT).show()
    }

}
