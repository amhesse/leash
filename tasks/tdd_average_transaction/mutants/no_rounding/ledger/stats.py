from ledger.store import Ledger


def average_transaction(ledger: Ledger, category: str) -> float:
    values = [e.cents for e in ledger.entries if e.category == category]
    if not values:
        raise ValueError(f"no entries in category {category!r}")
    return sum(values) / len(values)
