def over_budget(ledger, limits: dict[str, int]) -> dict[str, int]:
    result = {}
    for category, limit in limits.items():
        spent = -sum(e.cents for e in ledger.entries if e.category == category)
        if spent > limit:
            result[category] = spent - limit
    return result
