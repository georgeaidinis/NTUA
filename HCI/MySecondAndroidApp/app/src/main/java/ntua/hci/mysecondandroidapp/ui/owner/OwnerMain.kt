package ntua.hci.mysecondandroidapp.ui.owner


import android.app.AlertDialog
import android.content.ContentValues.TAG
import android.content.DialogInterface
import android.os.Bundle
import android.text.InputType
import android.util.Log
import android.widget.AdapterView.OnItemClickListener
import android.widget.ArrayAdapter
import android.widget.EditText
import android.widget.ListView
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.ktx.auth
import com.google.firebase.database.*
import com.google.firebase.database.ktx.database
import com.google.firebase.ktx.Firebase
import ntua.hci.mysecondandroidapp.R


class OwnerMain: AppCompatActivity()  {
    private lateinit var auth: FirebaseAuth
    private lateinit var database: DatabaseReference

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        auth = Firebase.auth
        database = Firebase.database.reference

        setContentView(R.layout.activity_pet_owner_main)
        setSupportActionBar(findViewById(R.id.toolbar2))
        setTitle(R.string.app_name)

        val listItems = mutableListOf<String>()
        val adapter = ArrayAdapter<String>(this, R.layout.activity_listview, listItems)
        val listView = findViewById<ListView>(R.id.mobile_list)
        listView.adapter = adapter


        val childEventListener = object : ChildEventListener {
            override fun onChildAdded(dataSnapshot: DataSnapshot, previousChildName: String?) {
                if (listItems.size <= dataSnapshot.key!!.toInt())
                    listItems.add(dataSnapshot.value.toString())

                Log.w(TAG, "onChildAdded $dataSnapshot")
                adapter.notifyDataSetChanged()
            }

            override fun onChildChanged(snapshot: DataSnapshot, previousChildName: String?) {
                Log.w(TAG, "onChildChanged $snapshot")
                adapter.notifyDataSetChanged()
            }

            override fun onChildRemoved(snapshot: DataSnapshot) {
                Log.w(TAG, "onChildRemoved $snapshot")
                adapter.notifyDataSetChanged()
            }

            override fun onChildMoved(snapshot: DataSnapshot, previousChildName: String?) {
                TODO("Not yet implemented")
            }

            override fun onCancelled(error: DatabaseError) {
                TODO("Not yet implemented")
            }

        }

        database.child(auth.currentUser!!.uid).child("items").addChildEventListener(childEventListener)


        listView.onItemClickListener = OnItemClickListener{_, _, position, _ ->
            listItems.removeAt(position)
            database.child(auth.currentUser!!.uid).child("items").setValue(listItems)
        }

        findViewById<FloatingActionButton>(R.id.fab).setOnClickListener {
            val builder: AlertDialog.Builder = AlertDialog.Builder(this)
            builder.setTitle("Εισάγετε το νέο αντικείμενο")
            val input = EditText(this)
            input.inputType = InputType.TYPE_CLASS_TEXT
            builder.setView(input)
            builder.setPositiveButton("OK",
                    DialogInterface.OnClickListener { _, _ ->
                        if (input.text.toString().isNotEmpty()) {
                            listItems.add(input.text.toString())
                            database.child(auth.currentUser!!.uid).child("items").setValue(listItems)
                        }
                    })
            builder.setNegativeButton("Άκυρο",
                    DialogInterface.OnClickListener { dialog, _ -> dialog.cancel() })

            builder.show()
        }
    }
}
