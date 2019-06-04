#coding=utf-8

from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
from split import div_first_last


def update_books (ISBN = '', Title = '', Pages = 0, Publication_Year = 0, Publisher = '', LibraryName = '', Author='',ISBN_KEY = '',  condition = ''):
	coma_counter = [0]*8
	if Author == '':
		AuthorName, AuthorSur = '' , ''
	else:
		AuthorName, AuthorSur = div_first_last(Author)
	attribute_list = ["ISBN = '", "Title = '", "Pages = ", "Publication_Year = ", "Publishers_Name = '", "LibraryName = '", "AuthorName = '", "AuthorSur = '"]
	i = 0
	if Pages == '0':
		Pages = 0
	if Publication_Year == '0':
		Publication_Year = 0

	if ISBN != '':
		coma_counter[0] +=1
	if Title != '':
		coma_counter[1] +=1
	if Pages != 0:
		coma_counter[2] +=1
	if Publication_Year != 0:
		coma_counter[3] +=1
	if Publisher != '':
		coma_counter[4] +=1
	if LibraryName != '':
		coma_counter[5] +=1
	if AuthorSur != '':
		coma_counter[6] +=1
	if AuthorSur != '':
		coma_counter[7] +=1

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
		List += ","
		j = j-1
	elif Pages != 0 and j==1:
		List += attribute_list[2]
		List += Pages
		List += ""


	if Publication_Year != 0 and j!=1:
		List += attribute_list[3]
		List += Publication_Year
		List += ","
		j = j-1
	elif Publication_Year != 0 and j==1:
		List += attribute_list[3]
		List += Publication_Year
		List += ""

	if Publisher != '' and j!=1:
		List += attribute_list[4]
		List += Publisher
		List += "',"
		j = j-1
	elif Publisher != '' and j==1:
		List += attribute_list[4]
		List += Publisher
		List += "'"

	if LibraryName != '' and j!=1:
		List += attribute_list[5]
		List += Library
		List += "'"
		j = j-1
	elif LibraryName != '' and j==1:
		List += attribute_list[5]
		List += Publisher
		List += "'"
	if AuthorName != '' and j!=1:
		List += attribute_list[6]
		List += AuthorName
		List += "',"
		j = j-1
	elif AuthorName != '' and j==1:
		List += attribute_list[6]
		List += AuthorName
		List += "'"
	if AuthorSur != '' and j==1:
		List += attribute_list[7]
		List += AuthorSur
		List += "'"
		j = j-1

	if ISBN_KEY!= '' or  condition!='':
		List += "Where "
		if ISBN_KEY != '':
			List += " ISBN = '"
			List += ISBN_KEY
			List += "'"
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

def update_authors(AuthorID = 0, Name = '', Surname = '', Birthdate = '', AuthorID_KEY=0, condition=''):
	coma_counter = [0]*4
	attribute_list = ["AuthorID = ", "Name = '", "Surname = '", "Birhtdate = '"]
	i = 0

	if AuthorID != 0:
		coma_counter[0] +=1
	if Name != '':
		coma_counter[1] +=1
	if Surname != 0:
		coma_counter[2] +=1
	if Birthdate != '':
		coma_counter[3] +=1
	j = sum(coma_counter)

	List = ["UPDATE Authors SET "]
	if AuthorID != 0 and j!=1:
		List += attribute_list[0]
		List += AuthorID
		List += ","
		j = j-1
	elif AuthorID != 0 and j==1:
		List += attribute_list[0]
		List += AuthorID


	if Name != '' and j!=1:
		List += attribute_list[1]
		List += Name
		List += "',"
		j = j-1
	elif Name != '' and j==1:
		List += attribute_list[1]
		List += Name
		List += "'"


	if Surname != '' and j!=1:
		List += attribute_list[2]
		List += Surname
		List += "',"
		j = j-1
	elif Surname != '' and j==1:
		List += attribute_list[2]
		List += Surname
		List += "'"


	if Birthdate != '' and j!=1:
		List += attribute_list[3]
		List += Birthdate
		List += "',"
		j = j-1
	elif Birthdate != '' and j==1:
		List += attribute_list[3]
		List += bi
		List += "'"

	if AuthorID_KEY!= 0 or  condition!='':
		List += "Where "
		if AuthorID_KEY != 0:
			List += "AuthorID = '"
			List += AuthorID_KEY
			List += "'"
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


def update_members(MemberID=0,Name='',Surname='',Address='',num_books_borrowed=-1,Birthdate='',Can_Borrow=-1, LibraryName='',MemberID_KEY=0, condition=''):
	coma_counter = [0]*8
	attribute_list = ["MemberID = ", "Name = '", "Surname = '", "Address = '", "num_books_borrowed = ", "Birthdate = '", "Can_Borrow = ", "LibraryName = '"]
	i = 0
	if Can_Borrow == '0':
		Can_Borrow = 0
	if Can_Borrow == '1':
		Can_Borrow = 1
	if int(num_books_borrowed) <0 or int(num_books_borrowed)>5:
		num_books_borrowed == '-1'
	if int(num_books_borrowed) == 5:
		Can_Borrow = 0
	if MemberID != 0:
		coma_counter[0] +=1
	if Name != '':
		coma_counter[1] +=1
	if Surname != '':
		coma_counter[2] +=1
	if Address != '':
		coma_counter[3] +=1
	if num_books_borrowed != '-1' or num_books_borrowed != -1:
		coma_counter[4] +=1
	if Birthdate != '':
		coma_counter[5] +=1
	if Can_Borrow == 0 or Can_Borrow == 1:
		coma_counter[6] +=1
	if LibraryName != '':
		coma_counter[7] +=1

	j = sum(coma_counter)
	List = ["UPDATE Members SET "]

	if MemberID != 0 and j!=1:
		List += attribute_list[0]
		List += MemberID
		List += ","
		j = j-1
	elif MemberID != 0 and j==1:
		List += attribute_list[0]
		List += MemberID
		List += ""

	if Name != '' and j!=1:
		List += attribute_list[1]
		List += Name
		List += "',"
		j = j-1
	elif Name != '' and j==1:
		List += attribute_list[1]
		List += Name
		List += "'"

	if Surname != 0 and j!=1:
		List += attribute_list[2]
		List += Surname
		List += "',"
		j = j-1
	elif Surname != 0 and j==1:
		List += attribute_list[2]
		List += Surname
		List += "'"
	if Address != '' and j!=1:
		List += attribute_list[3]
		List += Address
		List += "',"
		j = j-1
	elif Address != '' and j==1:
		List += attribute_list[3]
		List += Address
		List += "'"
	if num_books_borrowed != -1 and j!=1:
		List += attribute_list[4]
		List += num_books_borrowed
		List += ","
		j = j-1
	elif num_books_borrowed != -1 and j==1:
		List += attribute_list[4]
		List += num_books_borrowed
		List += ""
	if Birthdate != '' and j!=1:
		List += attribute_list[5]
		List += Birthdate
		List += "',"
		j = j-1
	elif Birthdate != '' and j==1:
		List += attribute_list[5]
		List += Birthdate
		List += "'"
	if (Can_Borrow == 0 or Can_Borrow == 1) and j!=1:
		List += attribute_list[6]
		List += str(Can_Borrow)
		List += ","
		j = j-1
	elif (Can_Borrow == 0 or Can_Borrow == 1) and j==1:
		List += attribute_list[6]
		List += str(Can_Borrow)
		List += ","
	if LibraryName != '' and j!=1:
		List += attribute_list[7]
		List += LibraryName
		List += "'"
		j = j-1
	elif LibraryName != '' and j==1:
		List += attribute_list[7]
		List += LibraryName
		List += "'"

	if MemberID!= 0 or  condition!='':
		List += "Where "
		if MemberID != '':
			List += "MemberID = '"
			List += MemberID
			List += "'"
		else:
			List += condition
	List += ";"
	print(List)
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


def update_publishers(Name='', Date_of_Establishment='', Address='',Name_KEY='', condition=''):
	coma_counter = [0]*3
	attribute_list = ["Name = '", "Date_of_Establishment = ", "Address = '"]
	i = 0

	if Date_of_Establishment == '0':
		Date_of_Establishment = 0
	if Name != '':
		coma_counter[0] +=1
	if Date_of_Establishment != 0:
		coma_counter[1] +=1
	if Address != '':
		coma_counter[2] +=1


	j = sum(coma_counter)
	List = ["UPDATE Publishers SET "]

	if Name != '' and j!=1:
		List += attribute_list[0]
		List += Name
		List += "',"
		j = j-1
	elif Name != '' and j==1:
		List += attribute_list[0]
		List += Name
		List += "'"


	if Date_of_Establishment != 0 and j!=1:
		List += attribute_list[1]
		List += Date_of_Establishment
		List += ","
		j = j-1
	elif Date_of_Establishment != 0 and j==1:
		List += attribute_list[1]
		List += Date_of_Establishment
		List += ""


	if Address != '' and j!=1:
		List += attribute_list[2]
		List += Address
		List += "',"
		j = j-1
	elif Address != '' and j==1:
		List += attribute_list[2]
		List += Address
		List += "'"

	if  Name_KEY != '' or  condition!='':
		List += "Where "
		if Name_KEY != '':
			List += "Name = '"
			List += Name_KEY
			List += "'"
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



def main():
	return

if __name__ == '__main__':
    main()
