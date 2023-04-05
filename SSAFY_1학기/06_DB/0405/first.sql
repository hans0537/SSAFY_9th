CREATE TABLE table_name (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE

);

ALTER TABLE table_name RENAME TO new_contacts;

ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

ALTER TABLE new_contacts ADD COLUMN addresss TEXT NOT NULL DEFAULT "no address";

ALTER TABLE new_contacts DROP COLUMN address;