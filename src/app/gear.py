class GearQuery:
    def __init__(self, search_term, query_date, gear_list):
        self.search_term = search_term
        self.query_date = query_date
        self.gear_list = gear_list

def find_gear_match(search_term: str, gear_list: list):
    search_term_set = set(search_term.lower().split())

    gear_match_list = []
    for item in gear_list:
        item_set = set(item["name"].lower().split())
        if search_term_set.issubset(item_set):
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
