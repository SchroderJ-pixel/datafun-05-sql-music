import sqlite3

# Define database file
db_path = "C:/Projects/datafun-05/datafun-05-sql/database.db"

# Read SQL file and execute it
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    with open("C:/Projects/datafun-05/datafun-05-sql/sql_create/01_drop_tables.sql", "r") as f:
        sql_script = f.read()
    cursor.executescript(sql_script)
    print("Tables dropped and recreated successfully!")
