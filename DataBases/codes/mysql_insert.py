from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config

"""
Inserts a row into the Books relation of the DB by creating
a query in sql format.Creates Connection, finds configuration.
The new row contains the attributes ISBN(Varchar 45, KEY), 
Title (Varchar 45), Pages(Int), Publication Year (Date),
Publishers_Name(Varchar45, Not Null) and Library Name(Varchar 45).
"""
"""
def insert_book(ISBN, Title, Pages, Publication_Year, Publishers_Name, Library_Name):
	query = "INSERT INTO Books(ISBN, Title, Pages, Publication Year, Publishers_Name, Library_Name)" \
			"VALUES(%s,%s,%s,%s,%s,%s)"
	args = (ISBN, Title, Pages, Publication_Year, Publishers_Name, Library_Name)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('last insert id', cursor.lastrowid)
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()

"""


"""
Inserts a row into the Library relation of the DB by creating
a query in sql format. Creates Connection, finds configuration.
The new row contains the attributes Library Name(Varchar 45, KEY).
"""
def insert_library(Library_Name):
	query = "INSERT INTO Library ( LibraryName )"\
				"VALUE('%s')"
	args = (Library_Name)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)
		#cursor.execute(query)
		if cursor.lastrowid:
			print('last insert id', cursor.lastrowid)
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
"""
def insert_Publisher(Name, Address, Date_of_Est):
	query = "INSERT INTO Publishers(Name, Address, Date of Establishment)" \
			"VALUES(%s,%s,%s)"
	args = (Name, Address, Date_of_Est)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('last insert id', cursor.lastrowid)
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()
"""



 
def main():
	insert_library("NTUA")
 
if __name__ == '__main__':
    main()