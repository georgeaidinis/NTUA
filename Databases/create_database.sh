#!/bin/bash
mysql < source database_delete.sql
mysql < source database_create.sql
mysql < source database_create_views.sql
python3 mysql_insert.py
mysql < source authored_create.sql
mysql < source triggers.sql
mysql < source database_insert_rest.sql
