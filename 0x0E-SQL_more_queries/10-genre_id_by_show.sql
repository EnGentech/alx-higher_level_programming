-- list shows base on at least 1 genre link

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres WHERE
tv_shows.id = tv_show_genres.show_id
ORDER BY by_shows.title, tv_show_genres.genre_id
ASC;
