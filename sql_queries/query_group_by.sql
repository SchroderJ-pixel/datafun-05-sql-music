-- query_group_by.sql
SELECT artist, title
FROM songs
GROUP BY artist
ORDER BY artist;