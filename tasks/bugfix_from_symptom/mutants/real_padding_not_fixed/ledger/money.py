"""Money is always an int number of cents; strings only at the edges."""


def parse_amount(text: str) -> int:
    """Parses "12", "12.5", "12.50" or "$12.50" into cents."""
    text = text.strip().lstrip("$")
    if "." in text:
        whole, frac = text.split(".", 1)
        if len(frac) > 2:
            raise ValueError(f"too many decimal places: {text!r}")
        return int(whole) * 100 + int(frac)
    return int(text) * 100


def format_cents(cents: int) -> str:
    """Formats cents as "$12.50"."""
    return f"${cents // 100}.{cents % 100:02d}"
