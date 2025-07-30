"""
Fetch data from tables.
"""
import sqlite3
from typing import List, Optional

from .sql_funcs import sql_fetch_all, sql_fetch_one


def fetch_query(search_term: str) -> Optional[sqlite3.Row]:
    """Fetch a specific query matching SEARCHTERM."""
    sql_query = "SELECT id, is_open, search_term, timestamp FROM gear_queries WHERE search_term = ?"
    return sql_fetch_one(sql_query,(search_term,))

def fetch_open_gear_queries() -> Optional[List[sqlite3.Row]]:
    """Fetch all gear queries."""
    return sql_fetch_all("SELECT id, is_open, search_term, timestamp FROM gear_queries WHERE is_open = 1")

def fetch_all_gear_queries() -> Optional[List[sqlite3.Row]]:
    """Fetch all gear queries."""
    return sql_fetch_all("SELECT id, is_open, search_term, timestamp FROM gear_queries")

def fetch_gear_list() -> Optional[List[sqlite3.Row]]:
    """Fetch all items in gear list table."""
    return sql_fetch_all("SELECT name, price, link FROM gear_list")

def fetch_gear_matches() -> Optional[List[sqlite3.Row]]:
    """Fetch all items in gear_matches table"""
    return sql_fetch_all("SELECT name, price, link, query_id FROM gear_matches")

def open_query_exists(search_term: str) -> bool:
    """Check if a query already exists for SEARCHTERM."""
    sql_query = "SELECT 1 FROM gear_queries WHERE search_term = ? AND is_open = 1 LIMIT 1"
    result = sql_fetch_one(sql_query, (search_term,))
    return result is not None
