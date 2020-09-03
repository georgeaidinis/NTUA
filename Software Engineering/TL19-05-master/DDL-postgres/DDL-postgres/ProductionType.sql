CREATE TABLE ProductionType (
  Id                 SERIAL NOT NULL, 
  EntityCreatedAt    timestamp(34) with time zone NOT NULL, 
  EntityModifiedAt   timestamp(34) with time zone NOT NULL, 
  ProductionTypeText varchar(255), 
  ProductionTypeNote varchar(255), 
  CONSTRAINT PK_ProductionType 
    PRIMARY KEY (Id));
CREATE UNIQUE INDEX IX_ProductionType_ProductionTypeText 
  ON ProductionType (ProductionTypeText) WHERE ([ProductionTypeText] IS NOT NULL);

