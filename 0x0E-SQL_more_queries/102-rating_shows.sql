-- list all shows from hbtn_0d_tvshow_rate
SELECT s.title, sum(r.rate) AS 'rating'
FROM  tv_shows s
left JOIN tv_show_ratings r on r.show_id=s.id
GROUP BY s.id
ORDER BY rating DESC;
