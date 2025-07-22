"""
Insert data to tables
"""

from .data import execute_sql_query


def post_gear_query(search_term: str, timestamp: str):
    """Post gear query to gear_queries table."""
    query_values = (search_term, timestamp)
    sql_query = "INSERT INTO gear_queries (search_term, timestamp) VALUES (?, ?)"
    execute_sql_query(sql_query, query_values)

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
    execute_sql_query(sql_query, gear_tuples, execute_many=True)


def post_gear_matches(gear_matches: list):
    """Post gear matches to database."""
    match_tuples = [
        (match["name"], match["price"], match["link"], match["query_id"])
        for match in gear_matches
    ]
    sql_query = "INSERT INTO gear_matches (name, price, link, query_id) VALUES (?, ?, ?, ?)"
    execute_sql_query(sql_query, match_tuples, execute_many=True)
