"""
Logic for CLI commands.
"""

from datetime import datetime

import typer
from typing_extensions import Annotated

from data.delete import delete_query, delete_query_matches
from data.fetch import fetch_gear_list
from data.post import post_gear_list, post_gear_matches, post_gear_query
from data.update import update_query_status
from scrapers.gear_scraper import get_latest_gear

from .gear import GearQuery, get_open_queries, get_query


def add_gear_query(search_term: Annotated[str, typer.Argument()]):
    """Search for a new item with SEARCHTERM."""
    timestamp = datetime.now().strftime("%Y-%m-%d")
    new_gear_query = GearQuery(search_term, timestamp)
    post_gear_query(
        new_gear_query.search_term,
        new_gear_query.timestamp,
        new_gear_query.is_open
    )

def close_gear_query(search_term: Annotated[str, typer.Argument()]):
    """Close a query for given SEARCHTERM."""
    query = get_query(search_term)
    if query:
        query.close_query()
        update_query_status(query.search_term, query.is_open)

def update_gear_matches():
    """Search for matches for all open queries. Update results."""
    gear_list = fetch_gear_list()
    active_queries = get_open_queries()
    if active_queries:
        for query in active_queries:
            print(query.search_term)
            matches = query.find_match(query.search_term, gear_list)
            post_gear_matches(matches)

def update_gear_list():
    """Run web scraper to update gear list."""
    gear_list = get_latest_gear()
    post_gear_list(gear_list)

def delete_gear_query(search_term: Annotated[str, typer.Argument()]):
    """Delete a query with SEARCHTERM and any associated matches."""
    typer.confirm(f"Delete query for {search_term} + history/matches?", abort=True)
    query = get_query(search_term)
    if query:
        if query.matches:
            delete_query_matches(query.query_id)
        delete_query(query.search_term)
        print(f"Deleted query for {query.search_term}")

