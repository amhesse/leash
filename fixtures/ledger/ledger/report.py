from .money import format_cents
from .store import Ledger


def summary(ledger: Ledger) -> str:
    lines = []
    for category in ledger.categories():
        total = sum(e.cents for e in ledger.entries if e.category == category)
        lines.append(f"{category}: {format_cents(total)}")
    lines.append(f"balance: {format_cents(ledger.balance())}")
    return "\n".join(lines)
