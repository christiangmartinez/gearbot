"""
Insert data to tables
"""

import sqlite3


def post_gear_list(gear_list: list):
    """"Post gear list to database"""
    connection = None
    try:
        connection = sqlite3.connect("gear_data.db")
        cursor = connection.cursor()

        gear_tuples = []
        _convert_to_tuples(gear_list, gear_tuples)

        if not gear_tuples:
            print("No valid data exists...")

        cursor.executemany(
            """INSERT INTO gear_list
            (name, price, link) VALUES (?, ?, ?)""",
            gear_tuples)
        connection.commit()

    except sqlite3.Error as e:
        print(f'Database error: {e}')

    finally:
        if connection:
            connection.close()

def post_gear_query(search_term: str, query_date: str):
    """Post gear query to database"""
    connection = None
    try:
        connection = sqlite3.connect("gear_data.db")
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO gear_queries 
            (search_term, query_date) VALUES (?, ?)""",
            (search_term, query_date))
        connection.commit()

    except sqlite3.Error as e:
        print(f'Database error: {e}')

    finally:
        if connection:
            connection.close()

def post_gear_matches(gear_matches: list):
    """Post gear matches to database"""
    connection = None
    try:
        connection = sqlite3.connect("gear_data.db")
        cursor = connection.cursor()
        match_tuples = []
        _convert_to_tuples(gear_matches, match_tuples)

        if not match_tuples:
            print("No valid data exists...")

        cursor.executemany(
            """INSERT INTO gear_matches 
            (name, price, link, queryid) VALUES (?, ?, ?, ?)""",
            gear_matches)
        connection.commit()

    except sqlite3.Error as e:
        print(f'Database error: {e}')

    finally:
        if connection:
            connection.close()

def _convert_to_tuples(input_list: list, output_list: list):
    for item in input_list:
        name = item["name"]
        price = item["price"]
        link = item["link"]
        output_list.append((name, price, link))
