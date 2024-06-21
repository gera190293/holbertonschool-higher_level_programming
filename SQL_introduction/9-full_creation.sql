-- creates a table second_table in the database
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT IGNORE INTO second_table (id, name, score) VALUES (1, 'Jhon', 10);
INSERT IGNORE INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT IGNORE INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT IGNORE INTO second_table (id, name, score) VALUES (4, 'George', 8);
