import pandas as pd

try:
    authors_df = pd.read_csv("C:/Projects/datafun-05/datafun-05-sql/data/authors.csv")
    print(authors_df.head())
except Exception as e:
    print(f"Error reading authors.csv: {e}")
    
try:
    books_df = pd.read_csv("C:/Projects/datafun-05/datafun-05-sql/data/books.csv")
    print(books_df.head())
except Exception as e:
    print(f"Error reading books.csv: {e}")

