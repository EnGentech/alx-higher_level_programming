-- selection from two tables with foreign key

SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states
WHERE name = 'California') ORDER BY id ASC
;
