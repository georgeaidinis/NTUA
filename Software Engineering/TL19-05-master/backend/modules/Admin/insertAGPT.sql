
USE `ElectroMarket` ;

USE ElectroMarket;


LOAD DATA LOCAL INFILE 'My_file.csv' INTO TABLE AggregatedGenerationPerType
FIELDS TERMINATED BY ';' 
ENCLOSED BY '' 
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(Id, EntityCreatedAt, EntityModifiedAt, ActionTaskID, Status, Year, Month, Day, DateTime, AreaName, UpdateTime, ActualGenerationOutput, ActualConsuption, AreaTypeCodeId, AreaCodeId, ResolutionCodeId, MapCodeId, ProductionTypeId, RowHash);

