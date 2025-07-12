"""
Logic to initialize database and general SQL functions
"""

import sqlite3
from typing import Any, List, Optional, Tuple, Union

GEAR_DB = "gear_data.db"

def init_db():
    """Initialize database and create tables"""
    connection = None
    try:
        connection = sqlite3.connect(GEAR_DB)
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gear_list (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL,
                link TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gear_queries (
                query_id INTEGER PRIMARY KEY AUTOINCREMENT,
                search_term TEXT,
                query_date TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gear_matches (
                gear_match_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL,
                link TEXT,
                query_id INT,
                FOREIGN KEY(query_id) REFERENCES gear_query(query_id)
            )
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
    is_select: bool = False,
) -> Optional[List[Tuple[Any,...]]]:
    """
    Executes a SQL query and returns optional results
    params: values to be inserted into tables - single tuple or list of tuples.

    execute_many: false uses execute for single value,
        true uses execute for a list of tuples.
    is_select: True to fetch all results from a SELECT query


    """
    try:
        with sqlite3.connect(GEAR_DB) as connection:
            cursor = connection.cursor()
            if execute_many:
                cursor.executemany(sql_query, params)
            else:
                cursor.execute(sql_query, params)
            if is_select:
                return cursor.fetchall()
            return None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
