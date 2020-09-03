CREATE TABLE ActualTotalLoad (
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
  CONSTRAINT `PK_ActualTotalLoad `
    PRIMARY KEY (Id));
CREATE INDEX `IX_ActualTotalLoad _ResolutionCodeId`
  ON ActualTotalLoad (ResolutionCodeId);
CREATE INDEX `IX_ActualTotalLoad _AreaCodeId`
  ON ActualTotalLoad (AreaCodeId);
CREATE INDEX `IX_ActualTotalLoad _AreaTypeCodeId`
  ON ActualTotalLoad (AreaTypeCodeId);
CREATE INDEX `IX_ActualTotalLoad _MapCodeId`
  ON ActualTotalLoad (MapCodeId);
ALTER TABLE `ActualTotalLoad` ADD CONSTRAINT FKActualTota167504 FOREIGN KEY (AreaCodeId) REFERENCES AllocatedEICDetail (Id);
ALTER TABLE `ActualTotalLoad` ADD CONSTRAINT `FK_ActualTotalLoad _AreaTypeCode_AreaTypeCodeId` FOREIGN KEY (AreaTypeCodeId) REFERENCES AreaTypeCode (Id) ON UPDATE No action ON DELETE No action;
ALTER TABLE `ActualTotalLoad` ADD CONSTRAINT `FK_ActualTotalLoad _MapCode_MapCodeId` FOREIGN KEY (MapCodeId) REFERENCES MapCode (Id) ON UPDATE No action ON DELETE No action;
ALTER TABLE `ActualTotalLoad` ADD CONSTRAINT `FK_ActualTotalLoad _ResolutionCode_ResolutionCodeId` FOREIGN KEY (ResolutionCodeId) REFERENCES ResolutionCode (Id) ON UPDATE No action ON DELETE No action;
