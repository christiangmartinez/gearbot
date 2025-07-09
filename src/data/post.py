"""
Insert data to tables
"""

import os
import sqlite3


def post_gear_list(gear_list: list):
    """"Post gear list to database"""
    check_db()
    connection = None
    try:
        connection = sqlite3.connect("gear_data.db")
        cursor = connection.cursor()

        gear_tuples = []
        for item in gear_list:
            name = item["name"]
            price = item["price"]
            link = item["link"]
            gear_tuples.append((name, price, link))

        if not gear_tuples:
            print("No valid data exists...")

        cursor.executemany("INSERT INTO gear_list (name, price, link) VALUES (?, ?, ?)", gear_tuples)

    except sqlite3.Error as e:
        print(f'Database error: {e}')

    finally:
        if connection:
            connection.close()

def post_gear_query(search_term: str, query_date: str):
    """Post gear query to database"""
    check_db()
    connection = None
    try:
        connection = sqlite3.connect("gear_data.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO gear_query (search_term, query_date) VALUES (?, ?)", (search_term, query_date))

    except sqlite3.Error as e:
        print(f'Database error: {e}')

    finally:
        if connection:
            connection.close()

def post_gear_match(name: str, price: str, link: str, query_id: int):
    """Post gear matches to database"""
    check_db()
    connection = None
    try:
        connection = sqlite3.connect("gear_data.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO gear_matches (name, price, link, queryid) VALUES (?, ?, ?, ?)", (name, price, link, query_id))

    except sqlite3.Error as e:
        print(f'Database error: {e}')

    finally:
        if connection:
            connection.close()

def check_db():
    """Check if database exists"""
    if not os.path.isfile("gear_list.db"):
        print("Error: gear list database not found. Please run 'gearbot setup'")

