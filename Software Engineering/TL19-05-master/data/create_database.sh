#!/bin/bash

mysql -u root -ppass < database_delete.sql
mysql -u root -ppass < database_create.sql


mysql -u root -ppass ElectroMarket < AllocatedEICDetail.sql
mysql -u root -ppass ElectroMarket < AreaTypeCode.sql
mysql -u root -ppass ElectroMarket < MapCode.sql
mysql -u root -ppass ElectroMarket < ProductionType.sql
mysql -u root -ppass ElectroMarket < ResolutionCode.sql

mysql -u root -ppass ElectroMarket < ActualTotalLoad.sql
mysql -u root -ppass ElectroMarket < AggregatedGenerationPerType.sql
mysql -u root -ppass ElectroMarket < DayAheadTotalLoadForecast.sql
mysql -u root -ppass ElectroMarket < Users.sql


mysql -u root -ppass ElectroMarket < insert_rows.sql
mysql -u root -ppass ElectroMarket < create_users.sql