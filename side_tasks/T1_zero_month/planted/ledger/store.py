import dataclasses
import datetime


@dataclasses.dataclass
class Entry:
    date: datetime.date
    category: str
    cents: int  # positive is income, negative is spending
    note: str = ""


class Ledger:
    def __init__(self):
        self.entries: list[Entry] = []

    def add(self, entry: Entry) -> None:
        self.entries.append(entry)

    def balance(self) -> int:
        return sum(e.cents for e in self.entries)

    def categories(self) -> list[str]:
        return sorted({e.category for e in self.entries})

    def by_month(self) -> dict[str, int]:
        totals: dict[str, int] = {}
        for e in sorted(self.entries, key=lambda e: e.date):
            key = f"{e.date.year:04d}-{e.date.month:02d}"
            totals[key] = totals.get(key, 0) + e.cents
        return {month: total for month, total in totals.items() if total != 0}
