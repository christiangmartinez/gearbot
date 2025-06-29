from .scrapers.gear_scraper import get_latest_gear


def search_gear(search_term):
    gear = get_latest_gear()
    search_set = make_set(search_term)

    matches = []
    for item in gear:
        item_set = make_set(item["name"])
        if search_set.issubset(item_set):
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

def make_set(string):
    return set(string.lower().split())
