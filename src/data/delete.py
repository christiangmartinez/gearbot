"""
Delete items from SQL tables.
"""

from .sql_funcs import sql_execute


def delete_query_matches(query_id: int):
    """Delete matches for a given query from gear_matches table."""
    sql_query = """DELETE FROM gear_matches WHERE query_id = ?"""
    sql_execute(sql_query, (query_id,))

def delete_query(search_term: str):
    """Delete a query with SEARCHTERM."""
    sql_query = """DELETE FROM gear_queries WHERE search_term = ?"""
    sql_execute(sql_query, (search_term,))
