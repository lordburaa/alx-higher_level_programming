-- lists all shows contained in hbtn_od_tvshows that have at least one genr likned

SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id FROM tv_shows, tv_show_genres WHERE tv_show_genres.show_id=tv_shows.id ORDER BY tv_shows.title, tv_show_genres.genre_id;
