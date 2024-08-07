import pyhdb
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import sqlite3
def connect_hana(host, port, user, password, database):
    try:
        make_connection_hana = pyhdb.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        return make_connection_hana
    except Exception as e:
        print("Fallo en conectar a la base de datos Hana",e)
        return None


def fetch_customer_details(connection, card_name):
    cursor = connection.cursor()
    query = f"SELECT CardCode, CardName FROM OCRD WHERE CardName like '%{card_name}%'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result

def fetch_item_detail(connection,item_code):
    cursor=connection.cursor()
    query=f"SELECT ItemCode FROM OITM WHERE ItemName like '%{item_code}%'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result

def create_business_part_report(connection, card_name):
    card_details = fetch_customer_details(connection, card_name)
    if card_details:
        c = canvas.Canvas(f"{card_name}_report.pdf", pagesize=letter)
        c.drawString(100, 750, "Business Partner Report")
        c.drawString(100, 735, f"Card Name: {card_details[1]}")
        c.drawString(100, 720, f"Card Code: {card_details[0]}")
        c.save()
        print("Reporte creado exitosamete para el business partner:", card_name)
    else:
        print("No se encontraron detalles:", card_name)

def create_item_report(connection, item_name):
    item_details = fetch_item_detail(connection, item_name)
    if item_details:
        c = canvas.Canvas(f"{item_name}_report.pdf", pagesize=letter)
        c.drawString(100, 750, "Item Report")
        c.drawString(100, 735, f"Item Code: {item_details[0]}")
        c.save()
        print("Reporte creado exitosamente el item:", item_name)
    else:
        print("No se encontraron detalles:", item_name)


"""
connection_hana = connect_hana(host, port, user, password, database)
#we gonna user cursor to
cursor_hana = connection_hana.cursor()
cursor_hana.execute("SELECT * FROM @table")
result_hana= cursor_hana.fetchall()
for row in result_hana:
    print(row)"""
"""
# Using SQLite we got an embedded db
sqlite_connection = sqlite3.connect('local.db')
sqlite_cursor = sqlite_connection.cursor()
sqlite_cursor.execute(CREATE TABLE IF NOT EXISTS local_table (
                            column1 TYPE,
                            column2 TYPE,
                            column3 TYPE
                        ))"""
"""
# Insert data into SQLite
sqlite_cursor.executemany("INSERT INTO local_table VALUES (?, ?, ?)", result_hana)
sqlite_connection.commit()

# Close SQLite connection
sqlite_cursor.close()
sqlite_connection.close()
""""""
for row in result_hana:
    print(row)
connection_hana.close()"""

