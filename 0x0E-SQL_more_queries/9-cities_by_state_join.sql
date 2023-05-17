-- selection from two tables with foreign key

SELECT id, name FROM cities
WHERE state_id = (SELECT name FROM states)
ORDER BY id ASC;
