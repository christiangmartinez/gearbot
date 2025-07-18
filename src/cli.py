"""
CLI app
"""

import typer
from typing_extensions import Annotated

from app.app import add_gear_query, update_gear_list, update_gear_matches
from data.data import init_db

app = typer.Typer()

@app.command()
def setup():
    init_db()

@app.command()
def main(search_term: Annotated[str, typer.Argument()]):
    add_gear_query(search_term)

app.command()(update_gear_matches)
app.command()(update_gear_list)

if __name__ == "__main__":
    app()
