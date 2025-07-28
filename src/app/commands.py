"""
Logic for CLI commands.
"""

from datetime import datetime

import typer
from rich.console import Console
from typing_extensions import Annotated

from data.delete import delete_query, delete_query_matches
from data.fetch import fetch_gear_list, open_query_exists
from data.post import post_gear_list, post_gear_matches, post_gear_query
from data.update import update_query_status
from scripts.gear_scraper import get_latest_gear

from .gear import GearQuery, get_all_queries, get_open_queries, get_query
from .report import generate_queries_table


def add_gear_query(search_term: Annotated[str, typer.Argument()]):
    """Search for a new item with SEARCHTERM."""
    if open_query_exists(search_term):
        print(f"Open query already exists for {search_term}")
    else:
        now = datetime.now()
        timestamp = now.isoformat(timespec="seconds")
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
        close_query_and_update_status(query)

def update_gear_matches():
    """Search for matches for all open queries. Update results."""
    gear_list = fetch_gear_list()
    active_queries = get_open_queries()
    if active_queries:
        for query in active_queries:
            matches = query.find_match(query.search_term, gear_list)
            if matches:
                post_gear_matches(matches)
                close_query_and_update_status(query)

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

def print_report(all_queries: Annotated[bool, typer.Option("--all")]=False):
    """Print a report with query status"""
    if all_queries:
        queries = get_all_queries()
    else:
        queries = get_open_queries()
    if not queries:
        print("No queries currently running")
    else:
        console = Console()
        table = generate_queries_table(queries, all_queries)
        console.print(table)

def close_query_and_update_status(query: GearQuery):
    """Closes a query and updates the database."""
    query.close_query()
    update_query_status(query.search_term, query.is_open)
