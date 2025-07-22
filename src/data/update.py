"""
Udate table data.
"""

from .data import execute_sql_query


def update_query_status(search_term: str, is_open: bool):
    """Update the status of a query by SEARCHTERM."""
    params = (search_term, is_open)
    sql_query = """UPDATE gear_list WHERE search_term = ? SET is_open = ?"""
    execute_sql_query(sql_query, params)
