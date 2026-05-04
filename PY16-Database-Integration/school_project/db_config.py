import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="schooldb",
            user="root",
            password="admindisha26"
        )
        return connection

    except Error as e:
        print("Database connection error:", e)
        return None