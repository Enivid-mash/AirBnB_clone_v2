-- this script prepares a MySQL server for the project

-- create the database if not exosts
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create a user if not exists
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
-- grant all previlages to the user hbnb_dev on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@localhost;
-- apply changes
FLUSH PRIVILEGES;
-- grant select previlage to the user hbnb_dev on the database performance_schema
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
-- save apply changes
FLUSH PRIVILEGES;
