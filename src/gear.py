from .scrapers.gear_scraper import get_latest_gear


def search_gear(search_term):
    gear_list = get_latest_gear()
    search_set = make_set(search_term)

    gear_match_list = []
    for item in gear_list:
        item_set = make_set(item["name"])
        if search_set.issubset(item_set):
            gear_match_list.append(f'{item["name"]}: {item["price"]}\n{item["link"]}')

    if not gear_match_list:
        print(f'No gear_match_list for {search_term}')
        return

    print(
        f"{len(gear_match_list) if len(gear_match_list) > 1 else ''}"
        f"{' Matches' if len(gear_match_list) > 1 else 'Match'} found for {search_term}!"
    )

    for gear_match in gear_match_list:
        print(gear_match)

def make_set(input_string):
    return set(input_string.lower().split())
