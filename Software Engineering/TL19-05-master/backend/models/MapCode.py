from sqlalchemy import Column, String, Integer, Boolean, Date
from sqlalchemy.orm import relationship
from base import Base


class MapCode(Base):
    __tablename__ = 'MapCode'

    id = Column(Integer, primary_key=True, nullable=False)
    EntityCreatedAt = Column(Date, nullable=False)
    EntityModifiedAt = Column(Date, nullable=False)
    MapCodeText = Column(String, unique=True)
    MapCodeNote = Column(String)

    def __init__(self, EntityCreatedAt, EntityModifiedAt, MapCodeText ,MapCodeNote):
        self.id = id
        self.EntityCreatedAt = EntityCreatedAt
        self.EntityModifiedAt = EntityModifiedAt
        self.MapCodeText = MapCodeText
        self.MapCodeNote = MapCodeNote