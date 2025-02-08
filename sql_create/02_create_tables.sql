import sqlite3
import pathlib

def create_tables(db_file):
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_create", "01_drop_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def main():
    db_file = "C:/Projects/datafun-05/datafun-05-sql/database.db"
    create_tables(db_file)

# Run the main function if this script is called directly
if __name__ == "__main__":
    main()
