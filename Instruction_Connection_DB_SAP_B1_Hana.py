import pyhdb
#If I want an embedded db choose sqlite3 as one
import sqlite3
def connect_hana(host, port, user, password, database):
    make_connection_hana = pyhdb.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    return make_connection_hana

# Steps to consider making a connection to Hana
## Take into consideration that this variables must be called at main class and execute the function
host = '' #Open config file located in C and take a look and fill as value in variable host
port = 30015  # Default HANA port but you can set another one checking out config file
user = 'throw an username'
password = 'throw a password'
database = 'stick a database up'

connection_hana = connect_hana(host, port, user, password, database)
#we gonna user cursor to
cursor_hana = connection_hana.cursor()
cursor_hana.execute("SELECT * FROM @table")
result_hana= cursor_hana.fetchall()
for row in result_hana:
    print(row)

# Using SQLite we got an embedded db
sqlite_connection = sqlite3.connect('local.db')
sqlite_cursor = sqlite_connection.cursor()
sqlite_cursor.execute("""CREATE TABLE IF NOT EXISTS local_table (
                            column1 TYPE,
                            column2 TYPE,
                            column3 TYPE
                        )""")

# Insert data into SQLite
sqlite_cursor.executemany("INSERT INTO local_table VALUES (?, ?, ?)", result_hana)
sqlite_connection.commit()

# Close SQLite connection
sqlite_cursor.close()
sqlite_connection.close()
"""
for row in result_hana:
    print(row)
connection_hana.close()"""

