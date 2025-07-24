"""
Insert data to tables.
"""

from .sql_funcs import sql_execute, sql_execute_many


def post_gear_query(search_term: str, timestamp: str, is_open: bool):
    """Post gear query to gear_queries table."""
    query_values = (search_term, timestamp, is_open)
    sql_query = "INSERT INTO gear_queries (search_term, timestamp, is_open) VALUES (?, ?, ?)"
    sql_execute(sql_query, query_values)

def post_gear_list(gear_list: list):
    """"
    Post all items in gear_list to gear_list table.
    Reverses gear list to order items oldest to newest in database so trigger
    can maintain 30 item cap. Oldest items out first.
    """
    gear_list.reverse()
    gear_tuples = [
        (gear["name"], gear["price"], gear["link"])
        for gear in gear_list
    ]
    sql_query = "INSERT INTO gear_list(name, price, link) VALUES (?, ?, ?)"
    sql_execute_many(sql_query, gear_tuples)


def post_gear_matches(gear_matches: list):
    """Post gear matches to database."""
    match_tuples = [
        (match["name"], match["price"], match["link"], match["query_id"])
        for match in gear_matches
    ]
    sql_query = "INSERT INTO gear_matches (name, price, link, query_id) VALUES (?, ?, ?, ?)"
    sql_execute_many(sql_query, match_tuples)
