from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, UniqueConstraint, Date
from sqlalchemy.orm import relationship
from base import Base


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    password = Column(String)
    username = Column(String, unique=True)
    role = Column(Integer, default=0)
    daily_quotas = Column(Integer, default=50)
    current_quotas = Column(Integer, default=50)
    last_login = Column(Date, default ='1998-02-18')
    email = Column(String)

    def __init__(self, id, password, username, role, daily_quotas, email,current_quotas,last_login):
        self.id = id
        self.password = password
        self.username = username
        self.role = role
        self.daily_quotas = daily_quotas
        self.email = email
        self.current_quotas = current_quotas
        self.last_login = last_login
