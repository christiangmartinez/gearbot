"""
CLI app
"""

import typer

from .app import add_gear_query
from .data.data import init_db
from .gear import get_active_queries

app = typer.Typer()
app.command()(add_gear_query)

@app.command()
def setup():
    init_db()

@app.command()
def print_active_queries():
    get_active_queries()

if __name__ == "__main__":
    app()
