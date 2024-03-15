-- displays teh average tempereature(Fahrenheurt( by city ordered by temprature descending)
SELECT AVG(`value`) AS avg_temp FROM `temperatures` GROUP BY `city` ORDER BY avg_temp DESC;
