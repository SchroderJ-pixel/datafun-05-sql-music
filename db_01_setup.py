import sqlite3
import pathlib
import pandas as pd
from utils_logger import logger  # Import the logger

def execute_sql_file(connection, file_path: pathlib.Path) -> None:
    """
    Executes a SQL file using the provided SQLite connection.

    Args:
        connection (sqlite3.Connection): SQLite connection object.
        file_path (pathlib.Path): Path to the SQL file to be executed.
    """
    # Check if the SQL file exists before proceeding
    if not file_path.is_file():
        logger.error(f"SQL file does not exist: {file_path}")
        raise FileNotFoundError(f"SQL file not found: {file_path}")
    
    try:
        with open(file_path, 'r') as file:
            # Read the SQL file into a string
            sql_script: str = file.read()
        with connection:
            # Execute the SQL script using the connection
            connection.executescript(sql_script)
        logger.info(f"Executed: {file_path}")
    except Exception as e:
        logger.error(f"Failed to execute {file_path}: {e}")
        raise

def insert_data_from_csv(db_path: pathlib.Path, artists_csv: pathlib.Path, songs_csv: pathlib.Path) -> None:
    """
    Reads CSV files using pandas and inserts data into the database.
    This replaces any existing data in the 'artists' and 'songs' tables.
    """
    try:
        # Read CSV files using pandas
        artists_df = pd.read_csv(artists_csv)
        songs_df = pd.read_csv(songs_csv)
        # Write data to the database, replacing any existing data
        with sqlite3.connect(db_path) as conn:
            artists_df.to_sql("artists", conn, if_exists="replace", index=False)
            songs_df.to_sql("songs", conn, if_exists="replace", index=False)
        logger.info("CSV data inserted successfully.")
    except Exception as e:
        logger.error(f"Error inserting CSV data: {e}")
        raise

def main() -> None:
    # Log the start of the database setup
    logger.info("Starting database setup...")
    
    # Define path variables
    ROOT_DIR = pathlib.Path(__file__).parent.resolve()
    SQL_CREATE_FOLDER = ROOT_DIR.joinpath("sql_create")
    DATA_FOLDER = ROOT_DIR.joinpath("data-05-sql-music")  # Set to your original data folder
    DB_PATH = DATA_FOLDER.joinpath('music_project.db')  # Path to your music database in the original folder
    
    # Define CSV file paths (ensure these CSVs have the correct headers)
    ARTISTS_CSV = ROOT_DIR.joinpath("data-05-sql-music", "artists.csv")  # Path to artists CSV
    SONGS_CSV = ROOT_DIR.joinpath("data-05-sql-music", "songs.csv")      # Path to songs CSV
    
    # Ensure the data folder exists
    DATA_FOLDER.mkdir(exist_ok=True)
    
    try:
        # Connect to SQLite database (it will be created if it doesn't exist)
        connection = sqlite3.connect(DB_PATH)
        logger.info(f"Connected to database: {DB_PATH}")
        
        # Execute SQL files to set up the database schema
        execute_sql_file(connection, SQL_CREATE_FOLDER.joinpath('01_drop_tables.sql'))
        execute_sql_file(connection, SQL_CREATE_FOLDER.joinpath('02_create_tables.sql'))
        # If you have a SQL script that inserts test data, comment it out if you want to use CSV data.
        # execute_sql_file(connection, SQL_CREATE_FOLDER.joinpath('03_insert_tables.sql'))
        
        connection.close()  # Close connection before CSV import
        
        # Insert data from CSV files to populate the database with your CSV headers
        insert_data_from_csv(DB_PATH, ARTISTS_CSV, SONGS_CSV)
        
        logger.info("Database setup and CSV data import completed successfully.")
    except Exception as e:
        logger.error(f"Error during database setup: {e}")
    finally:
        try:
            connection.close()
        except Exception:
            pass
        logger.info("Database connection closed.")

if __name__ == '__main__':
    main()

