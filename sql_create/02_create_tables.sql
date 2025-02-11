-- Create the artists table
CREATE TABLE IF NOT EXISTS artists (
    artist_id TEXT PRIMARY KEY,  -- Prefixed sequential ID as the primary key (e.g., ARTIST_001)
    name TEXT NOT NULL,          -- Artist's name (mandatory field)
    total_plays INTEGER         -- Total plays for the artist (optional)
);

-- Create the songs table
CREATE TABLE IF NOT EXISTS songs (
    song_id TEXT PRIMARY KEY,      -- Added primary key for songs
    title TEXT NOT NULL,           -- Song title (mandatory field)
    artist_id TEXT,                -- Foreign key linking to artists (must match the artists table)
    total_plays INTEGER,           -- Total plays for the song (optional)
    FOREIGN KEY (artist_id) REFERENCES artists (artist_id)  -- Relationship with artists
);


