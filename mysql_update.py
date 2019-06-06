#coding=utf-8

from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
from split import div_first_last



"""
Contents:

1)	update_book
2)	update_Library
3)	update_Author
4)	update_Member
5)	update_Publisher
6)	update_Staff
7)	update_Copy
8)	update_Authored
9)	update_Belongs
10)	update_Temporary
11)	update_Permanent
12)	update_Borrows
13)	update_Category
14)	update_Reminds



main


"""





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
		List += " Where "
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
			print('last update id not found')

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
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()

def update_authors(AuthorID = 0, Name = '', Surname = '', Birthdate = '', AuthorID_KEY=0, condition=''):
	coma_counter = [0]*4
	attribute_list = ["AuthorID = ", "Name = '", "Surname = '", "Birthdate = '"]
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
		List += Birthdate
		List += "'"

	if AuthorID_KEY!= 0 or  condition!='':
		List += " Where "
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
			print('last update id not found')

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
		List += " Where "
		if MemberID != '':
			List += "MemberID = '"
			List += MemberID
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
			print('last update id not found')

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
		List += " Where "
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
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()

def update_Staff(StaffID = 0,Name = '',Pay = 0,Surname = '',LibraryName = '', StaffID_KEY = 0, condition = ''):
	coma_counter = [0]*5
	attribute_list = ["StaffID = ", "Name = '", "Pay = ", "Surname = '", "LibraryName = '"]
	i = 0

	if StaffID == '0':
		StaffID = 0


	if StaffID != 0:
		coma_counter[0] +=1
	if Name != '':
		coma_counter[1] +=1
	if Pay != 0:
		coma_counter[2] +=1
	if Surname != '':
		coma_counter[3] +=1
	if LibraryName!='':
		coma_counter[4] +=1


	j = sum(coma_counter)
	List = ["UPDATE Staff SET "]



	if StaffID != 0 and j!=1:
		List += attribute_list[0]
		List += str(StaffID)
		List += ","
		j = j-1
	elif StaffID != 0 and j==1:
		List += attribute_list[0]
		List += str(StaffID)
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


	if Pay != 0 and j!=1:
		List += attribute_list[2]
		List += str(Pay)
		List += ","
		j = j-1
	elif Pay != 0 and j==1:
		List += attribute_list[2]
		List += str(Pay)
		List += ""


	if Surname != '' and j!=1:
		List += attribute_list[3]
		List += Surname
		List += "',"
		j = j-1
	elif Surname != '' and j==1:
		List += attribute_list[3]
		List += Surname
		List += "'"


	if LibraryName != '' and j!=1:
		List += attribute_list[4]
		List += LibraryName
		List += "',"
		j = j-1
	elif LibraryName != '' and j==1:
		List += attribute_list[4]
		List += LibraryName
		List += "'"

	if  StaffID_KEY != 0 or  condition!='':
		List += " Where "
		if StaffID_KEY != '':
			List += "StaffID = "
			List += str(StaffID_KEY)
			List += ""
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
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()


def update_Copy(Number = 0, Books_ISBN = '', Position = '', Number_KEY = 0, Books_ISBN_KEY = '', condition = ''):
	coma_counter = [0]*3
	attribute_list = ["Number = ", "Books_ISBN = '", "Position = '"]

	i = 0

	if Number == '0':
		Number = 0
	if Number_KEY == '0':
		Number_KEY = 0


	if Number != 0:
		coma_counter[0] +=1
	if Books_ISBN != '':
		coma_counter[1] +=1
	if Position != '':
		coma_counter[2] +=1

	j = sum(coma_counter)
	List = ["UPDATE Copy SET "]


	if Number != 0 and j!=1:
		List += attribute_list[0]
		List += str(Number)
		List += ","
		j = j-1
	elif Number != 0 and j==1:
		List += attribute_list[0]
		List += str(Number)
		List += ""


	if Books_ISBN != '' and j!=1:
		List += attribute_list[1]
		List += Books_ISBN
		List += "',"
		j = j-1
	elif Books_ISBN != '' and j==1:
		List += attribute_list[1]
		List += Books_ISBN
		List += "'"

	if Position != '' and j!=1:
		List += attribute_list[2]
		List += Position
		List += "',"
		j = j-1
	elif Position != '' and j==1:
		List += attribute_list[2]
		List += Position
		List += "'"


	if  (Number_KEY != 0 and Books_ISBN_KEY!='') or  condition!='':
		List += " Where "
		if Number_KEY != 0 and Books_ISBN_KEY!='':
			List += "Number = "
			List += str(Number_KEY)
			List += ", Books_ISBN = '"
			List += Books_ISBN_KEY
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
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()


def update_Authored(Authors_AuthorID = 0, Books_ISBN = '', Authors_AuthorID_KEY = 0, Books_ISBN_KEY = '', condition = ''):
	coma_counter = [0]*2
	attribute_list = ["Authors_AuthorID = ", "Books_ISBN = '"]
	i = 0

	if Authors_AuthorID == '0':
		Authors_AuthorID = 0

	if Authors_AuthorID != 0:
		coma_counter[0] +=1
	if Books_ISBN != '':
		coma_counter[1] +=1

	j = sum(coma_counter)
	List = ["UPDATE Authored SET "]

	if Authors_AuthorID != 0 and j!=1:
		List += attribute_list[0]
		List += Authors_AuthorID
		List += ","
		j = j-1
	elif Authors_AuthorID != 0 and j==1:
		List += attribute_list[0]
		List += Authors_AuthorID
		List += ""


	if Books_ISBN != '' and j!=1:
		List += attribute_list[1]
		List += Books_ISBN
		List += "',"
		j = j-1
	elif Books_ISBN != '' and j==1:
		List += attribute_list[1]
		List += Books_ISBN
		List += "'"

	if  (Authors_AuthorID_KEY != 0 and Books_ISBN_KEY!='') or  condition!='':
		List += " Where "
		if Authors_AuthorID_KEY != 0 and Books_ISBN_KEY!='':
			List += "Authors_AuthorID = "
			List += Authors_AuthorID_KEY
			List += ", Books_ISBN = '"
			List += Books_ISBN_KEY
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
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()


def update_Belongs(Books_ISBN = '', Category_Name = '', Books_ISBN_KEY = '', Category_Name_KEY = '', condition = ''):
	coma_counter = [0]*2
	attribute_list = ["Books_ISBN = '", "Category_Name = '"]
	i = 0


	if Books_ISBN != '':
		coma_counter[0] +=1
	if Category_Name != '':
		coma_counter[1] +=1

	j = sum(coma_counter)
	List = ["UPDATE Belongs SET "]


	if Books_ISBN != '' and j!=1:
		List += attribute_list[0]
		List += Books_ISBN
		List += "',"
		j = j-1
	elif Books_ISBN != '' and j==1:
		List += attribute_list[0]
		List += Books_ISBN
		List += "'"

	if Category_Name != '' and j!=1:
		List += attribute_list[1]
		List += Category_Name
		List += "',"
		j = j-1
	elif Category_Name != '' and j==1:
		List += attribute_list[1]
		List += Category_Name
		List += "'"



	if  (Books_ISBN_KEY != '' and Category_Name_KEY!='') or  condition!='':
		List += " Where "
		if Books_ISBN_KEY != '' and Category_Name_KEY!='':
			List += "Books_ISBN = '"
			List += Books_ISBN_KEY
			List += "', Category_Name = '"
			List += Books_ISBN_KEY
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
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()



def update_Temporary(Staff_StaffID = 0, ContractID = 0, Staff_StaffID_KEY = 0, condition = ''):

	coma_counter = [0]*2
	attribute_list = ["Staff_StaffID = ", "ContractID = "]
	i = 0

	if Staff_StaffID == '0':
		Staff_StaffID = 0

	if ContractID == '0':
		ContractID = 0


	if Staff_StaffID_KEY == '0':
		Staff_StaffID_KEY = 0


	if Staff_StaffID != 0:
		coma_counter[0] +=1
	if ContractID != 0:
		coma_counter[1] +=1

	j = sum(coma_counter)
	List = ["UPDATE Temporary SET "]

	if Staff_StaffID != 0 and j!=1:
		List += attribute_list[0]
		List += str(Staff_StaffID)
		List += ","
		j = j-1
	elif Staff_StaffID != 0 and j==1:
		List += attribute_list[0]
		List += str(Staff_StaffID)
		List += ""


	if ContractID != 0 and j!=1:
		List += attribute_list[1]
		List += str(ContractID)
		List += ","
		j = j-1
	elif ContractID != 0 and j==1:
		List += attribute_list[1]
		List += str(ContractID)
		List += ""

	if  Staff_StaffID_KEY != 0 or  condition!='':
		List += " Where "
		if Staff_StaffID_KEY != 0:
			List += "Staff_StaffID = "
			List += str(Staff_StaffID_KEY)
			List += ""
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
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()


def update_Permanent(Staff_StaffID = 0, Hiring_Date = '', Staff_StaffID_KEY = 0, condition = ''):
	coma_counter = [0]*2
	attribute_list = ["Staff_StaffID = ", "Hiring_Date = '"]
	i = 0

	if Staff_StaffID == '0':
		Staff_StaffID = 0

	if Staff_StaffID_KEY == '0':
		Staff_StaffID_KEY = 0


	if Staff_StaffID != 0:
		coma_counter[0] +=1
	if Hiring_Date != '':
		coma_counter[1] +=1

	j = sum(coma_counter)
	List = ["UPDATE Permanent SET "]

	if Staff_StaffID != 0 and j!=1:
		List += attribute_list[0]
		List += str(Staff_StaffID)
		List += ","
		j = j-1
	elif Staff_StaffID != 0 and j==1:
		List += attribute_list[0]
		List += str(Staff_StaffID)
		List += ""


	if Hiring_Date != '' and j!=1:
		List += attribute_list[1]
		List += Hiring_Date
		List += "',"
		j = j-1
	elif Hiring_Date != '' and j==1:
		List += attribute_list[1]
		List += Hiring_Date
		List += "'"

	if  Staff_StaffID_KEY  or  condition!='':
		List += " Where "
		if Staff_StaffID_KEY != 0:
			List += "Staff_StaffID = "
			List += str(Staff_StaffID_KEY)
			List += ""
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
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()

def update_Borrows(Members_MemberID = 0, Copy_Number = 0, Copy_Books_ISBN = '', Start_Date = '', Return_Date = '', Due_Date = '', Members_MemberID_KEY = 0, Copy_Number_KEY = 0, Copy_Books_ISBN_KEY = '', condition = ''):
	coma_counter = [0]*6
	attribute_list = ["Members_MemberID = ", "Copy_Number = ", "Copy_Books_ISBN = '", "Start_Date = '", "Return_Date = '", "Due_Date = '"]
	i = 0
	if Members_MemberID == '0':
		Members_MemberID = 0
	if Copy_Number == '0':
		Copy_Number = 0


	if Members_MemberID != 0:
		coma_counter[0] +=1
	if Copy_Number != 0:
		coma_counter[1] +=1
	if Copy_Books_ISBN != '':
		coma_counter[2] +=1
	if Start_Date != '':
		coma_counter[3] +=1
	if Return_Date != '':
		coma_counter[4] +=1
	if Due_Date != '':
		coma_counter[5] +=1

	j = sum(coma_counter)
	List = ["UPDATE Borrows SET "]



	if Members_MemberID != 0 and j!=1:
		List += attribute_list[0]
		List += str(Members_MemberID)
		List += ","
		j = j-1
	elif Members_MemberID != 0 and j==1:
		List += attribute_list[0]
		List += str(Members_MemberID)
		List += ""


	if Copy_Number != 0 and j!=1:
		List += attribute_list[1]
		List += str(Copy_Number)
		List += ","
		j = j-1
	elif Copy_Number != 0 and j==1:
		List += attribute_list[1]
		List += str(Copy_Number)
		List += ""


	if Copy_Books_ISBN != '' and j!=1:
		List += attribute_list[2]
		List += Copy_Books_ISBN
		List += "',"
		j = j-1
	elif Copy_Books_ISBN != '' and j==1:
		List += attribute_list[2]
		List += Copy_Books_ISBN
		List += "'"


	if Start_Date != '' and j!=1:
		List += attribute_list[3]
		List += Start_Date
		List += "',"
		j = j-1
	elif Start_Date != '' and j==1:
		List += attribute_list[3]
		List += Start_Date
		List += "'"


	if Return_Date != '' and j!=1:
		List += attribute_list[4]
		List += Return_Date
		List += "',"
		j = j-1
	elif Return_Date != '' and j==1:
		List += attribute_list[4]
		List += Return_Date
		List += "'"


	if Due_Date != '' and j!=1:
		List += attribute_list[5]
		List += Due_Date
		List += "',"
		j = j-1
	elif Due_Date != '' and j==1:
		List += attribute_list[5]
		List += Due_Date
		List += "'"



	if  (Members_MemberID_KEY != 0 and Copy_Number_KEY!=0 and Copy_Books_ISBN_KEY!='') or  condition!='':
		List += " Where "
		if Members_MemberID_KEY != 0 and Copy_Number_KEY!=0 and Copy_Books_ISBN_KEY!='':
			List += "Members_MemberID = "
			List += str(Members_MemberID_KEY)
			List += ", Copy_Number = "
			List += str(Copy_Number_KEY)
			List += ", Copy_Books_ISBN = '"
			List += Copy_Books_ISBN_KEY
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
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()



def update_Category(Name ='', Parent_category = '', Name_KEY = '', condition = ''):
	coma_counter = [0]*2
	attribute_list = ["Name = '", "Parent_category = '"]
	i = 0


	if Name != '':
		coma_counter[0] +=1
	if Parent_category != '':
		coma_counter[1] +=1

	j = sum(coma_counter)
	List = ["UPDATE Category SET "]


	if Name != '' and j!=1:
		List += attribute_list[0]
		List += Name
		List += "',"
		j = j-1
	elif Name != '' and j==1:
		List += attribute_list[0]
		List += Name
		List += "'"

	if Parent_category != '' and j!=1:
		List += attribute_list[1]
		List += Parent_category
		List += "',"
		j = j-1
	elif Parent_category != '' and j==1:
		List += attribute_list[1]
		List += Parent_category
		List += "'"



	if  Name_KEY != '' or  condition!='':
		List += " Where "
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
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()


def update_Reminds(Staff_StaffID = 0, Members_MemberID = 0, Date_of_Reminder = '', Staff_StaffID_KEY = 0, Members_MemberID_KEY = 0, condition = ''):
	coma_counter = [0]*3
	attribute_list = ["Staff_StaffID = ", "Members_MemberID = ", "Date_of_Reminder = '"]
	i = 0
	if Staff_StaffID == '0':
		Staff_StaffID = 0
	if Members_MemberID == '0':
		Members_MemberID = 0


	if Staff_StaffID != 0:
		coma_counter[0] +=1
	if Members_MemberID != 0:
		coma_counter[1] +=1
	if Date_of_Reminder != '':
		coma_counter[2] +=1

	j = sum(coma_counter)
	List = ["UPDATE Reminds SET "]


	if Staff_StaffID != 0 and j!=1:
		List += attribute_list[0]
		List += str(Staff_StaffID)
		List += ","
		j = j-1
	elif Staff_StaffID != 0 and j==1:
		List += attribute_list[0]
		List += str(Staff_StaffID)
		List += ""


	if Members_MemberID != 0 and j!=1:
		List += attribute_list[1]
		List += str(Members_MemberID)
		List += ","
		j = j-1
	elif Members_MemberID != 0 and j==1:
		List += attribute_list[1]
		List += str(Members_MemberID)
		List += ""


	if Date_of_Reminder != '' and j!=1:
		List += attribute_list[2]
		List += Date_of_Reminder
		List += "',"
		j = j-1
	elif Date_of_Reminder != '' and j==1:
		List += attribute_list[2]
		List += Date_of_Reminder
		List += "'"

	if  (Staff_StaffID_KEY != 0 and Members_MemberID_KEY!=0) or  condition!='':
		List += " Where "
		if (Staff_StaffID_KEY != 0 and Members_MemberID_KEY!=0):
			List += "Staff_StaffID = "
			List += str(Staff_StaffID_KEY)
			List += ", Members_MemberID = "
			List += str(Members_MemberID_KEY)
			List += ""
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
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()


def main():

	update_Reminds(Staff_StaffID = 12, Members_MemberID = 3, Date_of_Reminder = '', Staff_StaffID_KEY = 1, Members_MemberID_KEY = 21, condition = '')
	# update_Borrows(Members_MemberID = 3, Copy_Number = 7, Copy_Books_ISBN = '101-1312-1148', Start_Date = '', Return_Date = '', Due_Date = '', Members_MemberID_KEY = 3, Copy_Number_KEY = 1, Copy_Books_ISBN_KEY = '101-1312-1148', condition = '')

if __name__ == '__main__':
    main()
