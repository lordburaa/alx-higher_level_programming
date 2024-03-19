-- lists all shows contained in the databse hbtn_0d_tvshows
SELECT s.title, g.genre_id FROM tv_shows s, tv_show_genres g  WHERE s.id=g.show_id ORDER BY s.title, g.genre_id;
