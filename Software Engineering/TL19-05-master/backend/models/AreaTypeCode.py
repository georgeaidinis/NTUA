from sqlalchemy import Column, String, Integer, Boolean, Date
from sqlalchemy.orm import relationship
from base import Base


class AreaTypeCode(Base):
    __tablename__ = 'AreaTypeCode'

    id = Column(Integer, primary_key=True, nullable=False)
    EntityCreatedAt = Column(Date, nullable=False)
    EntityModifiedAt = Column(Date, nullable=False)
    AreaTypeCodeText = Column(String)
    AreaTypeCodeNote = Column(String)

    def __init__(self, EntityCreatedAt, EntityModifiedAt, AreaTypeCodeText ,AreaTypeCodeNote):
        self.id = id
        self.EntityCreatedAt = EntityCreatedAt
        self.EntityModifiedAt = EntityModifiedAt
        self.AreaTypeCodeText = AreaTypeCodeText
        self.AreaTypeCodeNote = AreaTypeCodeNote