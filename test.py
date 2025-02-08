import os

file_path = "C:/Projects/datafun-05/datafun-05-sql/sql_create/01_drop_tables.sql"
print(f"Checking file: {file_path}")
if os.path.exists(file_path):
    print("File found!")
else:
    print("File not found!")
