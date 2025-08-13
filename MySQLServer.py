import mysql.connector from mysql.connector 
import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (adjust credentials if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: Could not connect or create database. Details: {err}")

    finally:
        if connection and connection.is_connected():
            cursor.close() # type: ignore
            connection.close()
            # Optional: print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
