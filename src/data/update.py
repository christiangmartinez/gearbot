"""
Udate table data.
"""

from .data import execute_sql_query


def update_query_status(search_term: str, is_open: bool):
    """Update the status of a query by SEARCHTERM."""

