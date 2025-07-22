"""GearQuery class and functions for interacting with queries."""
from typing import Dict, List

from data.fetch import fetch_open_gear_queries


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

def get_open_queries():
    """Retrieve all open gear queries, returns a list of objects."""
    open_queries = []
    response = fetch_open_gear_queries()
    if response:
        for item in response:
            query = GearQuery(item["search_term"], item["timestamp"])
            query.query_id = item["id"]
            open_queries.append(query)
    if not open_queries:
        print("No open queries found")
    return open_queries
