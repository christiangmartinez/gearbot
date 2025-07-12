"""
CLI app
"""

import typer

from .app import add_gear_query
from .data.data import init_db
from .data.fetch import fetch_gear_list

app = typer.Typer()
app.command()(add_gear_query)

@app.command()
def setup():
    init_db()

@app.command()
def print_gear_list():
    gear_list = fetch_gear_list()
    if not gear_list:
        print("No gear to display")
    print(gear_list)

if __name__ == "__main__":
    app()
