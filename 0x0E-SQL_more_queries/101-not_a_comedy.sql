-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT DISTINCT s.title 
FROM tv_shows s
LEFT JOIN tv_show_genres sg ON s.id=sg.show_id
WHERE s.title NOT IN ( SELECT DISTINCT ts.title
	FROM tv_genres g
	JOIN tv_show_genres tg ON g.id=tg.genre_id
	JOIN tv_shows ts ON ts.id=tg.show_id
	WHERE g.name = 'Comedy' GROUP BY tg.genre_id)
ORDER BY s.title
;
