"""
Update table data.
"""

from .sql_funcs import sql_execute


def update_query_status(search_term: str, is_open: bool):
    """Update the status of a query by SEARCHTERM."""
    params = (is_open, search_term)
    sql_query = """UPDATE gear_queries SET is_open = ? WHERE search_term = ?"""
    sql_execute(sql_query, params)
