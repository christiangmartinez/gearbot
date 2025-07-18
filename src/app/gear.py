from typing import Dict, List

from data.fetch import fetch_gear_queries


class GearQuery:
    def __init__(self, search_term: str, timestamp: str):
        self.query_id = 0
        self.search_term = search_term
        self.timestamp = timestamp
        self.matches = []


    def find_match(self, search_term: str, gear_list: list) -> List[Dict]:
        """Searches for a match for a query's search term, returns a list of matches"""
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

def get_active_queries():
    """Retrieve all active gear queries, returns a list of objects"""
    active_queries = []
    response = fetch_gear_queries()
    if response:
        for item in response:
            query = GearQuery(item["search_term"], item["timestamp"])
            query.query_id = item["id"]
            active_queries.append(query)
        return active_queries
    print("No active queries found")
    return active_queries
