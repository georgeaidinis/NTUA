#coding=utf-8

from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
from csv_reader import 	read_the_file
from split import div_first_last



"""
Contents:

1)	insert_book
2)	insert_Library
3)	insert_Publisher
4)	insert_Member
5)	insert_Author
6)	insert_Staff
7)	insert_Copy
8)	insert_Authored
9)	insert_Belongs
10)	insert_Temporary
11)	insert_Permanent
12)	insert_Borrows
13)	insert_Category
14)	insert_Reminds



main


"""







"""
Inserts a row into the Books relation of the DB by creating
a query in sql format.Creates Connection, finds configuration.
The new row contains the attributes ISBN(Varchar 45, KEY), 
Title (Varchar 45), Pages(Int), Publication Year (Date),
Publishers_Name(Varchar45, Not Null) and Library Name(Varchar 45).
"""
def insert_book(ISBN, Title, Pages, Publication_Year, Publishers_Name, Library_Name, Author):
	query = "INSERT INTO Books VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
	AuthorName, AuthorSur = div_first_last(Author)
	args = (ISBN, Title, Pages, Publication_Year, Publishers_Name, Library_Name, AuthorName, AuthorSur)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()




"""
Inserts a row into the Library relation of the DB by creating
a query in sql format. Creates Connection, finds configuration.
The new row contains the attributes Library Name(Varchar 45, KEY).
"""
def insert_library(Library_Name):
	List = ["INSERT INTO Library VALUE('",Library_Name,"')"]
	query = ''.join(List)
	#args = (Library_Name)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()



"""
Inserts a row into the Publishers relation of the DB by creating
a query in sql format.Creates Connection, finds configuration.
The new row contains the attributes Name(Varchar 45, KEY), 
Address (Varchar 45),Date of Establishment (Date),
"""

def insert_Publisher(Name, Date_of_Est, Address):
	query = "INSERT INTO Publishers VALUES(%s,%s,%s)"
	args = (Name, Address, Date_of_Est)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()


"""
Inserts a row into the Members relation of the DB by creating
a query in sql format.Creates Connection, finds configuration.
The new row contains the attributes MemberID (INT, automated KEY)
Birthdate(DATE),Address (Varchar 45),Name(Varchar 45), 
Surname(Varchar 45), Number of Books(INT), Can_Borrow?(TINYINT),
and LibraryName(Varchar 45).
"""

def insert_Member(Name,Surname,Address,num_books_borrowed,Birthdate,Can_Borrow, Library='NTUA'):
	query = "INSERT INTO Members(Birthdate, Address, Name, Surname, num_books_borrowed, Can_Borrow, LibraryName) VALUES(%s , %s , %s , %s , %s , %s , %s )"
	args = (Birthdate, Address, Name, Surname, num_books_borrowed, 1, Library)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()

"""
Inserts a row into the Authors relation of the DB by creating
a query in sql format.Creates Connection, finds configuration.
The new row contains the attributes AuthorID (INT, automated KEY),
Name(Varchar 45), Surname(Varchar 45), Birthdate(DATE)
"""

def insert_Author(Name, Surname, Birthdate):
	query = "INSERT INTO Authors(Name, Surname, Birthdate) VALUES(%s , %s , %s )"
	args = (Name, Surname, Birthdate)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()




"""
Inserts a row into the Staff relation of the DB by creating
a query in sql format.Creates Connection, finds configuration.
The new row contains the attributes StaffID (INT, automated KEY),
Name(Varchar 45),Pay (INT), Surname(Varchar 45) and 
LibraryName(Varchar 45).
"""
def insert_Staff(Name,Pay,Surname ,LibraryName):
	query = "INSERT INTO Staff(Name,Pay,Surname ,LibraryName) VALUES(  %s , %s , %s , %s)"
	args = ( Name, Pay, Surname, LibraryName)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()


def insert_copy(Number, Books_ISBN, Position):
	query = "INSERT INTO Copy VALUES (%s,%s,%s)"
	args = (Books_ISBN, Number, Position)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()
 





def insert_Copy(Number, Books_ISBN, Position):
	query = "INSERT INTO Copy VALUES (%s,%s,%s)"
	args = (Books_ISBN, Number, Position)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()
 

def insert_Authored(Authors_AuthorID, Books_ISBN):
	query = "INSERT INTO Authored VALUES (%s,%s)"
	args = (Authors_AuthorID, Books_ISBN)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()


def insert_Belongs(Books_ISBN, Category_Name):
	query = "INSERT INTO Belongs VALUES (%s,%s)"
	args = (Books_ISBN, Category_Name)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()



def insert_Temporary(Staff_StaffID, ContractID):
	query = "INSERT INTO Temporary VALUES (%s,%s)"
	args = (Staff_StaffID, ContractID)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()


def insert_Permanent(Staff_StaffID, Hiring_Date):
	query = "INSERT INTO Permanent VALUES (%s,%s)"
	args = (Staff_StaffID, Hiring_Date)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()

def insert_Borrows(Members_MemberID, Copy_Number, Copy_Books_ISBN, Start_Date, Return_Date, Due_Date):
	query = "INSERT INTO Borrows VALUES (%s,%s,%s,%s,%s,%s)"
	args = (Members_MemberID, Copy_Number, Copy_Books_ISBN, Start_Date, Return_Date, Due_Date)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()

def insert_Category(Name, Parent_category):
	query = "INSERT INTO Category VALUES (%s,%s)"
	args = (Name, Parent_category)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()

def insert_Reminds(Staff_StaffID, Members_MemberID, Date_of_Reminder):
	query = "INSERT INTO Reminds VALUES (%s,%s,%s)"
	args = (Staff_StaffID, Members_MemberID, Date_of_Reminder)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()


def main():
	insert_library('NTUA')
	file_name = "publishers.csv"
	for x in read_the_file(file_name):
		insert_Publisher(x[0],x[1],x[2])
	file_name = "books.csv"
	for x in read_the_file(file_name):
		insert_book(x[0],x[1],x[2],x[3],x[4],x[5],x[6])
	file_name = "users.csv"
	for x in read_the_file(file_name):
		insert_Member(x[1],x[2],x[3],x[4],x[5],x[6])
	for x in read_the_file('authors.csv'):
		insert_Author(x[1],x[2],x[3])
	for x in read_the_file('copies.csv'):
		insert_copy(*x)
	#insert_Member("George","Aidinis","Pindou",0,"1998-06-04",1,"NTUA")
	insert_Staff("Theodor", 42,"Tsilivis", "NTUA")
	insert_Staff("George", 4200,"Aidinis", "NTUA")
	insert_Staff("Pheivws", 420,"Kalogiannis", "NTUA")
	insert_Staff("Donald John", 3,"Trump", "NTUA")
	insert_Staff("Melania", 4,"Trump", "NTUA")
	insert_Staff("Ivanka", 5,"Trump", "NTUA")
	insert_Staff("Donald Jr", 6,"Trump", "NTUA")
	insert_Staff("Tiffany", 7,"Trump", "NTUA")
	insert_Staff("Eric", 8,"Trump", "NTUA")
	"""insert_Borrows(1,1,"101-1312-1148","2019-01-01",'null', "2019-02-01")
	insert_Permanent(4,"2017-01-20")
	insert_Temporary(1,1)
	insert_Belongs("101-1312-2133","Romance")
	insert_Category("Romance", "Romance")
	insert_Reminds(1,12,"null")"""
 
if __name__ == '__main__':
    main()