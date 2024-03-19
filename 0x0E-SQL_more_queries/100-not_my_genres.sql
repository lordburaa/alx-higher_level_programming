-- list all genres not linked to the show Dexter
SELECT g.name FROM tv_genres g JOIN tv_show_genres sg ON sg.genre_id=g.id JOIN tv_shows s ON s.id=sg.show_id WHERE s.title!='Dexter' GROUP BY g.name ORDER BY g.name;
