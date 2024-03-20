-- list all shows from hbtn_0d_tvshow_rate
SELECT s.title, SUM(r.rate) AS 'rating'
FROM  tv_shows s
JOIN tv_show_ratings r ON r.show_id=s.id
GROUP BY s.title
ORDER BY rating DESC;
