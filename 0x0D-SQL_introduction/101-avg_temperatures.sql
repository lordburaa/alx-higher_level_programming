-- displays teh average tempereature(Fahrenheurt( by city ordered by temprature descending)
SELECT `city`, AVG(`value`) AS avg_temp FROM `temperatures` GROUP BY `city` ORDER BY avg_value DESC;
