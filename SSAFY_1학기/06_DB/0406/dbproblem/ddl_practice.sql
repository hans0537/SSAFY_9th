CREATE TABLE animals (
  animal_name TEXT NOT NULL,
  height INT NOT NULL,
  weight INT NOT NULL,
  age INT
);

ALTER TABLE animals ADD COLUMN meal TEXT;

ALTER TABLE animals RENAME COLUMN animal_name TO name;

ALTER TABLE animals RENAME TO zoo;

DROP TABLE zoo;
-----------------------------------------------------------

CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo 
VALUES
  ('gorilla', 'omnivore', 215, 180, 5),
  ('rabbit', 'herbivore', 3, 150, NULL),
  ('tiger', 'carnivore', 220, 115, 3),
  ('elephant', 'herbivore', 3800, 280, 10),
  ('dog', 'omnivore', 8, 20, 1),
  ('eagle', 'carnivore', 8, 75, NULL),
  ('dolphin', 'carnivore', 210, NULL, 3),
  ('alligator', 'carnivore', 250, 50, NULL),
  ('panda', 'herbivore', 80, 90, 2),
  ('pig', 'omnivore', 70, 45, 5);

SELECT name, height FROM zoo;

UPDATE zoo SET height=15 WHERE name='rabbit';

SELECT * FROM zoo WHERE name='rabbit';

DELETE FROM zoo WHERE eat='omnivore';

SELECT * FROM zoo;
------------------------------------------------------------

CREATE TABLE hotels (
  room_num TEXT NOT NULL,
  check_in TEXT NOT NULL,
  check_out TEXT NOT NULL,
  grade TEXT NOT NULL
);

ALTER TABLE hotels ADD COLUMN price INTEGER NOT NULL DEFAULT 0;

INSERT INTO hotels
VALUES
  ('B203', '2021-12-31', '2022-01-03', 'suite', 900),
  ('1102', '2022-01-04', '2022-01-08', 'suite', 850),
  ('303', '2022-01-01', '2022-01-03', 'deluxe', 500),
  ('807', '2021-01-04', '2022-01-07', 'superior', 300),
  ('B205', '2022-01-04', '2022-01-07', 'deluxe', 550);

UPDATE hotels SET check_in='2022-01-04' WHERE room_num='807';

SELECT * FROM hotels WHERE room_num like 'B%' OR grade='deluxe';

------------------------------------------------------------

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT,
    balance INTEGER NOT NULL
);

INSERT INTO users(first_name, last_name, age, country, phone, balance)
VALUES
  ('미현', '김', 19, '경기도', '011-211-8482', 300),
  ('', '최', 33, '제주특별자치도', '', 300),
  ('미숙', '이', 21, '서울특별시', '010-2122-4958', 480),
  ('남석', '박', 18, '경기도', '011-484-8667', 260),
  ('철수', '박', 22, '경상남도', '016-295-8989', 500),
  ('', '박', 45, '전라북도', '', 320),
  ('민준', '이', 35, '전라남도', '019-965-8833', 350),
  ('', '남', 24, '충청남도', '010-5882-5969', 210),
  ('신', '유', 29, '경상북도', '010-4949-2848', 290),
  ('', '김', 18, '대전광역시', '', 300);

SELECT id, age, balance FROM users WHERE age<25 ORDER BY age DESC, balance ASC;

SELECT first_name, balance FROM users WHERE first_name is not null and balance>400;

UPDATE users SET phone='알 수 없음' WHERE phone='';

SELECT * FROM users;

-------------------------------------------------------------------------
CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);

BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

SELECT COUNT(*)
FROM zoo;