import typer
from typing_extensions import Annotated

from .gear import search_gear


def add_gear_query(search_term: Annotated[str, typer.Argument()]):
    search_gear(search_term)
