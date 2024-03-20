-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT DISTINCT s.title 
FROM tv_shows s
right JOIN tv_show_genres sg ON s.id=sg.show_id
WHERE sg.genre_id NOT IN ( SELECT DISTINCT tg.genre_id
	FROM tv_genres g
	RIGHT JOIN tv_show_genres tg ON g.id=tg.genre_id
	WHERE g.name = 'Comedy' GROUP BY tg.genre_id)
ORDER BY s.title
;
