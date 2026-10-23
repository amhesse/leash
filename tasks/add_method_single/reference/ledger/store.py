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

    def total_for(self, category: str) -> int:
        return sum(e.cents for e in self.entries if e.category == category)
