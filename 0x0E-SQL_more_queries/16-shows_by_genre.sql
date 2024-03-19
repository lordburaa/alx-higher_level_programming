-- lists all shows and genres linked to that fron the database hbtn_0d_tvshows

SELECT s.title, g.name FROM tv_shows s LEFT JOIN tv_show_genres sg  ON sg.show_id=s.id LEFT JOIN tv_genres g ON g.id=sg.genre_id  ORDER BY s.title, g.name;
