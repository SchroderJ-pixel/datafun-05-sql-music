import sqlite3
import pandas as pd

# Connect to the existing database
conn = sqlite3.connect('music.db')
cursor = conn.cursor()

# Load the artists and songs data from CSVs
artists_df = pd.read_csv(r'C:\Projects\datafun-05\datafun-05-sql-music\data-music\artists.csv')
songs_df = pd.read_csv(r'C:\Projects\datafun-05\datafun-05-sql-music\data-music\songs.csv')

# Step 1: Create the artists table if it doesn't exist already
cursor.execute('''
CREATE TABLE IF NOT EXISTS artists (
    id INTEGER PRIMARY KEY,
    name TEXT,
    total_plays INTEGER
)
''')

# Step 2: Create the songs table if it doesn't exist already
cursor.execute('''
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY,
    title TEXT,
    artist_id INTEGER,
    total_plays INTEGER,
    FOREIGN KEY(artist_id) REFERENCES artists(id)
)
''')

# Add the 'id' column to the artists DataFrame to simulate the artist ID
artists_df['id'] = range(1, len(artists_df) + 1)

# Step 3: Insert the artists data into the database
for index, row in artists_df.iterrows():
    cursor.execute('''
    INSERT INTO artists (id, name, total_plays)
    VALUES (?, ?, ?)
    ''', (row['id'], row['Name'], row['TotalPlays']))

# Step 4: Create a dictionary mapping artist names to artist IDs
artist_dict = pd.Series(artists_df.id.values, index=artists_df.Name).to_dict()

# Step 5: Add the 'artist_id' column to the songs DataFrame
songs_df['artist_id'] = songs_df['Artist'].map(artist_dict)

# Step 6: Insert the songs data into the database
for index, row in songs_df.iterrows():
    cursor.execute('''
    INSERT INTO songs (title, artist_id, total_plays)
    VALUES (?, ?, ?)
    ''', (row['Title'], row['artist_id'], row['TotalPlays']))

# Commit the changes
conn.commit()

# Step 7: Verify the insertion by querying the database
cursor.execute('''
SELECT songs.title, artists.name, songs.total_plays
FROM songs
JOIN artists ON songs.artist_id = artists.id
''')

# Print the results
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()



