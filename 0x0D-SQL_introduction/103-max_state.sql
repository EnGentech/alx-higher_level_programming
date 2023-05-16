-- display states with max level of temperature
i
SELECT state, MAX(value) AS max_temp
FROM temperatures GROUP BY state
ORDER BY state;
