-- This script prepares a MySQL server for the project
-- Create or ensure the existence of a development database named: hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user named: hbnb_dev with password 'hbnb_dev_pwd' for localhost
-- Only create the user if it doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the database hbnb_dev_db to the user hbnb_dev
-- Ensure that the user has privileges only on this specific database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

-- Grant SELECT privilege on the performance_schema database to the user hbnb_dev
-- Ensure that the user has SELECT privileges only on this specific database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges again to apply the SELECT privilege
FLUSH PRIVILEGES;
