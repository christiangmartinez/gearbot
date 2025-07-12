"""
Fetch data from tables
"""

from .data import execute_sql_query


def fetch_gear_queries():
    """Fetch all gear queries"""
    return execute_sql_query("SELECT * FROM gear_queries", is_select=True)

def fetch_gear_list():
    """Fetch all items in gear list table"""
    return execute_sql_query("SELECT * FROM gear_list", is_select=True)
