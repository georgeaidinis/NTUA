#!/bin/bash
mysql < ./database_delete.sql
mysql < ./database_create.sql
python3 mysql_insert.py
mysql < authored_create.sql
mysql < triggers.sql
