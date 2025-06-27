"""
MAIN - update later
"""
import sys

from playwright.sync_api import sync_playwright

from .scrapers.gear_scraper import get_latest_gear


def main():
    if len(sys.argv) < 2:
        print("Search term must be provided")
        print('Usage: python3 main.py "gear you want"')
        sys.exit(1)

    search_term = sys.argv[1]

    with sync_playwright() as playwright:
        gear = get_latest_gear(playwright)

    matches = []
    for item in gear:
        if search_term.lower() in item["name"].lower():
            matches.append(f'{item["name"]}: {item["price"]}\n{item["link"]}')

    if not matches:
        print(f'No matches for {search_term}')
        return

    print(
        f"{len(matches) if len(matches) > 1 else ''}"
        f"{' Matches' if len(matches) > 1 else 'Match'} found for {search_term}!"
    )
    for match in matches:
        print(match)

if __name__ == "__main__":
    main()
