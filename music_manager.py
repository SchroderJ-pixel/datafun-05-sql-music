import sqlite3
import pathlib
import pandas as pd

# Define paths using joinpath, updated for your project
db_file_path = pathlib.Path("C:/Projects/datafun-05/datafun-05-sql-music/data-music/music_project.db")  # Corrected DB path
sql_create_file_path = pathlib.Path("C:/Projects/datafun-05/datafun-05-sql-music/sql_create").joinpath("02_create_tables.sql")  # Corrected path
sql_insert_file_path = pathlib.Path("C:/Projects/datafun-05/datafun-05-sql-music/sql_create").joinpath("03_insert_records.sql")  # Path to the insert script
artists_data_path = pathlib.Path("C:/Projects/datafun-05/datafun-05-sql-music/data-music").joinpath("artists.csv")  # Updated path
song_data_path = pathlib.Path("C:/Projects/datafun-05/datafun-05-sql-music/data-music").joinpath("songs.csv")  # Updated path

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

def aggregation_sql(db_path, sql_file_path):
    """Execute SQL aggregation query from a file to calculate the average."""
    try:
        with sqlite3.connect(db_path) as conn:
            # Read and execute SQL aggregation query
            sql_script = "SELECT AVG(TotalPlays) AS avg_total_plays FROM artists;"
            result_df = pd.read_sql_query(sql_script, conn)

            # Display the result
            if not result_df.empty:
                print("Average Total Plays:", result_df.iloc[0, 0])
            else:
                print("No data to aggregate.")
    except sqlite3.Error as e:
        print(f"Error aggregating from SQL file: {e}")

def query_filter_sql(db_path, sql_query_file_path):
    """Execute SQL query from a file with filtering conditions."""
    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_query_file_path, "r") as file:
                sql_script = file.read()
            
            # Execute the query and load the result into a DataFrame
            result_df = pd.read_sql_query(sql_script, conn)
            print("Query executed successfully. Filtered results:")
            print(result_df)
    
    except sqlite3.Error as e:
        print(f"Error executing filter query: {e}")
    except pd.errors.DatabaseError as e:
        print(f"Error executing query: {e}")


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

    # Step 4: Run aggregation to find the average total plays
    aggregation_sql(db_file_path, "C:/Projects/datafun-05/datafun-05-sql-music/sql_queries/query_aggregation.sql")

    # Step 5: Execute filter query
    query_filter_sql(db_file_path, "C:/Projects/datafun-05/datafun-05-sql-music/sql_queries/query_filter.sql")

if __name__ == "__main__":
    main()
