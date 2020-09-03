import os

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
host = 'localhost'
# change YOUR_PASSWORD to your real password
SQLALCHEMY_DATABASE_URI = 'mysql://root:YOUR_PASSWORD@'+host+'/mysql'
SQL_CHOOSE_DB = 'use ElectroMarket'
SECRET_KEY = '@48HourProjectS3Cr3Tk3Y#'