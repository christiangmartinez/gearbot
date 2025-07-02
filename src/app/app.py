
from datetime import datetime

import typer
from typing_extensions import Annotated

from .gear import GearQuery
from .scrapers.gear_scraper import get_latest_gear


def add_gear_query(search_term: Annotated[str, typer.Argument()]):
    gear_list = get_latest_gear()
    query_date = datetime.now()
    new_gear_query = GearQuery(search_term, query_date)
    print(f'GEAR QUERY MATCHES BEFORE: {new_gear_query.matches}')
    new_gear_query.find_gear_match(new_gear_query.search_term, gear_list)

    print(f'GEAR QUERY SEARCH TERM: {new_gear_query.search_term}')
    print(f'GEAR QUERY DATE: {new_gear_query.query_date}')
    print(f'GEAR QUERY MATCHES AFTER: {new_gear_query.matches}')
