#coding=utf-8

from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
from csv_reader import 	read_the_file

"""
Inserts a row into the Books relation of the DB by creating
a query in sql format.Creates Connection, finds configuration.
The new row contains the attributes ISBN(Varchar 45, KEY), 
Title (Varchar 45), Pages(Int), Publication Year (Date),
Publishers_Name(Varchar45, Not Null) and Library Name(Varchar 45).
"""
def insert_book(ISBN, Title, Pages, Publication_Year, Publishers_Name, Library_Name):
	query = "INSERT INTO Books VALUES (%s,%s,%s,%s,%s,%s)"
	args = (ISBN, Title, Pages, Publication_Year, Publishers_Name, Library_Name)
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

def insert_Member(MemberID,Name,Surname,Address,Number_of_Books,Birthdate,Can_Borrow):
	query = "INSERT INTO Members VALUES( %s , %s , %s , %s , %s , %s , %s , %s )"
	args = (MemberID, Birthdate, Address, Name, Surname, Number_of_Books, Can_Borrow, 'NTUA')
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
		insert_book(x[0],x[1],x[2],x[3],x[4],x[5])
	file_name = "users.csv"
	for x in read_the_file(file_name):
		insert_Member(x[0],x[1],x[2],x[3],x[4],x[5],x[6])
	
 
if __name__ == '__main__':
    main()