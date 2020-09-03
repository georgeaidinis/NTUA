CREATE TABLE DayAheadTotalLoadForecast (
  Id               int(11) NOT NULL AUTO_INCREMENT,
  EntityCreatedAt  timestamp(6) NOT NULL,
  EntityModifiedAt timestamp(6) NOT NULL,
  ActionTaskID     bigint(20) NOT NULL,
  Status           varchar(2),
  Year             int(11) NOT NULL,
  Month            int(11) NOT NULL,
  Day              int(11) NOT NULL,
  DateTime         datetime(6) NOT NULL,
  AreaName         varchar(200),
  UpdateTime       datetime(6) NOT NULL,
  TotalLoadValue   decimal(24, 2) NOT NULL,
  AreaTypeCodeId   int(11),
  AreaCodeId       int(11) NOT NULL,
  ResolutionCodeId int(11),
  MapCodeId        int(11),
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
ALTER TABLE DayAheadTotalLoadForecast ADD CONSTRAINT FKDayAheadTo524780 FOREIGN KEY (AreaCodeId) REFERENCES AllocatedEICDetail (Id);
ALTER TABLE DayAheadTotalLoadForecast ADD CONSTRAINT FK_DayAheadTotalLoadForecast_AreaTypeCode_AreaTypeCodeId FOREIGN KEY (AreaTypeCodeId) REFERENCES AreaTypeCode (Id) ON UPDATE No action ON DELETE No action;
ALTER TABLE DayAheadTotalLoadForecast ADD CONSTRAINT FK_DayAheadTotalLoadForecast_MapCode_MapCodeId FOREIGN KEY (MapCodeId) REFERENCES MapCode (Id) ON UPDATE No action ON DELETE No action;
ALTER TABLE DayAheadTotalLoadForecast ADD CONSTRAINT FK_DayAheadTotalLoadForecast_ResolutionCode_ResolutionCodeId FOREIGN KEY (ResolutionCodeId) REFERENCES ResolutionCode (Id) ON UPDATE No action ON DELETE No action;
