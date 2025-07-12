"""
Database creation
"""

import sqlite3
from typing import Any, List, Tuple, Union


def init_db():
    """Initialize database and create tables"""
    connection = None
    try:
        connection = sqlite3.connect("gear_data.db")
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gear_list (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL,
                link TEXT
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gear_queries (
                query_id INTEGER PRIMARY KEY AUTOINCREMENT,
                search_term TEXT,
                query_date TEXT
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gear_matches (
                gear_match_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL,
                link TEXT,
                query_id INT,
                FOREIGN KEY(query_id) REFERENCES gear_query(query_id)
            );
        """)

        connection.commit()
        print("Sucessfully created database.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        if connection:
            connection.close()

def execute_sql_query(
    sql_query: str,
    params: Union[Tuple[Any, ...], List[Tuple[Any, ...]]] = (),
    execute_many: bool = False,
):
    try:
        connection = sqlite3.connect("gear_data.db")
        cursor = connection.cursor()
        if execute_many:
            cursor.executemany(sql_query, params)
        else:
            cursor.execute(sql_query, params)
        connection.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
