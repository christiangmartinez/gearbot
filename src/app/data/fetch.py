"""
Fetch data from tables
"""

import sqlite3

from .data import execute_sql_query


def fetch_gear_queries():
    """Fetch all gear queries"""
    execute_sql_query("SELECT * FROM gear_queries")

def fetch_gear_list():
    """Fetch all items in gear list table"""
    execute_sql_query("SELECT * FROM gear_list")
