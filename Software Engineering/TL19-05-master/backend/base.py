# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import *

engine = create_engine(SQLALCHEMY_DATABASE_URI)
engine.execute(SQL_CHOOSE_DB)
Session = sessionmaker(bind=engine)
Base = declarative_base()