"""
Database creation
"""

import sqlite3


def init_db():
    """Initialize databases"""
    connection = None
    try:
        connection = sqlite3.connect("gear_data.db")
        cursor = connection.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS gear_list(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAl,
            link TEXT
        )""")

        cursor.execute(""" CREATE TABLE IF NOT EXISTS gear_query(
            query_id INTEGER PRIMARY KEY AUTOINCREMENT,
            search_term TEXT,
            query_date TEXT,
        )""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS gear_matches(
            gear_match_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL,
            link TEXT,
            query_id INT,
            FOREIGN KEY(query_id) REFERENCES gear_query(query_id)
        )""")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        if connection:
            connection.close()
