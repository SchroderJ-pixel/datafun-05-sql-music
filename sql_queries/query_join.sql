-- query_join.sql
SELECT songs.title, artists.name
FROM songs
INNER JOIN artists ON songs.artist = artists.name
ORDER BY artists.name;