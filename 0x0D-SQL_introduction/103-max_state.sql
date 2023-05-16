-- display states with max level of temperature

SELECT state, MAX(value) AS max_temp
FROM temperatures GROUP BY state
ORDER BY state;
