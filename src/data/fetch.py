"""
Fetch data from tables.
"""
import sqlite3
from typing import List, Optional

from .sql_funcs import sql_fetch_all, sql_fetch_one


def fetch_query(search_term: str) -> Optional[sqlite3.Row]:
    """Fetch a specific query matching SEARCHTERM."""
    sql_query = "SELECT * FROM gear_queries WHERE search_term = ?"
    return sql_fetch_one(sql_query,(search_term,))

def fetch_open_gear_queries() -> Optional[List[sqlite3.Row]]:
    """Fetch all gear queries."""
    return sql_fetch_all("SELECT * FROM gear_queries WHERE is_open = 1")

def fetch_open_query_search_terms() -> Optional[List[sqlite3.Row]]:
    """Fetch SEARCHTERM for all open queries"""
    return sql_fetch_all("SELECT search_term FROM gear_queries WHERE is_open = 1")

def fetch_all_gear_queries():
    """Fetch all gear queries."""
    return sql_fetch_all("SELECT * FROM gear_queries")

def fetch_gear_list():
    """Fetch all items in gear list table."""
    return sql_fetch_all("SELECT * FROM gear_list")

