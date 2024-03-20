-- list all genres not linked to the show Dexter
SELECT g.name FROM tv_genres g JOIN tv_show_genres sg ON sg.genre_id=g.id
WHERE g.name NOT IN
( SELECT t.name
	FROM tv_genres t
	JOIN tv_show_genres tg ON tg.genre_id=t.id
	JOIN tv_shows ts ON ts.id=tg.show_id
	WHERE ts.title='Dexter') 
GROUP BY g.name ORDER BY g.name;
