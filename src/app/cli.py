import typer

from .app import add_gear_query

app = typer.Typer()
app.command()(add_gear_query)

if __name__ == "__main__":
    app()
