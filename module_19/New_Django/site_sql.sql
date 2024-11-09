CREATE TABLE IF NOT EXISTS New_table(
    id INTEGER PRIMARY KEY,
    Author
    TEXT,
    Title
    TEXT,
    Price INTEGER);



INSERT INTO New_table(Author, Title, Price)
VALUES('Bulgakov', 'Lolita', 153),
('Dostoevskiy', 'Idiot', 185);

SELECT *
FROM
New_table;