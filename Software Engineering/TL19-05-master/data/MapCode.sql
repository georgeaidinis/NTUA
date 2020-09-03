CREATE TABLE MapCode (
  Id               int(11) NOT NULL AUTO_INCREMENT,
  EntityCreatedAt  timestamp(6) NOT NULL,
  EntityModifiedAt timestamp(6) NOT NULL, 
  MapCodeText      varchar(255),
  MapCodeNote      varchar(255),
  CONSTRAINT PK_MapCode
    PRIMARY KEY (Id));
CREATE UNIQUE INDEX IX_MapCode_MapCodeText
  ON MapCode (MapCodeText);
