CREATE TABLE ProductionType (
  Id                 int(11) NOT NULL AUTO_INCREMENT,
  EntityCreatedAt    timestamp(6) NOT NULL,
  EntityModifiedAt   timestamp(6) NOT NULL, 
  ProductionTypeText varchar(255),
  ProductionTypeNote varchar(255),
  CONSTRAINT PK_ProductionType
    PRIMARY KEY (Id));
CREATE UNIQUE INDEX IX_ProductionType_ProductionTypeText
  ON ProductionType (ProductionTypeText);
