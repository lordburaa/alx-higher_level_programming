-- list all genres not linked to the show 
SELECT g.name FROM tv_genres g LEFT JOIN tv_show_genres sg ON sg.genre_id=g.id
WHERE g.name NOT IN (SELECT DISTINCT t.name FROM tv_genres t JOIN tv_show_genres sg  ON sg.genre_id=t.id
	JOIN tv_shows s ON s.id=sg.show_id  WHERE s.title='Dexter' GROUP BY t.name) 
GROUP BY g.name ORDER BY g.name;
