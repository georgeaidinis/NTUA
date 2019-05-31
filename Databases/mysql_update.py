#coding=utf-8

from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config


def update_books (ISBN, Title, Pages, Publication_Year, Publishers_Name, Library_Name, ISBN_KEY):
	query = "UPDATE Books SET Title ='Ta arxidia moy KOUNIOUNTAI' WHERE Pages=1301;"
	#args = (Title)
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
	update_books("960-02-1088-8","Ta arxidia moy KOUNIOUNTAI",1301,1994,"Εκδοτικός Οίκος Φυσικής","NTUA","960-02-1088-8")
 
if __name__ == '__main__':
    main()