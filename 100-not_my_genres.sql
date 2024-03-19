-- list all genres not linked to the show 
SELECT DISTINCT g.name FROM tv_genres g JOIN tv_show_genres sg ON sg.genre_id=g.id
WHERE g.name NOT IN (SELECT t.name FROM tv_genres t JOIN tv_show_genres sg  ON sg.genre_id=t.id
	JOIN tv_shows s ON s.id=sg.show_id  WHERE s.title='Dexter') 
ORDER BY g.name;
