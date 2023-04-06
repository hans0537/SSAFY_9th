CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

-- user 테이블의 모든 컬럼 조회
SELECT * FROM users;

-- 이름과 나이 컬럼만 조회하기
SELECT first_name, age FROM users;

-- rowid와 이름 컬럼 조회하기
SELECT rowid, first_name FROM users;

-- 이름과 나이를 나이가 어린 순서대로 조회
SELECT first_name, age FROM users ORDER BY age;

-- 이름과 나이를 나이가 많은 순서대로 조회
SELECT first_name, age FROM users ORDER BY age DESC;

-- 이름, 나이 , 잔고를 나이가 작은 순서로, 잔고가 높은 순서대로 조회
SELECT first_name,	age,	balance FROM users
ORDER BY age,	balance DESC;

-- 조회 결과 중복 제거하는 방법 DISTINCT
SELECT DISTINCT country FROM users;


-- 조회 결과 중복 제거하는 방법 DISTINCT
SELECT DISTINCT country FROM users ORDER BY country;

-- 조회컬럼이 2개 이상인 경우
SELECT DISTINCT first_name, country FROM USERS;

SELECT DISTINCT first_name, country
FROM users
ORDER BY country;

-- 특정한 조건을 만족하는 결과
-- WHERE 절 사용 (IF문)
SELECT first_name, age, balance
FROM users
WHERE age >= 30;

-- 조건이 여러개인 경우 or , and 사
SELECT first_name, age, balance
FROM users
WHERE age >= 30 AND balance > 500000;

SELECT first_name, age, balance
FROM users
ORDER BY age
LIMIT 10 OFFSET 10;