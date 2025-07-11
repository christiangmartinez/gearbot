"""
Fetch data from tables
"""

import sqlite3


def fetch_gear_queries():
    """Fetch all gear queries"""
    connection = None
    try:
        connection = sqlite3.connect("gear_data.db")
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM gear_queries""")
        response = cursor.fetchall()
        return response
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        if connection:
            connection.close()
