-- prints the following description of a table
SHOW COLUMNS FROM first_table
SELECT 
    COLUMN_NAME AS 'Column Name', 
    COLUMN_TYPE AS 'Column Type', 
    IS_NULLABLE AS 'Is Nullable', 
    COLUMN_KEY AS 'Key', 
    COLUMN_DEFAULT AS 'Default', 
    EXTRA AS 'Extra'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'hbtn_0c_0' AND 
    TABLE_NAME = 'first_table';
