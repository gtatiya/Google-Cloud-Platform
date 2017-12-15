# Connecting to Cloud SQL

This application connects to Cloud SQL and displays the contents of table "guild" in database "mmorpg," and let's user to insert data in the table "guild".

## Create Data Model in Cloud SQL

CREATE DATABASE mmorpg;
USE mmorpg;
CREATE TABLE guild (id VARCHAR(20) PRIMARY KEY, title VARCHAR(50), created_date DATETIME, min_level INT);

## Set up a TCP port
cloud_sql_proxy -instances=connect-to-the-cloud-sql:us-east4:my-cloud-sql-instance=tcp:3307