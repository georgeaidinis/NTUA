CREATE TABLE DayAheadTotalLoadForecast (
  Id               SERIAL NOT NULL, 
  EntityCreatedAt  timestamp(34) with time zone NOT NULL, 
  EntityModifiedAt timestamp(34) with time zone NOT NULL, 
  ActionTaskID     int8 NOT NULL, 
  Status           varchar(2), 
  Year             int4 NOT NULL, 
  Month            int4 NOT NULL, 
  Day              int4 NOT NULL, 
  DateTime         timestamp(7) NOT NULL, 
  AreaName         varchar(200), 
  UpdateTime       timestamp(7) NOT NULL, 
  TotalLoadValue   numeric(24, 2) NOT NULL, 
  AreaTypeCodeId   int4, 
  MapCodeId        int4, 
  AreaCodeId       int4 NOT NULL, 
  ResolutionCodeId int4, 
  RowHash          varchar(255), 
  CONSTRAINT PK_DayAheadTotalLoadForecast 
    PRIMARY KEY (Id));
CREATE INDEX IX_DayAheadTotalLoadForecast_MapCodeId 
  ON DayAheadTotalLoadForecast (MapCodeId);
CREATE INDEX IX_DayAheadTotalLoadForecast_AreaTypeCodeId 
  ON DayAheadTotalLoadForecast (AreaTypeCodeId);
CREATE INDEX IX_DayAheadTotalLoadForecast_AreaCodeId 
  ON DayAheadTotalLoadForecast (AreaCodeId);
CREATE INDEX IX_DayAheadTotalLoadForecast_ResolutionCodeId 
  ON DayAheadTotalLoadForecast (ResolutionCodeId);
ALTER TABLE DayAheadTotalLoadForecast ADD CONSTRAINT FKDayAheadTo524780 FOREIGN KEY (AreaCodeId) REFERENCES eic.AllocatedEICDetail (Id);
ALTER TABLE DayAheadTotalLoadForecast ADD CONSTRAINT FK_DayAheadTotalLoadForecast_AreaTypeCode_AreaTypeCodeId FOREIGN KEY (AreaTypeCodeId) REFERENCES AreaTypeCode (Id) ON UPDATE No action ON DELETE No action;
ALTER TABLE DayAheadTotalLoadForecast ADD CONSTRAINT FK_DayAheadTotalLoadForecast_MapCode_MapCodeId FOREIGN KEY (MapCodeId) REFERENCES MapCode (Id) ON UPDATE No action ON DELETE No action;
ALTER TABLE DayAheadTotalLoadForecast ADD CONSTRAINT FK_DayAheadTotalLoadForecast_ResolutionCode_ResolutionCodeId FOREIGN KEY (ResolutionCodeId) REFERENCES ResolutionCode (Id) ON UPDATE No action ON DELETE No action;

