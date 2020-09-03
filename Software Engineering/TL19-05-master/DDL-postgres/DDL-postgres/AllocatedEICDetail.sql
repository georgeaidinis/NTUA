CREATE TABLE AllocatedEICDetail (
  Id                                    SERIAL NOT NULL, 
  EntityCreatedAt                       timestamp(34) with time zone NOT NULL, 
  EntityModifiedAt                      timestamp(34) with time zone NOT NULL, 
  MRID                                  varchar(250), 
  DocStatusValue                        varchar(250), 
  AttributeInstanceComponent            varchar(250), 
  LongNames                             varchar(250), 
  DisplayNames                          varchar(250), 
  LastRequestDateAndOrTime              timestamp(7), 
  DeactivateRequestDateAndOrTime        timestamp(7), 
  MarketParticipantStreetAddressCountry varchar(250), 
  MarketParticipantACERCode             varchar(250), 
  MarketParticipantVATcode              varchar(250), 
  Description                           varchar(255), 
  EICParentMarketDocumentMRID           varchar(250), 
  ELCResponsibleMarketParticipantMRID   varchar(250), 
  IsDeleted                             bool NOT NULL, 
  CONSTRAINT PK_AllocatedEICDetail 
    PRIMARY KEY (Id));

