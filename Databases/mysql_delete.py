#coding=utf-8

from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
from csv_reader import 	read_the_file
from split import div_first_last



"""
Contents:

1)	delete_book
2)	delete_Library
3)	delete_Author
4)	delete_Member
5)	delete_Publisher
6)	delete_Staff
7)	delete_Copy
8)	delete_Authored
9)	delete_Belongs
10)	delete_Temporary
11)	delete_Permanent
12)	delete_Borrows
13)	delete_Category
14)	delete_Reminds



main


"""





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


def delete_Library(LibraryName = '', condition = ''):
	if LibraryName== '' and condition=='':
		query = "DELETE FROM Library;"
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

	elif LibraryName!= '':
		query = "DELETE FROM Library WHERE LibraryName = '"
		query += LibraryName
		query +="';"
	else:
		query = "DELETE FROM Library WHERE  "
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
	if MemberID == '0':
		MemberID = 0
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



def delete_Staff(StaffID = 0, condition = ''):
	if StaffID == '0':
		StaffID = 0
	if StaffID== 0 and condition=='':
		query = "DELETE FROM Staff;"
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

	elif StaffID!= 0:
		query = "DELETE FROM Staff WHERE StaffID = "
		query += StaffID
		query += "';"
	else:
		query = "DELETE FROM Staff WHERE "
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



def delete_Copy(Books_ISBN = '', Number = 0, condition = ''):
	if Number == '0':
		Number = 0

	if Books_ISBN == '' and  Number== 0 and condition=='':
		query = "DELETE FROM Copy;"
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

	elif Books_ISBN != '' and Number!= 0:
		query = "DELETE FROM Copy WHERE Books_ISBN = '"
		query += Books_ISBN
		query += "', Number = "
		query += Number
		query += ";"
	else:
		query = "DELETE FROM Copy WHERE "
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


def delete_Authored(Authors_AuthorID = 0, condition = ''):
	if Authors_AuthorID == '0':
		Authors_AuthorID = 0
	if Authors_AuthorID== 0 and condition=='':
		query = "DELETE FROM Authored;"
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

	elif Authors_AuthorID!= 0:
		query = "DELETE FROM Authored WHERE Authors_AuthorID = "
		query += Authors_AuthorID
		query += "';"
	else:
		query = "DELETE FROM Authored WHERE "
		query += Authors_AuthorID
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


def delete_Belongs(Books_ISBN = '', Category_Name = ''):
	if Books_ISBN == '' and  Category_Name== '' and condition=='':
		query = "DELETE FROM Belongs;"
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

	elif Books_ISBN != '' and Category_Name!= '':
		query = "DELETE FROM Belongs WHERE Books_ISBN = '"
		query += Books_ISBN
		query += "', Category_Name = '"
		query += Category_Name
		query += "';"
	else:
		query = "DELETE FROM Belongs WHERE "
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


def delete_Temporary(Staff_StaffID = 0,condition = ''):
	if Staff_StaffID == '0':
		Staff_StaffID = 0
	if Staff_StaffID== 0 and condition=='':
		query = "DELETE FROM Temporary;"
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

	elif Staff_StaffID!= 0:
		query = "DELETE FROM Temporary WHERE Staff_StaffID = "
		query += Staff_StaffID
		query += "';"
	else:
		query = "DELETE FROM Temporary WHERE "
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


def delete_Permanent(Staff_StaffID = 0,condition = ''):
	if Staff_StaffID == '0':
		Staff_StaffID = 0
	if Staff_StaffID== 0 and condition=='':
		query = "DELETE FROM Permanent;"
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

	elif Staff_StaffID!= 0:
		query = "DELETE FROM Permanent WHERE Staff_StaffID = "
		query += Staff_StaffID
		query += "';"
	else:
		query = "DELETE FROM Permanent WHERE "
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

def delete_Borrows(MemberID = 0, Copy_Books_ISBN = '',Copy_Number = 0, condition = ''):
	if MemberID == '0':
		MemberID = 0
	if Copy_Number == '0':
		Copy_Number = 0
	if MemberID == 0 and Copy_Books_ISBN == '' and Copy_Number == 0 and condition == '':
		query = "DELETE FROM Borrows;"
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

	elif MemberID!= 0 and Copy_Books_ISBN !='' and Copy_Number != 0:
		query = "DELETE FROM Borrows WHERE MemberID = "
		query += MemberID
		query += ", Copy_Books_ISBN = '"
		query += Copy_Books_ISBN
		query += "', Copy_Number = "
		query += Copy_Number
		query += ";"
	else:
		query = "DELETE FROM Borrows WHERE "
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

def delete_Category(Name = '', condition = ''):
	if Name== '' and condition=='':
		query = "DELETE FROM Category;"
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
		query = "DELETE FROM Category WHERE Name = '"
		query += Name
		query += "';"
	else:
		query = "DELETE FROM Category WHERE "
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

def delete_Reminds(Staff_StaffID = 0, Members_MemberID = 0, condition = ''):
	if Staff_StaffID == '0':
		Staff_StaffID = 0
	if Members_MemberID == '0':
		Members_MemberID = 0

	if Staff_StaffID== 0 and Members_MemberID== 0 and condition=='':
		query = "DELETE FROM Reminds;"
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

	elif Staff_StaffID != 0 and Members_MemberID != 0 :
		query = "DELETE FROM Reminds WHERE Staff_StaffID = "
		query += Staff_StaffID
		query += ", Members_MemberID = "
		query += Members_MemberID
		query += ";"
	else:
		query = "DELETE FROM Reminds WHERE "
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
