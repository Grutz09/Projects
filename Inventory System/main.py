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

def register():
    username = input("Create username: ")
    password = input("Create password: ")
    password1 = input("Confirm password: ")

    if password != password1:
        print("Passwords do not match! Try again.")
        return


    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # cursor.execute("SELECT * FROM employee_acc")
        # rows = cursor.fetchall()
        # print(rows)

        insert_query = "INSERT INTO employee_acc(username, password) VALUES (%s, %s)"
        employee_data = (username, password)
        cursor.execute(insert_query, employee_data)
        cnx.commit()
        print("User registered successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'cnx' in locals() and cnx:
            cnx.close()
            print("Closing connection")

def access():
    username = input("username: ")
    password = input("password: ")

    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        cursor.execute("select * from employee_acc")
        rows = cursor.fetchall()

        count = 0
        remaining = 3
        for row in rows:
            count+=1
            remaining-=1
            if username != row[0] or password != row[1]:
                print(f"User or password incorrect! Try again. {remaining} attempt/s left.")
                username = input("Enter username again: ")
                password = input("Enter password again: ")
            else:
                print(f"Hi {row[0]}. Welcome to INVENTORY System!")
                inventory_sys()
            if count == 3:
                sys.exit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def inventory_sys():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    item_name = input("Item name: ")
    item_quantity = input("Item quantity: ")
    action = input("Action (Add/Remove/Check Stock): ")
    if action == "Add":
        insert_query = "INSERT INTO inventory(item_name, item_quantity) VALUES (%s, %s)"
        inventory_data = (item_name, item_quantity)
        cursor.execute(insert_query, inventory_data)
        cnx.commit()
        print(f"{item_name} has been added.")

    elif action == "Remove":
            update_query = "UPDATE inventory SET item_quantity = item_quantity - %s WHERE item_name = %s"
            data = (item_quantity, item_name)
            cursor.execute(update_query, data)
            cursor.execute("DELETE FROM inventory WHERE item_quantity <= 0")
            cnx.commit()
            print(f"{item_quantity} unit/s of {item_name} has been removed from inventory.")

            print("Table Updated.")
            cursor.execute("SELECT * FROM inventory")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    elif action == "Check Stock":
        cursor.execute("SELECT * FROM inventory")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    else:
        print("Please enter a valid input.")
        inventory_sys()


def home(option=None):
    option = input("Signup | Login | Exit: ")
    if option == "Signup":
        register()
    elif option == "Login":
        access()
    elif option == "Exit":
        return
    else:
        print("Please enter a valid option.")

home()
