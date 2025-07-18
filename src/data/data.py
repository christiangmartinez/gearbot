"""
Logic to initialize database and general SQL functions
"""

import sqlite3
from typing import Any, List, Optional, Tuple, Union

GEAR_DB = "gear_data.db"

def init_db():
    """
    Initialize the required database.
    Run after installation.
    """
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
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                search_term TEXT,
                timestamp TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gear_matches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL,
                link TEXT,
                query_id INTEGER,
                FOREIGN KEY(query_id) REFERENCES gear_queries(id)
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
) -> Optional[List[sqlite3.Row]]:
    """
    Executes a SQL query and returns optional results
    params: values to be inserted into tables - single tuple or list of tuples.

    execute_many: false uses execute for single value,
        true uses execute for a list of tuples.
    is_select: True to fetch all results from a SELECT query


    """
    try:
        with sqlite3.connect(GEAR_DB) as connection:
            connection.row_factory = sqlite3.Row
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
