import sqlite3
import pathlib
import pandas as pd

# Define paths using joinpath
db_file_path = pathlib.Path("music_project.db")
sql_create_file_path = pathlib.Path("sql_create").joinpath("02_create_tables.sql")  # Corrected path
sql_insert_file_path = pathlib.Path("sql_create").joinpath("03_insert_records.sql")  # Path to the insert script
artists_data_path = pathlib.Path("data-music").joinpath("artists.csv")  # Updated path
song_data_path = pathlib.Path("data-music").joinpath("songs.csv")  # Updated path


def verify_and_create_folders(paths):
    """Verify and create folders if they don't exist."""
    for path in paths:
        folder = path.parent
        if not folder.exists():
            print(f"Creating folder: {folder}")
            folder.mkdir(parents=True, exist_ok=True)
        else:
            print(f"Folder already exists: {folder}")


def create_database(db_path):
    """Create a new SQLite database file if it doesn't exist."""
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating the database: {e}")


def create_tables(db_path, sql_file_path):
    """Read and execute SQL statements to create tables."""
    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_file_path, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")


def insert_data_from_sql(db_path, sql_insert_file_path):
    """Execute SQL insert statements from a file."""
    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_insert_file_path, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Records inserted from SQL script.")
    except sqlite3.Error as e:
        print(f"Error inserting records from SQL file: {e}")


def insert_data_from_csv(db_path, artists_data_path, song_data_path):
    """Read data from CSV files and insert the records into their respective tables."""
    try:
        artists_df = pd.read_csv(artists_data_path)
        songs_df = pd.read_csv(song_data_path)

        # Insert new data into the tables with foreign key handling
        with sqlite3.connect(db_path) as conn:
            conn.execute("PRAGMA foreign_keys = OFF;")  # Disable foreign keys
            artists_df.to_sql("artists", conn, if_exists="replace", index=False)
            songs_df.to_sql("songs", conn, if_exists="replace", index=False)
            conn.execute("PRAGMA foreign_keys = ON;")  # Re-enable foreign keys

            print("Data inserted from CSV successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"Error inserting data from CSV: {e}")


def main():
    paths_to_verify = [sql_create_file_path, sql_insert_file_path, artists_data_path, song_data_path]
    verify_and_create_folders(paths_to_verify)

    create_database(db_file_path)
    
    # Step 1: Create tables using the SQL script
    create_tables(db_file_path, sql_create_file_path)
    
    # Step 2: Insert data from CSV files
    insert_data_from_csv(db_file_path, artists_data_path, song_data_path)
    
    # Step 3: Insert additional records from SQL script
    insert_data_from_sql(db_file_path, sql_insert_file_path)


if __name__ == "__main__":
    main()

