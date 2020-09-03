CREATE TABLE ResolutionCode (
  Id                 int(11) NOT NULL AUTO_INCREMENT,
  EntityCreatedAt    timestamp(6) NOT NULL,
  EntityModifiedAt   timestamp(6) NOT NULL, 
  ResolutionCodeText varchar(255),
  ResolutionCodeNote varchar(255),
  CONSTRAINT PK_ResolutionCode
    PRIMARY KEY (Id));
CREATE UNIQUE INDEX IX_ResolutionCode_ResolutionCodeText
  ON ResolutionCode (ResolutionCodeText);
