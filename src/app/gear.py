"""GearQuery class and functions for interacting with queries."""
import sqlite3
from typing import Dict, List, Optional

from data.fetch import (fetch_all_gear_queries, fetch_open_gear_queries,
                        fetch_open_query_search_terms, fetch_query)


class GearQuery:
    """Gear queries are added by user. Everything interacts with these queries."""
    def __init__(self, search_term: str, timestamp: str):
        self.query_id = 0
        self.search_term = search_term
        self.timestamp = timestamp
        self.matches = []
        self.is_open = True


    def find_match(self, search_term: str, gear_list: list) -> List[Dict]:
        """Searches for a match for a query's search term, returns a list of matches."""
        search_term_set = set(search_term.lower().split())

        for item in gear_list:
            item_set = set(item["name"].lower().split())
            if search_term_set.issubset(item_set):
                match = {
                    "name": item["name"],
                    "price": item["price"],
                    "link": item["link"],
                    "query_id": self.query_id
                }
                self.matches.append(match)

        if not self.matches:
            print(f"No matches for {search_term}")
            return self.matches
        print(f"{len(self.matches)} match(es) for {search_term}")
        return self.matches

    def close_query(self):
        """
        A query is considered closed when a match is found 
        or can be can be closed by the user.
        """
        self.is_open = False

def get_query(search_term: str):
    """Returns an open query matching SEARCHTERM."""
    response = fetch_query(search_term)
    if response is None:
        return None
    query = convert_to_gear_query(response)
    return query

def get_open_queries():
    """Retrieve all open gear queries, returns a list of objects."""
    response = fetch_open_gear_queries()
    if response is None:
        return None
    return convert_queries(response)

def get_all_queries():
    """Returns all queries regardless of status"""
    response = fetch_all_gear_queries()
    if response is None:
        return None
    return convert_queries(response)

def convert_to_gear_query(sql_row: sqlite3.Row):
    """
    Takes a sqlite3 Row returned from from a fetch call.
    Converts it to a GearQuery object so it can be interacted with.
    """
    query = GearQuery(sql_row["search_term"], sql_row["timestamp"])
    return query

def convert_queries(sql_response: List[sqlite3.Row]):
    """Convert a list of Rows from the database to Gear Queries."""
    queries = []
    for item in sql_response:
        query = convert_to_gear_query(item)
        query.query_id = item["id"]
        queries.append(query)
    if not queries:
        print("No queries found")
    return queries

def query_exists(search_term: str) -> bool:
    """Check if a query already exists for SEARCHTERM."""
    existing_queries = fetch_open_query_search_terms()
    if existing_queries:
        for query in existing_queries:
            if search_term in query:
                return True
    return False
