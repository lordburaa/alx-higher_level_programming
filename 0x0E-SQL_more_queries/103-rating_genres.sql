-- list all genres in the databse hbtn_0d_tvshows_rate
SELECT g.name, SUM(sr.rate) AS 'rating'
FROM tv_show_ratings sr
JOIN tv_show_genres sg ON sg.show_id=sr.show_id
JOIN tv_genres g ON g.id=sg.genre_id
GROUP BY g.name
ORDER BY rating DESC;
