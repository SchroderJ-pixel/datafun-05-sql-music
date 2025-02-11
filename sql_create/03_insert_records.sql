-- Insert artists into the artists table
INSERT INTO artists (name, TotalPlays) 
VALUES
('Chappell Roan', 8000),
('Surfaces', 7000),
('Teddy Swims', 700);

-- Insert songs into the songs table
INSERT INTO songs (title, Artist, TotalPlays)
VALUES
('Pink Pony Club', 'Chappell Roan', 4000),
('HOT TO GO!', 'Chappell Roan', 3000),
('Good Luck, Babe!', 'Chappell Roan', 1000),
('Wave of You', 'Surfaces', 5000),
('Sunday Best', 'Surfaces', 2000),
('Guilty', 'Teddy Swims', 500),
('The Door', 'Teddy Swims', 20);

-- Update Queen to Queen (Freddie Mercury)
UPDATE artists
SET name = 'Queen (Freddie Mercury)'
WHERE name = 'Queen';

