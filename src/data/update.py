"""
Udate table data.
"""

from .data import execute_sql_query


def update_query_status(search_term: str, is_open: bool):
    """Update the status of a query by SEARCHTERM."""
    params = (is_open, search_term)
    sql_query = """UPDATE gear_queries
        SET is_open = ?
        WHERE search_term = ?
    """
    execute_sql_query(sql_query, params)
