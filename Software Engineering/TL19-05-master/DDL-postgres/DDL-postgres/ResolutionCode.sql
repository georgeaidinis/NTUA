CREATE TABLE ResolutionCode (
  Id                 SERIAL NOT NULL, 
  EntityCreatedAt    timestamp(34) with time zone NOT NULL, 
  EntityModifiedAt   timestamp(34) with time zone NOT NULL, 
  ResolutionCodeText varchar(255), 
  ResolutionCodeNote varchar(255), 
  CONSTRAINT PK_ResolutionCode 
    PRIMARY KEY (Id));
CREATE UNIQUE INDEX IX_ResolutionCode_ResolutionCodeText 
  ON ResolutionCode (ResolutionCodeText) WHERE ([ResolutionCodeText] IS NOT NULL);

