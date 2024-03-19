-- list Number of shows by genre
SELECT g.name, COUNT(g.name) AS number_of_shows FROM tv_genres g JOIN tv_show_genres sg ON sg.genre_id=g.id WHERE sg.genre_id IS NOT NULL GROUP BY g.name ORDER BY number_of_shows DESC
