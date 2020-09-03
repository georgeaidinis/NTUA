CREATE TABLE ActualTotalLoad (
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
  CONSTRAINT "PK_ActualTotalLoad " 
    PRIMARY KEY (Id));
CREATE INDEX "IX_ActualTotalLoad _ResolutionCodeId" 
  ON ActualTotalLoad (ResolutionCodeId);
CREATE INDEX "IX_ActualTotalLoad _AreaCodeId" 
  ON ActualTotalLoad (AreaCodeId);
CREATE INDEX "IX_ActualTotalLoad _AreaTypeCodeId" 
  ON ActualTotalLoad (AreaTypeCodeId);
CREATE INDEX "IX_ActualTotalLoad _MapCodeId" 
  ON ActualTotalLoad (MapCodeId);
ALTER TABLE "ActualTotalLoad " ADD CONSTRAINT FKActualTota167504 FOREIGN KEY (AreaCodeId) REFERENCES eic.AllocatedEICDetail (Id);
ALTER TABLE "ActualTotalLoad " ADD CONSTRAINT "FK_ActualTotalLoad _AreaTypeCode_AreaTypeCodeId" FOREIGN KEY (AreaTypeCodeId) REFERENCES AreaTypeCode (Id) ON UPDATE No action ON DELETE No action;
ALTER TABLE "ActualTotalLoad " ADD CONSTRAINT "FK_ActualTotalLoad _MapCode_MapCodeId" FOREIGN KEY (MapCodeId) REFERENCES MapCode (Id) ON UPDATE No action ON DELETE No action;
ALTER TABLE "ActualTotalLoad " ADD CONSTRAINT "FK_ActualTotalLoad _ResolutionCode_ResolutionCodeId" FOREIGN KEY (ResolutionCodeId) REFERENCES ResolutionCode (Id) ON UPDATE No action ON DELETE No action;

