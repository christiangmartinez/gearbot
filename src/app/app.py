"""
Add gear query logic
"""

from datetime import datetime

import typer
from typing_extensions import Annotated

from .data.post import post_gear_list, post_gear_query
from .gear import GearQuery
from .scrapers.gear_scraper import get_latest_gear


def add_gear_query(search_term: Annotated[str, typer.Argument()]):
    """Create a new gear query"""
    gear_list = get_latest_gear()
    post_gear_list(gear_list)

    query_date = datetime.now().strftime("%Y-%m-%d")
    new_gear_query = GearQuery(search_term, query_date)
    post_gear_query(new_gear_query.search_term, new_gear_query.query_date)
#    new_gear_query.find_gear_match(new_gear_query.search_term, gear_list)
