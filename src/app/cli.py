"""
CLI app
"""

import typer

from .app import add_gear_query
from .data.data import init_db

app = typer.Typer()
app.command()(add_gear_query)

@app.command()
def setup():
    init_db()

if __name__ == "__main__":
    app()
