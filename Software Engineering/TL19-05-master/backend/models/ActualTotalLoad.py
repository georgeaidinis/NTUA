from sqlalchemy import Column, String, Integer, Boolean, Date, Float
from sqlalchemy.orm import relationship
from base import Base

class ActualTotalLoad(Base):
    __tablename__ = "ActualTotalLoad"


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
    TotalLoadValue = Column(Float, nullable=False)
    AreaTypeCodeId = Column(Integer)
    AreaCodeId = Column(Integer, nullable=False)
    ResolutionCodeId = Column(Integer)
    MapCodeId = Column(Integer)
    RowHash = Column(String)

    def __init__(self, Id, EntityCreatedAt, EntityModifiedAt, ActionTaskID, Status, Year, Month, Day, DateTime, AreaName, UpdateTime, TotalLoadValue, AreaTypeCodeId, AreaCodeId, ResolutionCodeId, MapCodeId, RowHash):
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
        self.TotalLoadValue = TotalLoadValue
        self.AreaTypeCodeId = AreaTypeCodeId
        self.AreaCodeId = AreaCodeId
        self.ResolutionCodeId = ResolutionCodeId
        self.MapCodeId = MapCodeId
        self.RowHash = RowHash
 