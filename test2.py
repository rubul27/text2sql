import sqlite3

# Define the path to your .sql file and the desired .db file
sql_file_path = 'Sample-SQL-File-1000-Rows.sql'
db_file_path = 'output_database.db'

# Read the SQL file
with open(sql_file_path, 'r') as file:
    sql_script = file.read()

# Connect to the SQLite database (it will be created if it does not exist)
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

# Execute the SQL script
cursor.executescript(sql_script)

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"Database created successfully at {db_file_path}")