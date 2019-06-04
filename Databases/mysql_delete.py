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

	elif ISBN!= '':
		query = "DELETE FROM Books WHERE ISBN = %s;"
		args = (ISBN)
	else:
		query = "DELETE FROM Books WHERE %s;"
		args = (condition)
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




def delete_Publisher(Name = '', condition''):
	if Name== '' and condition=='':
		query = "DELETE FROM Publishers;"
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

	elif Name!= '':
		query = "DELETE FROM Publishers WHERE Name = %s;"
		args = (Name)
	else:
		query = "DELETE FROM Publishers WHERE %s;"
		args = (condition)
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


def delete_Author(AuthorID = 0, condition = ''):
	if AuthorID== 0 and condition=='':
		query = "DELETE FROM Authors;"
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

	elif AuthorID!= 0:
		query = "DELETE FROM Authors WHERE AuthorID = %s;"
		args = (AuthorID)
	else:
		query = "DELETE FROM Authors WHERE %s;"
		args = (condition)
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

def delete_Member(MemberID = 0, condition = ''):
	if MemberID== 0 and condition=='':
		query = "DELETE FROM Members;"
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

	elif MemberID!= 0:
		query = "DELETE FROM Members WHERE MemberID = %s;"
		args = (MemberID)
	else:
		query = "DELETE FROM Members WHERE %s;"
		args = (condition)
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
	return
 
if __name__ == '__main__':
    main()