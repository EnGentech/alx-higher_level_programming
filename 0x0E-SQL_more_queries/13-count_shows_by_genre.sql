-- multiple commands with count, having
-- group and order
-- writen to list genres with value count

SELECT tv_show_genres.genre AS genre,
COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY tv_show_genres.genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
