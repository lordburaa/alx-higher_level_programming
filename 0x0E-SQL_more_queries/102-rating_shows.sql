-- list all shows from hbtn_0d_tvshow_rate
SELECT s.title, sum(r.rate) AS 'rating'
FROM tv_shows s 
JOIN tv_show_genres sg ON s.id=sg.show_id
JOIN tv_show_ratings r on r.show_id=sg.show_id
JOIN tv_genres g ON sg.genre_id=g.id
GROUP BY s.title
ORDER BY rating DESC;
