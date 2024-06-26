--  lists all records of the table second_table of the database
-- Don’t list rows without a name value
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score
SELECT score, name FROM second_table
WHERE name IS NOt NULL
ORDER BY score DESC;
