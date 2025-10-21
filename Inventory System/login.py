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
            if count == 3:
                sys.exit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")