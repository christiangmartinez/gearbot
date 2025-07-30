"""
Logic to initialize database and general SQL functions.
"""

import sqlite3
from typing import Any, List, Optional, Tuple

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
                name TEXT NOT NULL,
                price REAL NOT NULL,
                link TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS limit_gear_list_to_thirty_items
            AFTER INSERT ON gear_list
            WHEN (SELECT COUNT(*) FROM gear_list) > 30
            BEGIN
                DELETE FROM gear_list
                WHERE id IN (SELECT id FROM GEAR_LIST ORDER BY id ASC
                    LIMIT (SELECT COUNT(*) FROM gear_list) - 30);
            END;
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gear_queries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                is_open INTEGER NOT NULL,
                search_term TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gear_matches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                link TEXT NOT NULL,
                query_id INTEGER NOT NULL,
                FOREIGN KEY(query_id)
                    REFERENCES gear_queries(id)
            )
        """)

        connection.commit()
        print("Successfully created database.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        if connection:
            connection.close()

def sql_execute(sql_query: str, params: Tuple[Any,...]):
    """
    Perform a SQL with execute where a return value is not required.
    """
    with sqlite3.connect(GEAR_DB) as connection:
        cursor = connection.cursor()
        cursor.execute(sql_query, params)

def sql_execute_many(sql_query: str, params: List[Tuple[Any, ...]]):
    """
    Perform a SQL with executemany where a return value is not required.
    """
    with sqlite3.connect(GEAR_DB) as connection:
        cursor = connection.cursor()
        cursor.executemany(sql_query, params)

def sql_fetch_one(sql_query: str, params: Tuple[Any, ...]) -> Optional[sqlite3.Row]:
    """Execute a SQL query that returns a single value."""
    with sqlite3.connect(GEAR_DB) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(sql_query, params)
        response = cursor.fetchone()
        return response if response else None

def sql_fetch_all(sql_query: str) -> Optional[List[sqlite3.Row]]:
    """Execute a SQL query that returns a list of values."""
    with sqlite3.connect(GEAR_DB) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(sql_query)
        response = cursor.fetchall()
        return response if response else None
