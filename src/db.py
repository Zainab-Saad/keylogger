from dotenv import load_dotenv
import psycopg2
import os
from datetime import datetime

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

def insert_keypress(pressed_keys):
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, 
            user=USER, 
            password=PASSWORD, 
            host=HOST, 
            port=PORT
        )
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO keypress_log (pressed_keys, timestamp)
        VALUES (%s, %s);
        """

        cursor.execute(insert_query, (pressed_keys, datetime.now()))

        conn.commit()
        print(f"Inserted keys: {pressed_keys}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Database connection closed")

try:
    conn = psycopg2.connect(
        dbname=DB_NAME, 
        user=USER, 
        password=PASSWORD, 
        host=HOST, 
        port=PORT
    )
    cursor = conn.cursor()
    print("Connected to the database")

    create_table_query = """
    CREATE TABLE IF NOT EXISTS keypress_log (
        id SERIAL PRIMARY KEY,  -- Unique ID (auto-incremented)
        pressed_keys TEXT[],    -- Array of characters (list of keys)
        timestamp TIMESTAMPTZ   -- Timestamp with timezone
    );
    """

    cursor.execute(create_table_query)
    conn.commit()
    print("Table 'keypress_log' created successfully")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Database connection closed")
