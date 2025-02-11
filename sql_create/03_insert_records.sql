-- Insert artists into the artists table
INSERT INTO artists (name, total_plays) 
VALUES
('Chappell Roan', 8000),
('Surfaces', 7000),
('Teddy Swims', 700);

-- Insert songs into the songs table
INSERT INTO songs (title, artist_name, total_plays)
VALUES
('Pink Pony Club', 'Chappell Roan', 4000),
('HOT TO GO!', 'Chappell Roan', 3000),
('Good Luck, Babe!', 'Chappell Roan', 1000),
('Wave of You', 'Surfaces', 5000),
('Sunday Best', 'Surfaces', 2000),
('Guilty', 'Teddy Swims', 500),
('The Door', 'Teddy Swims', 20);

-- Query to check the insertion and link the songs to artists
SELECT songs.title, artists.name, songs.total_plays
FROM songs
JOIN artists ON songs.artist_name = artists.name;

