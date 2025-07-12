"""
Insert data to tables
"""

import sqlite3

from .data import execute_sql_query


def post_gear_list(gear_list: list):
    """"Post all items in gear_list to gear_list table"""
    gear_tuples = []
    _convert_to_tuples(gear_list, gear_tuples)
    sql_query = "INSERT INTO gear_list(name, price, link) VALUES (?, ?, ?)"

    execute_sql_query(sql_query, gear_tuples, execute_many=True)


def post_gear_query(search_term: str, query_date: str):
    """Post gear query to gear_queries table"""
    sql_query = "INSERT INTO gear_queries (search_term, query_date) VALUES (?, ?)"
    execute_sql_query(sql_query, search_term, query_date)

def post_gear_matches(gear_matches: list):
    """Post gear matches to database"""
    sql_query = "INSERT INTO gear_matches (name, price, link, queryid) VALUES (?, ?, ?, ?)"
    execute_sql_query(sql_query, gear_matches, execute_many=True)

def _convert_to_tuples(input_list: list, output_list: list):
    for item in input_list:
        name = item["name"]
        price = item["price"]
        link = item["link"]
        output_list.append((name, price, link))
