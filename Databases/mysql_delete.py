#coding=utf-8

from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
from csv_reader import 	read_the_file
from split import div_first_last


def delete_Books(ISBN = '', condition = ''):
	if ISBN== '' and condition=='':
		query = "DELETE FROM Books;"
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

	elif ISBN!= '':
		query = "DELETE FROM Books WHERE ISBN = '"
		query += ISBN
		query +="';"
	else:
		query = "DELETE FROM Books WHERE  "
		query += condition
		query +=";"
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




def delete_Publishers(Name = '', condition=''):
	if Name== '' and condition=='':
		query = "DELETE FROM Publishers;"
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

	elif Name!= '':
		query = "DELETE FROM Publishers WHERE Name = '"
		query += Name
		query += "';"
	else:
		query = "DELETE FROM Publishers WHERE "
		query += condition
		query += ";"
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


def delete_Authors(AuthorID = 0, condition = ''):
	if AuthorID== 0 and condition=='':
		query = "DELETE FROM Authors;"
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

	elif AuthorID!= 0:
		query = "DELETE FROM Authors WHERE AuthorID = "
		query += str(AuthoID)
		query += ";"
	else:
		query = "DELETE FROM Authors WHERE "
		query += condition
		query += ";"
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

def delete_Members(MemberID = 0, condition = ''):
	if MemberID== 0 and condition=='':
		query = "DELETE FROM Members;"
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

	elif MemberID!= 0:
		query = "DELETE FROM Members WHERE MemberID = "
		query += str(MemberID)
		query += ";"
	else:
		query = "DELETE FROM Members WHERE "
		query += condition
		query += ";"
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














def main():
	delete_Books(ISBN = "")
 
if __name__ == '__main__':
    main()