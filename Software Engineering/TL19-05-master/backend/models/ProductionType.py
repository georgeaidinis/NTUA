from sqlalchemy import Column, String, Integer, Boolean, Date
from sqlalchemy.orm import relationship
from base import Base


class ProductionType(Base):
    __tablename__ = 'ProductionType'

    id = Column(Integer, primary_key=True, nullable=False)
    EntityCreatedAt = Column(Date, nullable=False)
    EntityModifiedAt = Column(Date, nullable=False)
    ProductionTypeText = Column(String, unique=True)
    ProductionTypeNote = Column(String)

    def __init__(self, EntityCreatedAt, EntityModifiedAt, ProductionTypeText ,ProductionTypeNote):
        self.id = id
        self.EntityCreatedAt = EntityCreatedAt
        self.EntityModifiedAt = EntityModifiedAt
        self.ProductionTypeText = ProductionTypeText
        self.ProductionTypeNote = ProductionTypeNote