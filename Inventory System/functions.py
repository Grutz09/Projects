import mysql.connector
import sys

    #Connect Database
config = {
        'user': 'root',
        'password': '020805Grutas',
        'host': '127.0.0.1',
        'port': 3306,
        'database': 'employee_acc',
    }


def add_stock(item_name, item_quantity):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    
    insert_query = "INSERT INTO inventory(item_name, item_quantity) VALUES (%s, %s)"
    inventory_data = (item_name, item_quantity)
    cursor.execute(insert_query, inventory_data)
    cnx.commit()
    
    return {f"{item_name} has been added."}
    
def remove_stock(item_name, item_quantity):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    
    update_query = "UPDATE inventory SET item_quantity = item_quantity - %s WHERE item_name = %s"
    data = (item_quantity, item_name)
    cursor.execute(update_query, data)
    cursor.execute("DELETE FROM inventory WHERE item_quantity <= 0")
    cnx.commit()
    
    return {f"{item_quantity} unit/s of {item_name} has been removed from inventory."}
    
def get_all_stock():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    for row in rows:
        print (f"ID: {row[0]}, Item: {row[1]}, Quantity: {row[2]}")

get_all_stock()