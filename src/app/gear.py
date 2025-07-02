class GearQuery:
    def __init__(self, search_term: str, query_date: object):
        self.search_term = search_term
        self.query_date = query_date
        self.matches = []


    def find_gear_match(self, search_term: str, gear_list: list):
        search_term_set = set(search_term.lower().split())

        for item in gear_list:
            item_set = set(item["name"].lower().split())
            if search_term_set.issubset(item_set):
                self.matches.append(item)

        if not self.matches:
            print(f'No matches for {search_term}')
            return

        print(
            f"{len(self.matches) if len(self.matches) > 1 else ''}"
            f"{' Matches' if len(self.matches) > 1 else 'Match'} found for {search_term}!"
        )

        for match in self.matches:
            print(f'{match["name"]}: {match["price"]} \n {match["link"]}')
