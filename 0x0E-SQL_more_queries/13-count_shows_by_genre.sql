-- Write a script that lists all cities contained in the database hbtn_0d_usa.
SELECT tv_genres.name AS genre, count(tv_show_genres.genre_id) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;
