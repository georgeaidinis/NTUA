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

@app.route('/')
def index():
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

@app.route("/Examples")
def Examples():
    return render_template("Examples.html")

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
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Books")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Update_Books.html",userDetails=userDetails)
    return render_template("Error.html")

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
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Publishers")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Update_Publishers.html",userDetails=userDetails)
    return render_template("Error.html")

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
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Members")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Update_Members.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/DeleteBooks",methods=['GET', 'POST'])
def DeleteBooks():
    if request.method == 'POST':
        # Fetch form data
        BookDetails = request.form
        ISBN = BookDetails['ISBN']
        mysql_delete.delete_Books(ISBN,'')
        return redirect('/Books')
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Books")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Delete_Books.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/DeletePublishers",methods=['GET', 'POST'])
def DeletePublishers():
    if request.method == 'POST':
        # Fetch form data
        PublisherDetails = request.form
        Name = PublisherDetails['Name']
        mysql_delete.delete_Publishers(Name,'')
        return redirect('/Publishers')
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Publishers")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Delete_Publishers.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/DeleteMembers",methods=['GET', 'POST'])
def DeleteMembers():
    if request.method == 'POST':
        # Fetch form data
        MemberDetails = request.form
        MembersID = MemberDetails['MembersID']
        mysql_delete.delete_Members(MembersID,'')
        return redirect('/Members')
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Members")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Delete_Members.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/About")
def About():
    return render_template("About.html")

@app.route("/Authors")
def Authors():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Authors")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Authors.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/Publishers")
def Publishers():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Publishers")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
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
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Copies.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/Members")
def Members():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Members")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Members.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/RestrictedMembers")
def RestrictedMembers():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Members_view")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("RestrictedMembers.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/Books")
def Books():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Books")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Books.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/RestrictedAuthors")
def restrictedAuthors():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Authors_view")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("RestrictedAuthors.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/RestrictedPublishers")
def restrictedPublishers():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Publishers_view")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
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
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("RestrictedCopies.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/RestrictedBooks")
def restrictedBooks():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Books_view")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("RestrictedBooks.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/Query1")
def Ex1():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("Select Books_ISBN,Title,Name,Surname,Publication_year from Authored, Authors,Books where Authors.AuthorID = Authors_AuthorID and Books_ISBN = Books.ISBN order by Publication_year;")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Ex1.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/Query2",methods=['GET', 'POST'])
def Ex2():
    if request.method == 'POST':
        # Fetch form data
        CategoryDetails = request.form
        Category = CategoryDetails['Category']
        cur = mysql.connection.cursor()
        a = "select DISTINCT Title  from Belongs, Books , Category Where Category_Name = '"
        a += Category
        a += "' and Books.ISBN = Belongs.Books_ISBN;"
        resultValue = cur.execute(a)
        if resultValue > 0:
            userDetails = cur.fetchall()
        if cur.rowcount == 0 :
            return render_template("Error.html")
        else:
            return render_template("Ex2f.html",userDetails=userDetails)
    return render_template("Ex2.html")

@app.route("/Query3")
def Ex3():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("select ISBN,Title,Total from Books,(select Copy_Books_ISBN,count(*) as Total from Borrows group by Copy_Books_ISBN) NEW WHERE ISBN = NEW.Copy_Books_ISBN;")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Ex3.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/Query4")
def Ex4():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT Books.ISBN,Books.Title,count(Copy.Number) FROM Copy , Books WHERE Copy.Books_ISBN = Books.ISBN GROUP BY Books.ISBN;")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Ex4.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/Query5")
def Ex5():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("select Distinct Name,Surname,Birthdate from Authors where Birthdate > (select avg(Birthdate) from Authors) order by Birthdate DESC;")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Ex5.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/Query6")
def Ex6():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("select distinct ISBN,Title,Name from Books join Publishers on Name=Publishers_Name ORDER by Name;")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Ex6.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/Query7",methods=['GET', 'POST'])
def Ex7():
    if request.method == 'POST':
        # Fetch form data
        NumberDetails = request.form
        Number = NumberDetails['Number']
        cur = mysql.connection.cursor()
        a = "select Name,num_books_borrowed,MemberID from Members , Borrows Where MemberID = Borrows.Members_MemberID group by num_books_borrowed , MemberID having num_books_borrowed >= "
        a += Number
        a += ";"
        resultValue = cur.execute(a)
        print(a)
        if resultValue > 0:
            NumberDetails = cur.fetchall()
        if cur.rowcount == 0 :
            return render_template("Error.html")
        return render_template("Ex7f.html",userDetails=NumberDetails)
    return render_template("Ex7.html")

@app.route("/Query8")
def Ex8():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("Select New.Name , New.Surname,count(Old.ISBN) AS Counter from (Select* from Authors join Authored on AuthorID=Authors_AuthorID) New ,(select ISBN from Books join Borrows on Copy_Books_ISBN = ISBN) Old WHERE Old.ISBN = New.Books_ISBN GROUP BY New.Name,New.Surname ORDER BY Counter DESC LIMIT 5;")
    if resultValue > 0:
        userDetails = cur.fetchall()
    if cur.rowcount == 0 :
        return render_template("Error.html")
    else:
        return render_template("Ex8.html",userDetails=userDetails)
    return render_template("Error.html")

@app.route("/Query9",methods=['GET', 'POST'])
def Ex9():
    if request.method == 'POST':
        # Fetch form data
        NumberDetails = request.form
        Title = NumberDetails['Title']
        cur = mysql.connection.cursor()
        a = "Select ISBN,Title from Books where Title like '%"
        a += Title
        a += "%';"
        resultValue = cur.execute(a)
        print(a)
        if resultValue > 0:
            NumberDetails = cur.fetchall()
        if cur.rowcount == 0 :
            return render_template("Error.html")
        return render_template("Ex9f.html",userDetails=NumberDetails)
    return render_template("Ex9.html")

@app.route("/Query10",methods=['GET', 'POST'])
def Ex10():
    if request.method == 'POST':
        # Fetch form data
        NumberDetails = request.form
        Surname = NumberDetails['Surname']
        cur = mysql.connection.cursor()
        a = "Select Name,Surname from Authors where Surname like '%"
        a += Surname
        a += "%';"
        resultValue = cur.execute(a)
        print(a)
        if resultValue > 0:
            NumberDetails = cur.fetchall()
        if cur.rowcount == 0 :
            return render_template("Error.html")
        return render_template("Ex10f.html",userDetails=NumberDetails)
    return render_template("Ex10.html")

@app.route("/Query11",methods=['GET', 'POST'])
def Ex11():
    if request.method == 'POST':
        # Fetch form data
        NumberDetails = request.form
        Name = NumberDetails['Name']
        cur = mysql.connection.cursor()
        a = "Select Name,Address from Publishers where Name like '%"
        a += Name
        a += "%';"
        resultValue = cur.execute(a)
        print(a)
        if resultValue > 0:
            NumberDetails = cur.fetchall()
        if cur.rowcount == 0 :
            return render_template("Error.html")
        return render_template("Ex11f.html",userDetails=NumberDetails)
    return render_template("Ex11.html")

@app.route("/Query12",methods=['GET', 'POST'])
def Ex12():
    if request.method == 'POST':
        # Fetch form data
        NumberDetails = request.form
        Members_MemberID = NumberDetails['Members_MemberID']
        Copy_Number = NumberDetails['Copy_Number']
        Copy_Books_ISBN = NumberDetails['Copy_Books_ISBN']
        Start_Date = NumberDetails['Start_Date']
        Due_Date = NumberDetails['Due_Date']
        mysql_insert.insert_Borrows(Members_MemberID, Copy_Number, Copy_Books_ISBN, Start_Date, '', Due_Date)
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM Borrows")
        if resultValue > 0:
            userDetails = cur.fetchall()
        if cur.rowcount == 0 :
            return render_template("Error.html")
        else:
            return render_template("Ex12.html",userDetails=userDetails)
        return render_template("Error.html")
    return render_template("Ex12f.html")

@app.route("/Employees")
def Employees():
    return render_template("Employees.html")

@app.route("/Error")
def Error():
    return render_template("Error.html")

if __name__ == '__main__':
    app.run(debug=True)
