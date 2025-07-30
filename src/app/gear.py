"""GearQuery class and functions for interacting with queries."""
import sqlite3
from typing import Dict, List, Optional

from data.fetch import (fetch_all_gear_queries, fetch_gear_matches,
                        fetch_open_gear_queries, fetch_query)


class GearQuery:
    """Gear queries are added by user. Everything interacts with these queries."""
    def __init__(self, search_term: str, timestamp: str, query_id: int=0, is_open: bool=True):
        self.query_id = query_id
        self.is_open = is_open
        self.search_term = search_term
        self.timestamp = timestamp
        self.matches = []


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

def get_query(search_term: str) -> Optional[GearQuery]:
    """Returns an open query matching SEARCHTERM."""
    query = fetch_query(search_term)
    if query is None:
        return None
    return convert_to_gear_query(query)

def get_open_queries() -> Optional[list[GearQuery]]:
    """Retrieves all open gear queries, returns a list of objects."""
    queries = fetch_open_gear_queries()
    if queries is None:
        return None
    return convert_queries(queries)

def get_all_queries() -> Optional[list[GearQuery]]:
    """Returns all queries and any matches"""
    queries_row = fetch_all_gear_queries()
    if queries_row is None:
        return None
    queries = convert_queries(queries_row)
    add_matches(queries)
    return queries

def add_matches(queries: list[GearQuery]) -> Optional[list[GearQuery]]:
    """Fetches all matches and adds them to associated queries."""
    matches = fetch_gear_matches()
    if matches is None:
        return None
    query_map = {}
    for query in queries:
        query_map[query.query_id] = query
    for match in matches:
        name, price, link, query_id = match
        if query_id in query_map:
            query_map[query_id].matches.append(f"{name} {price}\n{link}\n")
    return queries

def convert_to_gear_query(query_row: sqlite3.Row) -> GearQuery:
    """
    Takes a sqlite3 Row returned from from a fetch call.
    Converts it to a GearQuery object so it can be interacted with.
    """
    query = GearQuery(
        query_row["search_term"],
        query_row["timestamp"],
        query_row["id"],
        query_row["is_open"])
    return query

def convert_queries(query_row_list: List[sqlite3.Row]) -> list[GearQuery]:
    """Converts a list of Rows from the database to Gear Queries."""
    queries = []
    for query_row in query_row_list:
        query = convert_to_gear_query(query_row)
        queries.append(query)
    if not queries:
        print("No queries found")
    return queries
