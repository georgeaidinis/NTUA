from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml
import mysql_insert
import mysql_update
import mysql_delete

app = Flask(__name__, static_url_path='/static')

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    return render_template('Home.html')

@app.route("/View")
def View():
    return render_template("View.html")

@app.route("/RestrictedView")
def RestrictedView():
    return render_template("RestrictedView.html")

@app.route("/Edit")
def Edit():
    return render_template("Edit.html")

@app.route("/InsertBooks",methods=['GET', 'POST'])
def InsertBooks():
    if request.method == 'POST':
        # Fetch form data
        BookDetails = request.form
        ISBN = BookDetails['ISBN']
        Title = BookDetails['Title']
        Pages = BookDetails['Pages']
        Publication_Year = BookDetails['Publication_Year']
        Publishers_Name = BookDetails['Publishers_Name']
        Author = BookDetails['Author']
        mysql_insert.insert_book(ISBN,Title,Pages,Publication_Year,Publishers_Name,'NTUA',Author)
        return redirect('/Books')
    return render_template("Insert_Books.html")

@app.route("/InsertPublishers",methods=['GET', 'POST'])
def InsertPublishers():
    if request.method == 'POST':
        # Fetch form data
        PublisherDetails = request.form
        Name = PublisherDetails['Name']
        Address = PublisherDetails['Address']
        Date_of_Establishment = PublisherDetails['Date of Establishment']
        mysql_insert.insert_Publisher(Name,Date_of_Establishment,Address)
        return redirect('/Publishers')
    return render_template("Insert_Publishers.html")

@app.route("/InsertMembers",methods=['GET', 'POST'])
def InsertMembers():
    if request.method == 'POST':
        # Fetch form data
        MemberDetails = request.form
        Address = MemberDetails['Address']
        Birthdate = MemberDetails['Birthdate']
        Name = MemberDetails['Name']
        Surname = MemberDetails['Surname']
        mysql_insert.insert_Member(Name,Surname,Address,0,Birthdate,1,'NTUA')
        return redirect('/Members')
    return render_template("Insert_Members.html")

@app.route("/UpdateBooks",methods=['GET', 'POST'])
def UpdateBooks():
    if request.method == 'POST':
        # Fetch form data
        BookDetails = request.form
        Old_ISBN = BookDetails['Old_ISBN']
        New_ISBN = BookDetails['New_ISBN']
        Title = BookDetails['Title']
        Pages = BookDetails['Pages']
        Publication_Year = BookDetails['Publication_Year']
        Publishers_Name = BookDetails['Publishers_Name']
        Author = BookDetails['Author']
        mysql_update.update_books(New_ISBN,Title,Pages,Publication_Year,Publishers_Name,'',Author,Old_ISBN,'')
        return redirect('/Books')
    return render_template("Update_Books.html")

@app.route("/UpdatePublishers",methods=['GET', 'POST'])
def UpdatePublishers():
    if request.method == 'POST':
        # Fetch form data
        PublisherDetails = request.form
        Name = PublisherDetails['Name']
        Address = PublisherDetails['Address']
        Date_of_Establishment = PublisherDetails['Date of Establishment']
        New_name = PublisherDetails['New Name']
        mysql_update.update_publishers(New_name,Date_of_Establishment,Address,Name,'')
        return redirect('/Publishers')
    return render_template("Update_Publishers.html")

@app.route("/UpdateMembers",methods=['GET', 'POST'])
def UpdateMembers():
    if request.method == 'POST':
        # Fetch form data
        MemberDetails = request.form
        MemberID = MemberDetails['MemberID']
        Address = MemberDetails['Address']
        Birthdate = MemberDetails['Birthdate']
        Number_of_Borrowed_Books = MemberDetails['Number_of_Borrowed_Books']
        Can_Borrow = MemberDetails['Can_Borrow']
        Name = MemberDetails['Name']
        Surname = MemberDetails['Surname']
        mysql_update.update_members(MemberID,Name,Surname,Address,Number_of_Borrowed_Books,Birthdate,Can_Borrow,'NTUA',MemberID,'')
        return redirect('/Members')
    return render_template("Update_Members.html")

@app.route("/DeleteBooks",methods=['GET', 'POST'])
def DeleteBooks():
    if request.method == 'POST':
        # Fetch form data
        BookDetails = request.form
        ISBN = BookDetails['ISBN']
        mysql_delete.delete_Books(ISBN,'')
        return redirect('/Books')
    return render_template("Delete_Books.html")

@app.route("/DeletePublishers",methods=['GET', 'POST'])
def DeletePublishers():
    if request.method == 'POST':
        # Fetch form data
        PublisherDetails = request.form
        Name = PublisherDetails['Name']
        mysql_delete.delete_Publishers(Name,'')
        return redirect('/Publishers')
    return render_template("Delete_Publishers.html")

@app.route("/DeleteMembers",methods=['GET', 'POST'])
def DeleteMembers():
    if request.method == 'POST':
        # Fetch form data
        MemberDetails = request.form
        MembersID = MemberDetails['MembersID']
        mysql_delete.delete_Members(MembersID,'')
        return redirect('/Members')
    return render_template("Delete_Members.html")

@app.route("/About")
def About():
    return render_template("About.html")

@app.route("/Authors")
def Authors():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Authors")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template("Authors.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/Publishers")
def Publishers():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Publishers")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template("Publishers.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/Copies")
def Copies():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("""SELECT Books.ISBN,Books.Title,count(Copy.Number)
    FROM Copy , Books
    WHERE Copy.Books_ISBN = Books.ISBN
    GROUP BY Books.ISBN""")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template("Copies.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/Members")
def Members():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Members")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template("Members.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/RestrictedMembers")
def RestrictedMembers():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Members_view")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template("RestrictedMembers.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/Books")
def Books():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Books")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template("Books.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/RestrictedAuthors")
def restrictedAuthors():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Authors_view")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template("RestrictedAuthors.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/RestrictedPublishers")
def restrictedPublishers():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Publishers_view")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template("RestrictedPublishers.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/RestrictedCopies")
def restrictedCopies():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("""SELECT Books_view.ISBN,Books_view.Title,count(Copy_view.Number)
    FROM Copy_view , Books_view
    WHERE Copy_view.Books_ISBN = Books_view.ISBN
    GROUP BY Books_view.ISBN""")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template("RestrictedCopies.html",userDetails=userDetails)
    return render_template("Error.html")


@app.route("/RestrictedBooks")
def restrictedBooks():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Books_view")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template("RestrictedBooks.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/Library")
def Library():
    return render_template("Library.html")

@app.route("/Employees")
def Employees():
    return render_template("Employees.html")


@app.route("/Error")
def Error():
    return render_template("Error.html")


if __name__ == '__main__':
    app.run(debug=True)
