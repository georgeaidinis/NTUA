CREATE TABLE AreaTypeCode (
  Id               SERIAL NOT NULL, 
  EntityCreatedAt  timestamp(34) with time zone NOT NULL, 
  EntityModifiedAt timestamp(34) with time zone NOT NULL, 
  AreaTypeCodeText varchar(255), 
  AreaTypeCodeNote varchar(255), 
  CONSTRAINT PK_AreaTypeCode 
    PRIMARY KEY (Id));
CREATE UNIQUE INDEX IX_AreaTypeCode_AreaTypeCodeText 
  ON AreaTypeCode (AreaTypeCodeText) WHERE ([AreaTypeCodeText] IS NOT NULL);

