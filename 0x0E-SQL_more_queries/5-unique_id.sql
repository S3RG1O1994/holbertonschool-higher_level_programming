-- The database name will be passed as an argument of the mysql command.
-- If the table id_not_null already exists, your script should not fail.
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
