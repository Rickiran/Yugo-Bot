import pyodbc

def connect_sql_server(server, database, username, password):
    connection_string = (
        f"DRIVER={{ODBC Driver (13 14 15 16 or 17 You can define) for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )
    connection = pyodbc.connect(connection_string)
    return connection

# Example usage
server = 'Insert a host server like 192.168.0.1'
database = 'fill database name'
username = 'type a username'
password = 'insert your password'

connection = connect_sql_server(server, database, username, password)
cursor = connection.cursor()
cursor.execute("SELECT * FROM @table")
result = cursor.fetchall()

for row in result:
    print(row)
connection.close()