# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-20T14:34-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| codestral:22b (Q4_0) | 1.6 | 0.0 | not measured | +1.6 | – | 210 | 0 |

## codestral:22b (Q4_0)

|  |  |
|---|---|
| Model | codestral:22b |
| Digest | 0898a8b286d56d81 |
| Size / quantization | 22.2B / Q4_0 |
| Runtime | Ollama 0.33.2, context 32768 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | disabled |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-20T14:00 → 2026-09-20T14:34 |

### Scores

**Leash 1.6** (uniform-v1, spec 0.1). Raw (no checks): 0.0. System (with escalation): not measured. Harness lift +1.6, escalation lift –.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 8 | 4 | 0 | 18 | 14.2% | 29.7% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 6 | 0 | 0 | 24 | 9.5% | 11.4% | 2.3 | L0 Supervised |
| multi-file | 16.7% | 45 | 10 | 0 | 0 | 35 | 12.5% | 7.9% | 6.0 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 14 | 3 | 0 | 28 | 19.5% | 17.9% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 4 | 0 | 0 | 26 | 5.3% | 11.4% | 1.3 | L0 Supervised |
| tdd | 16.7% | 30 | 3 | 1 | 0 | 26 | 3.5% | 16.7% | 0.0 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 3 | 27 | 0 | 0 | 3.5% | 96.5% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 6 | 24 | 0 | 0 | 9.5% | 90.5% | 0.0 | L0 Supervised |
| multi-file | 16.7% | 45 | 10 | 35 | 0 | 0 | 12.5% | 87.5% | 0.0 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 1 | 44 | 0 | 0 | 0.4% | 99.6% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 0 | 30 | 0 | 0 | 0.0% | 100.0% | 0.0 | L0 Supervised |
| tdd | 16.7% | 30 | 1 | 29 | 0 | 0 | 0.6% | 99.4% | 0.0 | L0 Supervised |

### Escalation

Escalation was disabled for this run.

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 9.8 | 2424.0 | 0.0% | 95.2% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 2/0/0/13 | 2/13/0/0 | – |
| add_method_single | prose-single-small | 0/0/0/15 | 0/15/0/0 | – |
| algorithm_single | prose-single-logic | 8/0/0/7 | 1/14/0/0 | – |
| bugfix_from_symptom | bugfix | 6/2/0/7 | 1/14/0/0 | – |
| bugfix_negative_fraction | bugfix | 2/2/0/11 | 2/13/0/0 | – |
| exact_new_file | exact-spec | 0/0/0/15 | 0/15/0/0 | – |
| exact_replace_function_file | exact-spec | 6/0/0/9 | 6/9/0/0 | – |
| feature_single_dates | prose-single-logic | 2/0/0/13 | 0/15/0/0 | – |
| multi_file_cli_flag | multi-file | 4/0/0/11 | 4/11/0/0 | – |
| rename_across_files | multi-file | 4/0/0/11 | 4/11/0/0 | – |
| small_edit_single | prose-single-small | 4/0/0/11 | 0/15/0/0 | – |
| split_evenly_signed | prose-single-logic | 4/3/0/8 | 0/15/0/0 | – |
| tdd_average_transaction | tdd | 1/0/0/14 | 0/15/0/0 | – |
| tdd_budget | tdd | 2/1/0/12 | 1/14/0/0 | – |

### Every silent wrong (197 across 189 trial(s))

**add_currency_field** trial 1 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 2
    import dataclasses
IndentationError: unexpected indent
```

**add_currency_field** trial 2 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_currency_field** trial 4 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_currency_field** trial 5 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 2
    import dataclasses
IndentationError: unexpected indent
```

**add_currency_field** trial 6 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_currency_field** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 2
    import dataclasses
IndentationError: unexpected indent
```

**add_currency_field** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 2
    import dataclasses
IndentationError: unexpected indent
```

**add_currency_field** trial 9 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 2
    import dataclasses
IndentationError: unexpected indent
```

**add_currency_field** trial 11 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_currency_field** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 2
    import dataclasses
IndentationError: unexpected indent
```

**add_currency_field** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 2
    import dataclasses
IndentationError: unexpected indent
```

**add_currency_field** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_currency_field** trial 15 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger import cli
  File "cli.py", line 1
    """ledger CLI: reads a CSV of date,category,amount,note,currency and prints a summary."""
IndentationError: unexpected indent
```

**add_method_single** trial 1 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_method_single** trial 2 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_method_single** trial 3 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_method_single** trial 4 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 2
    import dataclasses
IndentationError: unexpected indent
```

**add_method_single** trial 5 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_method_single** trial 6 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_method_single** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_method_single** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_method_single** trial 9 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_method_single** trial 10 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_method_single** trial 11 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_method_single** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_method_single** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_method_single** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**add_method_single** trial 15 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**algorithm_single** trial 1 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly, format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**algorithm_single** trial 2 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly, format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**algorithm_single** trial 3 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly, format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**algorithm_single** trial 4 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly, format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**algorithm_single** trial 5 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly, format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**algorithm_single** trial 6 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly, format_cents
  File "money.py", line 2
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**algorithm_single** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly, format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**algorithm_single** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly, format_cents
  File "money.py", line 2
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**algorithm_single** trial 10 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly, format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**algorithm_single** trial 11 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly, format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**algorithm_single** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly, format_cents
  File "money.py", line 2
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**algorithm_single** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly, format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**algorithm_single** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly, format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**algorithm_single** trial 15 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly, format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_from_symptom** trial 1 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_from_symptom** trial 2 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_from_symptom** trial 3 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_from_symptom** trial 4 - `unchecked` (snapshot), `checked`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 2
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

Grader output for checked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1700 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.002s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 5 - `unchecked` (snapshot), `checked`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

Grader output for checked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1700 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 6 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 2
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_from_symptom** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_from_symptom** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_from_symptom** trial 9 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_from_symptom** trial 10 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_from_symptom** trial 11 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_from_symptom** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_from_symptom** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_from_symptom** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_negative_fraction** trial 1 - `unchecked` (snapshot), `checked`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

Grader output for checked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 7, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: -1150 != -1250 : -12.50

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_negative_fraction** trial 2 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_negative_fraction** trial 3 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_negative_fraction** trial 4 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_negative_fraction** trial 5 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_negative_fraction** trial 6 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_negative_fraction** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_negative_fraction** trial 9 - `unchecked` (snapshot), `checked`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

Grader output for checked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 7, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1200 != -1200 : -12

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_negative_fraction** trial 11 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_negative_fraction** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_negative_fraction** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_negative_fraction** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**bugfix_negative_fraction** trial 15 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**exact_new_file** trial 1 - `unchecked` (snapshot)

```
-    """Shared constants."""
? ---
+ """Shared constants."""
  
-    DEFAULT_CURRENCY = "USD"
? ---
+ DEFAULT_CURRENCY = "USD"
-    CENTS_PER_UNIT = 100
? ---
+ CENTS_PER_UNIT = 100
-    ===END===


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**exact_new_file** trial 2 - `unchecked` (snapshot)

```
-    """Shared constants."""
? ---
+ """Shared constants."""
  
-    DEFAULT_CURRENCY = "USD"
? ---
+ DEFAULT_CURRENCY = "USD"
-    CENTS_PER_UNIT = 100
? ---
+ CENTS_PER_UNIT = 100
-    ===END===


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**exact_new_file** trial 3 - `unchecked` (snapshot)

```
-    """Shared constants."""
? ---
+ """Shared constants."""
  
-    DEFAULT_CURRENCY = "USD"
? ---
+ DEFAULT_CURRENCY = "USD"
-    CENTS_PER_UNIT = 100
? ---
+ CENTS_PER_UNIT = 100
-    ===END===


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**exact_new_file** trial 4 - `unchecked` (snapshot)

```
-    """Shared constants."""
? ---
+ """Shared constants."""
  
-    DEFAULT_CURRENCY = "USD"
? ---
+ DEFAULT_CURRENCY = "USD"
-    CENTS_PER_UNIT = 100
? ---
+ CENTS_PER_UNIT = 100
-    ===END===


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**exact_new_file** trial 5 - `unchecked` (snapshot)

```
-    """Shared constants."""
? ---
+ """Shared constants."""
  
-    DEFAULT_CURRENCY = "USD"
? ---
+ DEFAULT_CURRENCY = "USD"
-    CENTS_PER_UNIT = 100
? ---
+ CENTS_PER_UNIT = 100
-    ===END===


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**exact_new_file** trial 6 - `unchecked` (snapshot)

```
-    """Shared constants."""
? ---
+ """Shared constants."""
  
-    DEFAULT_CURRENCY = "USD"
? ---
+ DEFAULT_CURRENCY = "USD"
-    CENTS_PER_UNIT = 100
? ---
+ CENTS_PER_UNIT = 100
-    ===END===


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**exact_new_file** trial 7 - `unchecked` (snapshot)

```
-    """Shared constants."""
? ---
+ """Shared constants."""
  
-    DEFAULT_CURRENCY = "USD"
? ---
+ DEFAULT_CURRENCY = "USD"
-    CENTS_PER_UNIT = 100
? ---
+ CENTS_PER_UNIT = 100
-    ===END===


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**exact_new_file** trial 8 - `unchecked` (snapshot)

```
-    """Shared constants."""
? ---
+ """Shared constants."""
  
-    DEFAULT_CURRENCY = "USD"
? ---
+ DEFAULT_CURRENCY = "USD"
-    CENTS_PER_UNIT = 100
? ---
+ CENTS_PER_UNIT = 100
-    ===END===


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**exact_new_file** trial 9 - `unchecked` (snapshot)

```
-    """Shared constants."""
? ---
+ """Shared constants."""
  
-    DEFAULT_CURRENCY = "USD"
? ---
+ DEFAULT_CURRENCY = "USD"
-    CENTS_PER_UNIT = 100
? ---
+ CENTS_PER_UNIT = 100
-    ===END===


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**exact_new_file** trial 10 - `unchecked` (snapshot)

```
-    """Shared constants."""
? ---
+ """Shared constants."""
  
-    DEFAULT_CURRENCY = "USD"
? ---
+ DEFAULT_CURRENCY = "USD"
-    CENTS_PER_UNIT = 100
? ---
+ CENTS_PER_UNIT = 100
-    ===END===


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**exact_new_file** trial 11 - `unchecked` (snapshot)

```
-    """Shared constants."""
? ---
+ """Shared constants."""
  
-    DEFAULT_CURRENCY = "USD"
? ---
+ DEFAULT_CURRENCY = "USD"
-    CENTS_PER_UNIT = 100
? ---
+ CENTS_PER_UNIT = 100
-    ===END===


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**exact_new_file** trial 12 - `unchecked` (snapshot)

```
-    """Shared constants."""
? ---
+ """Shared constants."""
  
-    DEFAULT_CURRENCY = "USD"
? ---
+ DEFAULT_CURRENCY = "USD"
-    CENTS_PER_UNIT = 100
? ---
+ CENTS_PER_UNIT = 100
-    ===END===


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**exact_new_file** trial 13 - `unchecked` (snapshot)

```
-    """Shared constants."""
? ---
+ """Shared constants."""
  
-    DEFAULT_CURRENCY = "USD"
? ---
+ DEFAULT_CURRENCY = "USD"
-    CENTS_PER_UNIT = 100
? ---
+ CENTS_PER_UNIT = 100
-    ===END===


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**exact_new_file** trial 14 - `unchecked` (snapshot)

```
-    """Shared constants."""
? ---
+ """Shared constants."""
  
-    DEFAULT_CURRENCY = "USD"
? ---
+ DEFAULT_CURRENCY = "USD"
-    CENTS_PER_UNIT = 100
? ---
+ CENTS_PER_UNIT = 100
-    ===END===


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**exact_new_file** trial 15 - `unchecked` (snapshot)

```
-    """Shared constants."""
? ---
+ """Shared constants."""
  
-    DEFAULT_CURRENCY = "USD"
? ---
+ DEFAULT_CURRENCY = "USD"
-    CENTS_PER_UNIT = 100
? ---
+ CENTS_PER_UNIT = 100
-    ===END===


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**exact_replace_function_file** trial 1 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**exact_replace_function_file** trial 2 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**exact_replace_function_file** trial 3 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**exact_replace_function_file** trial 5 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**exact_replace_function_file** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**exact_replace_function_file** trial 9 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**exact_replace_function_file** trial 11 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**exact_replace_function_file** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**exact_replace_function_file** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**feature_single_dates** trial 1 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**feature_single_dates** trial 2 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**feature_single_dates** trial 3 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**feature_single_dates** trial 4 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 2
    import dataclasses
IndentationError: unexpected indent
```

**feature_single_dates** trial 5 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**feature_single_dates** trial 6 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**feature_single_dates** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**feature_single_dates** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**feature_single_dates** trial 9 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**feature_single_dates** trial 10 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**feature_single_dates** trial 11 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**feature_single_dates** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**feature_single_dates** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**feature_single_dates** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**feature_single_dates** trial 15 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**multi_file_cli_flag** trial 1 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 1
    """ledger CLI: reads a CSV of date,category,amount,note and prints a summary."""
IndentationError: unexpected indent
```

**multi_file_cli_flag** trial 2 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 1
    """ledger CLI: reads a CSV of date,category,amount,note and prints a summary."""
IndentationError: unexpected indent
```

**multi_file_cli_flag** trial 3 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 34
    ===END===
             ^
IndentationError: unindent does not match any outer indentation level
```

**multi_file_cli_flag** trial 5 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 1
    """ledger CLI: reads a CSV of date,category,amount,note and prints a summary."""
IndentationError: unexpected indent
```

**multi_file_cli_flag** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 35
    ===END===
             ^
IndentationError: unindent does not match any outer indentation level
```

**multi_file_cli_flag** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 1
    """ledger CLI: reads a CSV of date,category,amount,note and prints a summary."""
IndentationError: unexpected indent
```

**multi_file_cli_flag** trial 9 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 1
    """ledger CLI: reads a CSV of date,category,amount,note and prints a summary."""
IndentationError: unexpected indent
```

**multi_file_cli_flag** trial 11 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    ...existing content...
       ^^^^^^^^
SyntaxError: invalid syntax
```

**multi_file_cli_flag** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 1
    """ledger CLI: reads a CSV of date,category,amount,note and prints a summary."""
IndentationError: unexpected indent
```

**multi_file_cli_flag** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 2
    """ledger CLI: reads a CSV of date,category,amount,note and prints a summary."""
IndentationError: unexpected indent
```

**multi_file_cli_flag** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 1
    """ledger CLI: reads a CSV of date,category,amount,note and prints a summary."""
IndentationError: unexpected indent
```

**rename_across_files** trial 1 - `unchecked` (snapshot)

```
----------------------------------------------------------------------
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in test
    self.assertFalse(hasattr(Ledger, "add"))
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: True is not false

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 2 - `unchecked` (snapshot)

```
----------------------------------------------------------------------
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in test
    self.assertFalse(hasattr(Ledger, "add"))
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: True is not false

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 4 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**rename_across_files** trial 5 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 2
    import dataclasses
IndentationError: unexpected indent
```

**rename_across_files** trial 6 - `unchecked` (snapshot)

```
----------------------------------------------------------------------
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in test
    self.assertFalse(hasattr(Ledger, "add"))
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: True is not false

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 2
    import dataclasses
IndentationError: unexpected indent
```

**rename_across_files** trial 9 - `unchecked` (snapshot)

```
----------------------------------------------------------------------
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in test
    self.assertFalse(hasattr(Ledger, "add"))
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: True is not false

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 12 - `unchecked` (snapshot)

```
----------------------------------------------------------------------
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in test
    self.assertFalse(hasattr(Ledger, "add"))
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: True is not false

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 1
    import dataclasses
IndentationError: unexpected indent
```

**rename_across_files** trial 14 - `unchecked` (snapshot)

```
----------------------------------------------------------------------
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in test
    self.assertFalse(hasattr(Ledger, "add"))
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: True is not false

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 15 - `unchecked` (snapshot)

```
----------------------------------------------------------------------
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in test
    self.assertFalse(hasattr(Ledger, "add"))
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: True is not false

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**small_edit_single** trial 1 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**small_edit_single** trial 2 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**small_edit_single** trial 3 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**small_edit_single** trial 4 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**small_edit_single** trial 5 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**small_edit_single** trial 6 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 2
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**small_edit_single** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**small_edit_single** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**small_edit_single** trial 9 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**small_edit_single** trial 10 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**small_edit_single** trial 11 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 2
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**small_edit_single** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**small_edit_single** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**small_edit_single** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**small_edit_single** trial 15 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**split_evenly_signed** trial 1 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**split_evenly_signed** trial 2 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**split_evenly_signed** trial 3 - `unchecked` (snapshot), `checked`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [-33, -33, -34] != [-34, -33, -33]

First differing element 0:
-33
-34

- [-33, -33, -34]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 4 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**split_evenly_signed** trial 5 - `unchecked` (snapshot), `checked`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

Grader output for checked:

```
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [32, 33, 33] != [-34, -33, -33]

First differing element 0:
32
-34

- [32, 33, 33]
?   ^

+ [-34, -33, -33]
?  + ^  +    +


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 6 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**split_evenly_signed** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**split_evenly_signed** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**split_evenly_signed** trial 9 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**split_evenly_signed** trial 10 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**split_evenly_signed** trial 11 - `unchecked` (snapshot), `checked`

```
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [32, 33, 33] != [-34, -33, -33]

First differing element 0:
32
-34

- [32, 33, 33]
?   ^

+ [-34, -33, -33]
?  + ^  +    +


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**split_evenly_signed** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
  File "money.py", line 2
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**split_evenly_signed** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**split_evenly_signed** trial 15 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
  File "money.py", line 2
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**tdd_average_transaction** trial 1 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 2 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 3 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 4 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 5 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 6 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
  File "stats.py", line 1
    def average_transaction(ledger, category: str) -> float:
IndentationError: unexpected indent
```

**tdd_average_transaction** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
  File "stats.py", line 1
    from ledger.store import Ledger
IndentationError: unexpected indent
```

**tdd_average_transaction** trial 9 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
  File "stats.py", line 1
    from ledger.store import Ledger, Entry
IndentationError: unexpected indent
```

**tdd_average_transaction** trial 10 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 11 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 12 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 13 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 14 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 15 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_budget** trial 1 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
  File "budget.py", line 1
    from ledger.store import Ledger
IndentationError: unexpected indent
```

**tdd_budget** trial 2 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 3 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 5 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
  File "budget.py", line 2
    from ledger.store import Ledger
IndentationError: unexpected indent
```

**tdd_budget** trial 6 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
  File "budget.py", line 2
    from ledger import store
IndentationError: unexpected indent
```

**tdd_budget** trial 7 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 8 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 9 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 10 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 11 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 12 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 13 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 14 - `unchecked` (snapshot), `checked`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
  File "budget.py", line 1
    from ledger import store
IndentationError: unexpected indent
```

Grader output for checked:

```
  File "budget.py", line 12, in over_budget
    return {category: spent - limit for category, spent in category_spending.items() if spent > limits.get(category, 0)}
                              ^^^^^
NameError: name 'limit' is not defined. Did you mean: 'limits'?

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 15 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

## Limitations

- Small task set: every task currently uses the same Python fixture (ledger); results say nothing yet about other languages or larger codebases.
- Escalation is repair-only, with one cloud model per run (Gemini via the agy CLI by default, or Claude). TDD items are repaired with a single pass, not re-run red/green.
- Cloud models change behind the same name; escalation results are dated and go stale faster than local-model results.
- Scores are specific to the harness configuration named in each section and are not comparable across harness configurations.
