import sys

from .gear import search_gear


def main():
    if len(sys.argv) < 2:
        print("Search term must be provided")
        print('Usage: python3 -m src.main "gear you want"')
        sys.exit(1)

    search_term = sys.argv[1]
    search_gear(search_term)

if __name__ == "__main__":
    main()
