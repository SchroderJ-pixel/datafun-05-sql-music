def insert_data_from_csv(db_path, artists_data_path, song_data_path):
    """Read data from CSV files and insert the records into their respective tables."""
    try:
        artists_df = pd.read_csv(artists_data_path)
        songs_df = pd.read_csv(song_data_path)
        print("Artists Data Preview:\n", artists_df.head())  # Print first few rows
        print("Songs Data Preview:\n", songs_df.head())  # Print first few rows
        with sqlite3.connect(db_path) as conn:
            artists_df.to_sql("artists", conn, if_exists="replace", index=False)
            songs_df.to_sql("songs", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"Error inserting data: {e}")
