CREATE TABLE AreaTypeCode (
  Id               int(11) NOT NULL AUTO_INCREMENT,
  EntityCreatedAt  timestamp(6) NOT NULL,
  EntityModifiedAt timestamp(6) NOT NULL, 
  AreaTypeCodeText varchar(255),
  AreaTypeCodeNote varchar(255),
  CONSTRAINT PK_AreaTypeCode
    PRIMARY KEY (Id));
CREATE UNIQUE INDEX IX_AreaTypeCode_AreaTypeCodeText
  ON AreaTypeCode (AreaTypeCodeText);
