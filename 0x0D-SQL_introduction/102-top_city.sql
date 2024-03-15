-- Displays the top 3 cities temprature during juls and august
SELECT city AS city, AVG(value) AS avg_temp FROM temperatures WHERE month >= 7 AND  month <= 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
