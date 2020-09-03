CREATE TABLE AllocatedEICDetail (
  Id                                    int(11) NOT NULL AUTO_INCREMENT, 
  EntityCreatedAt                       datetime(6) NOT NULL, 
  EntityModifiedAt                      datetime(6) NOT NULL, 
  MRID                                  varchar(250), 
  DocStatusValue                        varchar(250), 
  AttributeInstanceComponent            varchar(250), 
  LongNames                             varchar(250), 
  DisplayNames                          varchar(250), 
  LastRequestDateAndOrTime              datetime(6) NULL, 
  DeactivateRequestDateAndOrTime        datetime(6) NULL, 
  MarketParticipantStreetAddressCountry varchar(250), 
  MarketParticipantACERCode             varchar(250), 
  MarketParticipantVATcode              varchar(250), 
  Description                           varchar(255), 
  EICParentMarketDocumentMRID           varchar(250), 
  ELCResponsibleMarketParticipantMRID   varchar(250), 
  IsDeleted                             bit(1) NOT NULL, 
  CONSTRAINT PK_AllocatedEICDetail 
    PRIMARY KEY (Id));

