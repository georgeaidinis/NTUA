CREATE TABLE AggregatedGenerationPerType (
  Id                     int(11) NOT NULL AUTO_INCREMENT,
  EntityCreatedAt        timestamp(6) NOT NULL,
  EntityModifiedAt       timestamp(6) NOT NULL,
  ActionTaskID           bigint(20) NOT NULL,
  Status                 varchar(2),
  Year                   int(11) NOT NULL,
  Month                  int(11) NOT NULL,
  Day                    int(11) NOT NULL,
  DateTime               datetime(6) NOT NULL,
  AreaName               varchar(200),
  UpdateTime             datetime(6) NOT NULL,
  ActualGenerationOutput decimal(24, 2) NOT NULL,
  ActualConsuption       decimal(24, 2) NOT NULL,
  AreaTypeCodeId         int(11),
  ProductionTypeId       int(11),
  ResolutionCodeId       int(11),
  MapCodeId              int(11),
  AreaCodeId             int(11) NOT NULL,
  RowHash                varchar(255),
  CONSTRAINT `PK_AggregatedGenerationPerType `
    PRIMARY KEY (Id));
CREATE INDEX `IX_AggregatedGenerationPerType _AreaCodeId`
  ON AggregatedGenerationPerType (AreaCodeId);
CREATE INDEX `IX_AggregatedGenerationPerType _ResolutionCodeId`
  ON AggregatedGenerationPerType (ResolutionCodeId);
CREATE INDEX `IX_AggregatedGenerationPerType _ProductionTypeId`
  ON AggregatedGenerationPerType (ProductionTypeId);
CREATE INDEX `IX_AggregatedGenerationPerType _MapCodeId`
  ON AggregatedGenerationPerType (MapCodeId);
CREATE INDEX `IX_AggregatedGenerationPerType _AreaTypeCodeId`
  ON AggregatedGenerationPerType (AreaTypeCodeId);
ALTER TABLE `AggregatedGenerationPerType` ADD CONSTRAINT FKAggregated783487 FOREIGN KEY (AreaCodeId) REFERENCES AllocatedEICDetail (Id);
ALTER TABLE `AggregatedGenerationPerType` ADD CONSTRAINT `FK_AggregatedGenerationPerType _AreaTypeCode_AreaTypeCodeId` FOREIGN KEY (AreaTypeCodeId) REFERENCES AreaTypeCode (Id) ON UPDATE No action ON DELETE No action;
ALTER TABLE `AggregatedGenerationPerType` ADD CONSTRAINT `FK_AggregatedGenerationPerType _MapCode_MapCodeId` FOREIGN KEY (MapCodeId) REFERENCES MapCode (Id) ON UPDATE No action ON DELETE No action;
ALTER TABLE `AggregatedGenerationPerType` ADD CONSTRAINT `FK_AggregatedGenerationPerType _ProductionType_ProductionTypeId` FOREIGN KEY (ProductionTypeId) REFERENCES ProductionType (Id) ON UPDATE No action ON DELETE No action;
ALTER TABLE `AggregatedGenerationPerType` ADD CONSTRAINT `FK_AggregatedGenerationPerType _ResolutionCode_ResolutionCodeId` FOREIGN KEY (ResolutionCodeId) REFERENCES ResolutionCode (Id) ON UPDATE No action ON DELETE No action;
