-- This script prepares a MySQL server for the project's testing environment
-- Create or ensure the existence of a testing database named: hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user named: hbnb_test with the password 'hbnb_test_pwd' for localhost
-- Only create the user if it doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant SELECT privilege on the performance_schema database to the user hbnb_test
-- Ensure that the user has SELECT privileges only on this specific database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Grant all privileges on the database hbnb_test_db to the user hbnb_test
-- Ensure that the user has privileges only on this specific database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
