from sqlalchemy import Column, String, Integer, Boolean, Date
from sqlalchemy.orm import relationship
from base import Base


class ResolutionCode(Base):
    __tablename__ = 'ResolutionCode'

    id = Column(Integer, primary_key=True, nullable=False)
    EntityCreatedAt = Column(Date, nullable=False)
    EntityModifiedAt = Column(Date, nullable=False)
    ResolutionCodeText = Column(String)
    ResolutionCodeNote = Column(String)

    def __init__(self, EntityCreatedAt, EntityModifiedAt, ResolutionCodeText ,ResolutionCodeNote):
        self.id = id
        self.EntityCreatedAt = EntityCreatedAt
        self.EntityModifiedAt = EntityModifiedAt
        self.ResolutionCodeText = ResolutionCodeText
        self.ResolutionCodeNote = ResolutionCodeNote