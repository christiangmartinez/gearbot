"""
Logic for generating Gear Query status reports.
"""
from datetime import datetime, timedelta

from rich.table import Table

from .gear import GearQuery


def generate_queries_table(queries: list[GearQuery], all_queries: bool=False) -> Table:
    """Generate table for open queries"""
    table = Table(show_lines=True)
    table.add_column("Search term")
    table.add_column("Query uptime")
    if all_queries:
        table.add_column("Matches")

    now = datetime.now()

    for query in queries:
        start_time = datetime.fromisoformat(query.timestamp)
        uptime: timedelta = now - start_time
        uptime_message = format_time_message(uptime)
        row_values = [query.search_term, uptime_message]
        if all_queries:
            if query.is_open:
                matches = "None - query open"
            elif not query.matches:
                matches = "No matches found"
            else:
                matches = "\n".join(query.matches)
            row_values.append(matches)
        table.add_row(*row_values)
    return table

def format_time_message(td: timedelta) -> str:
    """Formats a time delta to X days X hours X minutes X seconds."""
    total_seconds = int(td.total_seconds())
    if total_seconds == 0:
        return "0 seconds"

    time_string = []

    days = total_seconds // (24 * 3600)
    total_seconds %= (24 * 3600)
    if days > 0:
        time_string.append(f"{days} day{'s' if days != 1 else ''}")

    hours = total_seconds // 3600
    total_seconds %= 3600
    if hours > 0:
        time_string.append(f"{hours} hour{'s' if hours != 1 else ''}")

    minutes = total_seconds // 60
    total_seconds %= 60
    if minutes > 0:
        time_string.append(f"{minutes} minute{'s' if minutes != 1 else ''}")

    seconds = total_seconds
    if seconds > 0:
        time_string.append(f"{seconds} second{'s' if seconds != 1 else ''}")

    return " ".join(time_string)
