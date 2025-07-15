from typing import Dict, List, Optional

from .data.fetch import fetch_gear_list, fetch_gear_queries
from .data.post import post_gear_matches


class GearQuery:
    def __init__(self, search_term: str, query_date: str):
        self.query_id = 0
        self.search_term = search_term
        self.query_date = query_date
        self.matches = []


    def find_match(self, search_term: str, gear_list: list) -> Optional[List[Dict]]:
        search_term_set = set(search_term.lower().split())

        for item in gear_list:
            item_set = set(item["name"].lower().split())
            if search_term_set.issubset(item_set):
                match = item.update({"query_id": self.query_id})
                self.matches.append(match)

        if not self.matches:
            print(f'No matches for {search_term}')
            return None

        print(
            f"{len(self.matches) if len(self.matches) > 1 else ''}"
            f"{' Matches' if len(self.matches) > 1 else 'Match'} found for {search_term}!"
        )

        for match in self.matches:
            print(f'{match["name"]}: {match["price"]} \n {match["link"]}')
        return self.matches

#def find_gear_matches():
#    active_queries = get_active_queries()
#    gear_list = fetch_gear_list()
#    if active_queries and gear_list:
#    for query in active_queries:
#        query.find_match(gear_list)


def get_active_queries():
    active_queries = []
    response = fetch_gear_queries()
    if response:
        for item in response:
            query = GearQuery(item["search_term"], item["query_date"])
            query.query_id = item["id"]
            active_queries.append(query)
        for query in active_queries:
            print(f"id: {query.query_id} search term: {query.search_term}")
        return active_queries
    print("No active queries found")
    return None
