CREATE TABLE users (
  first_name TEXT NOT null,
  last_name TEXT NOT null,
  age INTEGER NOT null,
  country TEXT NOT null,
  phone TEXT NOT null,
  balance INTEGER NOT null
);

select * from users;

select first_name, age from users;

select rowid, first_name from users;

select first_name, age from users ORDER BY age ASC, first_name DESC;

SELECT first_name, age, balance FROM users ORDER BY age LIMIT 10 OFFSET 20;
