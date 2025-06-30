import typer

from .gear import search_gear


def main(search_term: str):
    search_gear(search_term)

if __name__ == "__main__":
    typer.run(main)
