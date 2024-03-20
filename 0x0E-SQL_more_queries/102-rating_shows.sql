-- list all shows from hbtn_0d_tvshow_rate
SELECT s.title, sum(r.rate) AS 'rating'
FROM tv_show_genres sg
right JOIN tv_shows s ON s.id=sg.show_id
left JOIN tv_show_ratings r on r.show_id=s.id
left JOIN tv_genres g ON sg.genre_id=g.id
GROUP BY s.id
ORDER BY rating DESC;
