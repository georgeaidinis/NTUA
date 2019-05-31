#coding=utf-8

from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config


def update_books (ISBN = '', Title = '', Pages = 0, Publication_Year = 500, Publisher = '', Library = '', ISBN_KEY = '',  condition = ''):
	coma_counter = [0]*6
	attribute_list = ["ISBN = '", "Title = '", "Pages = ", "Publication_Year = ", "Publishers_Name = '", "LibraryName = '"]
	i = 0
	
	if ISBN != '':
		coma_counter[0] +=1
	if Title != '':
		coma_counter[1] +=1
	if Pages != 0:
		coma_counter[2] +=1
	if Publication_Year != 500:
		coma_counter[3] +=1
	if Publisher != '':
		coma_counter[4] +=1
	if Library != '':
		coma_counter[5] +=1
	
	j = sum(coma_counter)
	List = ["UPDATE Books SET "]

	if ISBN != '' and j!=1:
		List += attribute_list[0]
		List += ISBN
		List += "',"
		j = j-1
	elif ISBN != '' and j==1: 
		List += attribute_list[0]
		List += ISBN
		List += "'"

	
	if Title != '' and j!=1:
		List += attribute_list[1]
		List += Title
		List += "',"
		j = j-1
	elif Title != '' and j==1: 
		List += attribute_list[1]
		List += Title
		List += "'"


	if Pages != 0 and j!=1:
		List += attribute_list[2]
		List += Pages
		List += "',"
		j = j-1
	elif Pages != 0 and j==1: 
		List += attribute_list[2]
		List += Pages
		List += "'"


	if Publication_Year != 500 and j!=1:
		List += attribute_list[3]
		List += Publication_Year
		List += "',"
		j = j-1
	elif Publication_Year != 500 and j==1: 
		List += attribute_list[3]
		List += Publication_Year
		List += "'"

	if Publisher != '' and j!=1:
		List += attribute_list[4]
		List += Publisher
		List += "',"
		j = j-1
	elif Publisher != '' and j==1: 
		List += attribute_list[4]
		List += Publisher
		List += "'"

	elif Library != '' and j==1: 
		List += attribute_list[5]
		List += Library
		List += "'"


	List += "Where "
	if ISBN_KEY != '':
		List += ISBN_KEY
	else:
		List += condition
	List += ";"

	query = ''.join(List)
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

def update_library (LibraryName):

	List = ["UPDATE Library SET LibraryName = '", LibraryName,"';"]
	query = ''.join(List)

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

def update_authors(AuthorID = 0, Name = '', Surname = '', Birthdate = ''):
	oma_counter = [0]*4
	attribute_list = ["AuthorID = ", "Name = '", "Surname = '", "Birhtdate = '"]
	i = 0
	
	if ISBN != '':
		coma_counter[0] +=1
	if Title != '':
		coma_counter[1] +=1
	if Pages != 0:
		coma_counter[2] +=1
	if Publication_Year != 500:
		coma_counter[3] +=1
	if Publisher != '':
		coma_counter[4] +=1
	if Library != '':
		coma_counter[5] +=1
	
	j = sum(coma_counter)
	List = ["UPDATE Books SET "]


def main():

if __name__ == '__main__':
    main()