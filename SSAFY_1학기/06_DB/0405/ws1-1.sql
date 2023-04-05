CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

SELECT first_name, age, balance FROM users ORDER BY age, balance DESC;

SELECT first_name, age FROM users ORDER BY first_name, age DESC;

SELECT first_name, country FROM users WHERE first_name="건우" and country="경기도";

SELECT 
    first_name, country, age 
FROM 
    users 
WHERE 
    country <> "경기도" and country <> "강원도" and 
    age BETWEEN 20 and 30
ORDER BY
    age;

SELECT 
    first_name, phone, country 
FROM
    users
WHERE
    phone like '%-51__-%'
    AND
    country <> '서울';

SELECT 
    * 
FROM 
    users
ORDER BY
    age
LIMIT 20 OFFSET 60;

CREATE TABLE contacts (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
);

SELECT
    first_name, age, balance
FROM
    users
ORDER BY
    age, balance DESC;