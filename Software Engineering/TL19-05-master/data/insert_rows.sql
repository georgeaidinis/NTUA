-- LOAD DATA LOCAL INFILE 'AllocatedEICDetail.csv' INTO TABLE MapCode
-- FIELDS TERMINATED BY ';' 
-- ENCLOSED BY '' 
-- LINES TERMINATED BY '\r\n'
-- IGNORE 1 LINES
-- (Id, EntityCreatedAt, EntityModifiedAt, MRID, DocStatusValue, AttributeInstanceComponent, LongNames, DisplayNames, LastRequestDateAndOrTime, DeactivateRequestDateAndOrTime, MarketParticipantStreetAddressCountry, MarketParticipantACERCode, MarketParticipantVATcode, Description, EICParentMarketDocumentMRID, ELCResponsibleMarketParticipantMRID, IsDeleted, AllocatedEICID);

LOAD DATA LOCAL INFILE 'AreaTypeCode.csv' INTO TABLE AreaTypeCode
FIELDS TERMINATED BY ';' 
ENCLOSED BY '' 
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(Id, EntityCreatedAt, EntityModifiedAt, AreaTypeCodeText, AreaTypeCodeNote);

LOAD DATA LOCAL INFILE 'MapCode.csv' INTO TABLE MapCode
FIELDS TERMINATED BY ';' 
ENCLOSED BY '' 
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(Id ,EntityCreatedAt ,EntityModifiedAt ,MapCodeText ,MapCodeNote);


LOAD DATA LOCAL INFILE 'ProductionType.csv' INTO TABLE ProductionType
FIELDS TERMINATED BY ';' 
ENCLOSED BY '' 
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(Id, EntityCreatedAt, EntityModifiedAt, ProductionTypeText, ProductionTypeNote);


LOAD DATA LOCAL INFILE 'ResolutionCode.csv' INTO TABLE ResolutionCode
FIELDS TERMINATED BY ';' 
ENCLOSED BY '' 
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(Id, EntityCreatedAt, EntityModifiedAt, ResolutionCodeText, ResolutionCodeNote);

-- LOAD DATA LOCAL INFILE 'ActualTotalLoad-10days.csv' INTO TABLE ActualTotalLoad
-- FIELDS TERMINATED BY ';' 
-- ENCLOSED BY '' 
-- LINES TERMINATED BY '\r\n'
-- IGNORE 1 LINES
-- (Id, EntityCreatedAt, EntityModifiedAt, ActionTaskID, Status, Year, Month, Day, DateTime, AreaName, UpdateTime, TotalLoadValue, AreaTypeCodeId, AreaCodeId, ResolutionCodeId, MapCodeId, RowHash);

-- LOAD DATA LOCAL INFILE 'AggregatedGenerationPerType-10days.csv' INTO TABLE AggregatedGenerationPerType
-- FIELDS TERMINATED BY ';' 
-- ENCLOSED BY '' 
-- LINES TERMINATED BY '\r\n'
-- IGNORE 1 LINES
-- (Id, EntityCreatedAt, EntityModifiedAt, ActionTaskID, Status, Year, Month, Day, DateTime, AreaName, UpdateTime, ActualGenerationOutput, ActualConsuption, AreaTypeCodeId, AreaCodeId, ResolutionCodeId, MapCodeId, ProductionTypeId, RowHash);

LOAD DATA LOCAL INFILE 'DayAheadTotalLoadForecast-10days.csv' INTO TABLE DayAheadTotalLoadForecast
FIELDS TERMINATED BY ';' 
ENCLOSED BY '' 
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(Id, EntityCreatedAt, EntityModifiedAt, ActionTaskID, Status, Year, Month, Day, DateTime, AreaName, UpdateTime, TotalLoadValue, AreaTypeCodeId, AreaCodeId, ResolutionCodeId, MapCodeId, RowHash);
