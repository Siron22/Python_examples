/*
1. Установить SQLite
2. Создать таблицу Persons(name: string, favorite_color: string, profit: float)
3. Создать таблицу Cars(model: string, color: string, price: float)
4. Заполнить таблицы данными
5. Вывести для каждого человека, который может купить автомобиль, самый дешевый автомобиль его любимого цвета, который он может себе позволить (цена автомобиля должна быть меньше или равна дохода человека). Отсортировать по имени чловека в алфавитном порядке.

Со звездочкой по желанию
6*. Вывести для каждого человека самый дешевый автомобиль его любимого цвета, который он может себе позволить (цена автомобиля должна быть меньше или равна дохода человека). Отсортировать по имени чловека в алфавитном порядке.
Решением должен быть файл с расширением .sql и всеми запросами

Пример данных и результата:
Данные в таблице Persons:
('John', 'red', 1000),
('Anna', 'red', 2000),
('James', 'green', 500),
('Karl', 'black', 2500);

Данные в таблице Cars:
('BMW M1', 'blue', 700),
('BMW M2', 'black', 1700),
('BMW M3', 'black', 2300),
('Fiat M1', 'red', 1500),
('Fiat M2', 'red', 1000),
('Chevrolet M1', 'green', 501);

Результат для 5:
name  model    color  price   profit
----  -------  -----  ------  ------
Anna  Fiat M2  red    1000.0  2000.0
John  Fiat M2  red    1000.0  1000.0
Karl  BMW M2   black  1700.0  2500.0

Результат для 6*
name   model    color  price   profit
-----  -------  -----  ------  ------
Anna   Fiat M2  red    1000.0  2000.0
James           green          500.0
John   Fiat M2  red    1000.0  1000.0
Karl   BMW M2   black  1700.0  2500.0
*/

CREATE TABLE Persons (
	person_id integer PRIMARY KEY,
	name TEXT NOT NULL,
	favorite_color TEXT,
	profit REAL
);

CREATE TABLE Cars (
	car_id integer PRIMARY KEY,
	model TEXT NOT NULL,
	color TEXT,
	price REAL
);

INSERT INTO Persons (name, favorite_color, profit)
VALUES
   ('John', 'red', 1000),
   ('Anna', 'red', 2000),
   ('James', 'green', 500),
   ('Karl', 'black', 2500);

INSERT INTO Cars (model, color, price)
VALUES
   ('BMW M1', 'blue', 700),
   ('BMW M2', 'black', 1700),
   ('BMW M3', 'black', 2300),
   ('Fiat M1', 'red', 1500),
   ('Fiat M2', 'red', 1000),
   ('Chevrolet M1', 'green', 501);

-- solution 5
SELECT
    name, model, color, price, profit
FROM
    Persons
INNER JOIN Cars
    ON Persons.favorite_color=Cars.color
WHERE Persons.profit >= Cars.price AND Cars.price = (SELECT min(price) from Cars WHERE Persons.favorite_color=Cars.color GROUP BY color) ORDER BY name;

-- solution 6
SELECT
    name, model, color, price, profit
FROM
    Persons
INNER JOIN Cars
    ON Persons.favorite_color=Cars.color
WHERE Persons.profit >= Cars.price AND Cars.price = (SELECT min(price) from Cars WHERE Persons.favorite_color=Cars.color GROUP BY color)
UNION
SELECT name, NULL, favorite_color, NULL, profit FROM Persons
WHERE name NOT IN
(SELECT DISTINCT
    name
FROM
    Persons
INNER JOIN Cars
    ON Persons.favorite_color=Cars.color WHERE Persons.profit >= Cars.price);
