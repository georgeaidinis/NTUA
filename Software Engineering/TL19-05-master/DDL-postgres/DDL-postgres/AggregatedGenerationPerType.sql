CREATE TABLE AggregatedGenerationPerType (
  Id                     SERIAL NOT NULL, 
  EntityCreatedAt        timestamp(34) with time zone NOT NULL, 
  EntityModifiedAt       timestamp(34) with time zone NOT NULL, 
  ActionTaskID           int8 NOT NULL, 
  Status                 varchar(2), 
  Year                   int4 NOT NULL, 
  Month                  int4 NOT NULL, 
  Day                    int4 NOT NULL, 
  DateTime               timestamp(7) NOT NULL, 
  AreaName               varchar(200), 
  UpdateTime             timestamp(7) NOT NULL, 
  ActualGenerationOutput numeric(24, 2) NOT NULL, 
  ActualConsuption       numeric(24, 2) NOT NULL, 
  AreaTypeCodeId         int4, 
  ProductionTypeId       int4, 
  ResolutionCodeId       int4, 
  MapCodeId              int4, 
  AreaCodeId             int4 NOT NULL, 
  RowHash                varchar(255), 
  CONSTRAINT "PK_AggregatedGenerationPerType " 
    PRIMARY KEY (Id));
CREATE INDEX "IX_AggregatedGenerationPerType _AreaCodeId" 
  ON AggregatedGenerationPerType (AreaCodeId);
CREATE INDEX "IX_AggregatedGenerationPerType _ResolutionCodeId" 
  ON AggregatedGenerationPerType (ResolutionCodeId);
CREATE INDEX "IX_AggregatedGenerationPerType _ProductionTypeId" 
  ON AggregatedGenerationPerType (ProductionTypeId);
CREATE INDEX "IX_AggregatedGenerationPerType _MapCodeId" 
  ON AggregatedGenerationPerType (MapCodeId);
CREATE INDEX "IX_AggregatedGenerationPerType _AreaTypeCodeId" 
  ON AggregatedGenerationPerType (AreaTypeCodeId);
ALTER TABLE "AggregatedGenerationPerType " ADD CONSTRAINT FKAggregated783487 FOREIGN KEY (AreaCodeId) REFERENCES eic.AllocatedEICDetail (Id);
ALTER TABLE "AggregatedGenerationPerType " ADD CONSTRAINT "FK_AggregatedGenerationPerType _AreaTypeCode_AreaTypeCodeId" FOREIGN KEY (AreaTypeCodeId) REFERENCES AreaTypeCode (Id) ON UPDATE No action ON DELETE No action;
ALTER TABLE "AggregatedGenerationPerType " ADD CONSTRAINT "FK_AggregatedGenerationPerType _MapCode_MapCodeId" FOREIGN KEY (MapCodeId) REFERENCES MapCode (Id) ON UPDATE No action ON DELETE No action;
ALTER TABLE "AggregatedGenerationPerType " ADD CONSTRAINT "FK_AggregatedGenerationPerType _ProductionType_ProductionTypeId" FOREIGN KEY (ProductionTypeId) REFERENCES ProductionType (Id) ON UPDATE No action ON DELETE No action;
ALTER TABLE "AggregatedGenerationPerType " ADD CONSTRAINT "FK_AggregatedGenerationPerType _ResolutionCode_ResolutionCodeId" FOREIGN KEY (ResolutionCodeId) REFERENCES ResolutionCode (Id) ON UPDATE No action ON DELETE No action;

