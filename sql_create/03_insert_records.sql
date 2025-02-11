-- Insert artists into the artists table
INSERT INTO artists (artist_id, name, total_plays) 
VALUES
('ARTIST_001', 'Chappell Roan', 500),
('ARTIST_002', 'Surfaces', 800),
('ARTIST_003', 'Teddy Swims', 700);

-- Insert songs into the songs table
INSERT INTO songs (song_id, title, artist_id, total_plays)
VALUES
('SONG_001', 'Pink Pony Club', 'ARTIST_001', 150),
('SONG_002', 'HOT TO GO!', 'ARTIST_001', 200),
('SONG_003', 'Good Luck, Babe!', 'ARTIST_001', 250),
('SONG_004', 'Wave of You', 'ARTIST_002', 300),
('SONG_005', 'Sunday Best', 'ARTIST_002', 350),
('SONG_006', 'Guilty', 'ARTIST_003', 120),
('SONG_007', 'The Door', 'ARTIST_003', 180);

-- Query to check the insertion and link the songs to artists
SELECT songs.title, artists.name, songs.total_plays
FROM songs
JOIN artists ON songs.artist_id = artists.artist_id;
