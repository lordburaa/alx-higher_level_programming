-- displays the max temperature of  each state by state name
SELECT state AS state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
