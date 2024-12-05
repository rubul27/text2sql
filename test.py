import pyodbc
import json

def get_tables_and_columns(server, database, username, password):
    # Define the connection string
    conn_str = (
        f"DRIVER={{'ODBC Driver 17 for SQL Server'}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    )
    
    # Connect to the Azure SQL Database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # Query to get all table names
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';")
    tables = cursor.fetchall()
    
    # Initialize a dictionary to hold table names and their columns
    db_structure = {}
    
    for table_name in tables:
        table_name = table_name[0]
        cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = ?;", (table_name,))
        columns = cursor.fetchall()
        column_names = [column[0] for column in columns]
        db_structure[table_name] = column_names
    
    # Close the database connection
    conn.close()
    
    return db_structure

def main():
    # Replace these variables with your actual database details
    server = 'aimdmdbsql.westindia.azurecontainer.io'
    database = 'SchemaMaster'
    username = 'sa'
    password = 'mexx@2023'
    
    db_structure = get_tables_and_columns(server, database, username, password)
    
    # Convert the dictionary to JSON format
    json_output = json.dumps(db_structure, indent=4)
    
    # Print the JSON output
    print(json_output)

if __name__ == "__main__":
    main()
