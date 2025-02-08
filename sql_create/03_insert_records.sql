-- Insert records into the authors table first
INSERT INTO authors (author_id, name, birth_year, nationality) VALUES
    ('6b693b96-394a-4a1d-a4e2-792a47d7a568', 'J.K. Rowling', 1965, 'British'),
    ('16f3e0a1-24cb-4ed6-a50d-509f63e367f7', 'J.R.R. Tolkien', 1892, 'British'),
    ('8d8107b6-1f24-481c-8a21-7d72b13b59b5', 'J.D. Salinger', 1919, 'American');

-- Insert records into the books table
-- And include foreign key references to the authors table
INSERT INTO books (book_id, title, year_published, author_id) VALUES
    ('ca8e64c3-1e67-47f5-82cc-3e4e30f63b75', 'Harry Potter and the Philosopher''s Stone', 1997, '6b693b96-394a-4a1d-a4e2-792a47d7a568'),
    ('be951205-6cc2-4b3d-96f1-7257b8fc8c0f', 'The Hobbit', 1937, '16f3e0a1-24cb-4ed6-a50d-509f63e367f7'),
    ('dce0f8f2-d3ed-48a9-b8ff-960b6baf1f6f', 'The Lord of the Rings', 1954, '06cf58ab-90f1-448d-8e54-055e4393e75c'),
    ('c2a62a4b-cf5c-4246-9bf7-b2601d542e6d', 'The Catcher in the Rye', 1951, '8d8107b6-1f24-481c-8a21-7d72b13b59b5');
