"""
CLI app.
"""

import typer

from app.commands import *
from data.data import init_db

app = typer.Typer()

app.command("setup")(init_db)
app.command("search")(add_gear_query)
app.command("close-query")(close_gear_query)
app.command("update-matches")(update_gear_matches)
app.command("update-gear")(update_gear_list)

if __name__ == "__main__":
    app()
