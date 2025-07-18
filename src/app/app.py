"""
Add gear query logic
"""

from datetime import datetime

from data.fetch import fetch_gear_list
from data.post import post_gear_list, post_gear_matches, post_gear_query
from scrapers.gear_scraper import get_latest_gear

from .gear import GearQuery, get_active_queries


def add_gear_query(search_term: str):
    """Create a new gear query"""
    timestamp = datetime.now().strftime("%Y-%m-%d")
    new_gear_query = GearQuery(search_term, timestamp)
    post_gear_query(new_gear_query.search_term, new_gear_query.timestamp)

def update_gear_matches():
    """Checks current gear list for matches for any active queries"""
    gear_list = fetch_gear_list()
    active_queries = get_active_queries()
    for query in active_queries:
        print(query.search_term)
        matches = query.find_match(query.search_term, gear_list)
        post_gear_matches(matches)

def update_gear_list():
    """Scrapes latest gear at Hank's and updates DB"""
    gear_list = get_latest_gear()
    post_gear_list(gear_list)
