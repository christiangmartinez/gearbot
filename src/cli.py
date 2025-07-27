"""
CLI app.
"""

import typer

from app.commands import *
from data.sql_funcs import init_db

app = typer.Typer()

app.command("setup")(init_db)
app.command("search")(add_gear_query)
app.command("close-query")(close_gear_query)
app.command("update-matches")(update_gear_matches)
app.command("update-gear")(update_gear_list)
app.command("delete")(delete_gear_query)
app.command("report")(print_report)

if __name__ == "__main__":
    app()
