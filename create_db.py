import sqlite3
import pathlib

# Define the database file path
db_file = pathlib.Path("project.sqlite3")

def create_database():
    """Create an SQLite database file if it does not exist."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print(f"Database '{db_file}' created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def main():
    create_database()

if __name__ == "__main__":
    main()
