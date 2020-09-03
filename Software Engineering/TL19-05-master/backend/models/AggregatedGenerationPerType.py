from sqlalchemy import Column, String, Integer, Boolean, Date, Float
from sqlalchemy.orm import relationship
from base import Base

class AggregatedGenerationPerType(Base):
    __tablename__ = "AggregatedGenerationPerType"


    Id = Column(Integer, primary_key= True, nullable=False)
    EntityCreatedAt = Column(Date, nullable=False)
    EntityModifiedAt = Column(Date, nullable=False)
    ActionTaskID = Column(Integer, nullable=False)
    Status = Column(String)
    Year = Column(Integer, nullable=False)
    Month = Column(Integer, nullable=False)
    Day = Column(Integer, nullable=False)
    DateTime = Column(Date, nullable=False)
    AreaName = Column(String)
    UpdateTime = Column(Date, nullable=False)
    ActualGenerationOutput = Column(Float, nullable=False)
    ActualConsuption = Column(Float, nullable=False)
    ProductionTypeId = Column(Integer)   
    AreaTypeCodeId = Column(Integer)
    AreaCodeId = Column(Integer, nullable=False)
    ResolutionCodeId = Column(Integer)
    MapCodeId = Column(Integer)
    RowHash = Column(String)

    def __init__(self, Id, EntityCreatedAt, EntityModifiedAt, ActionTaskID, Status, Year, Month, Day, DateTime, AreaName, UpdateTime, ActualGenerationOutput, AreaTypeCodeId, AreaCodeId, ResolutionCodeId, MapCodeId, RowHash):
        self.id = id
        self.EntityCreatedAt = EntityCreatedAt
        self.EntityModifiedAt = EntityModifiedAt
        self.ActionTaskID = ActionTaskID
        self.Status = Status
        self.Year = Year
        self.Month = Month
        self.Day = Day
        self.DateTime = DateTime
        self.AreaName = AreaName
        self.UpdateTime = UpdateTime
        self.ActualGenerationOutput = ActualGenerationOutput
        self.AreaTypeCodeId = AreaTypeCodeId
        self.AreaCodeId = AreaCodeId
        self.ResolutionCodeId = ResolutionCodeId
        self.MapCodeId = MapCodeId
        self.RowHash = RowHash
 