-- list Number of shows by genre
SELECT g.name AS 'genre', COUNT(g.name) AS 'number_of_shows' FROM tv_genres g INNER JOIN tv_show_genres sg ON sg.genre_id=g.id GROUP BY g.name ORDER BY 'number_of_shows' DESC
