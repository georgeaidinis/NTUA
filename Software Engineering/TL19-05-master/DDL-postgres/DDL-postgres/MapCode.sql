CREATE TABLE MapCode (
  Id               SERIAL NOT NULL, 
  EntityCreatedAt  timestamp(34) with time zone NOT NULL, 
  EntityModifiedAt timestamp(34) with time zone NOT NULL, 
  MapCodeText      varchar(255), 
  MapCodeNote      varchar(255), 
  CONSTRAINT PK_MapCode 
    PRIMARY KEY (Id));
CREATE UNIQUE INDEX IX_MapCode_MapCodeText 
  ON MapCode (MapCodeText) WHERE ([MapCodeText] IS NOT NULL);

