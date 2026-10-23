# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-20T08:31-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| deepseek-coder-v2:16b (Q4_0) | 9.2 | 7.2 | not measured | +2.0 | – | 210 | 0 |

## deepseek-coder-v2:16b (Q4_0)

|  |  |
|---|---|
| Model | deepseek-coder-v2:16b |
| Digest | 63fb193b3a9b4322 |
| Size / quantization | 15.7B / Q4_0 |
| Runtime | Ollama 0.33.2, context 163840 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | disabled |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-20T08:16 → 2026-09-20T08:31 |

### Scores

**Leash 9.2** (uniform-v1, spec 0.1). Raw (no checks): 7.2. System (with escalation): not measured. Harness lift +2.0, escalation lift –.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 0 | 30 | 0 | 0 | 0.0% | 100.0% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 17 | 0 | 0 | 28 | 25.1% | 7.9% | 11.9 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 17 | 28 | 0 | 0 | 25.1% | 74.9% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 0 | 0 | 0 | 30 | 0.0% | 11.4% | 0.0 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 0 | 30 | 0 | 0 | 0.0% | 100.0% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 16 | 29 | 0 | 0 | 23.2% | 76.8% | 0.0 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 17 | 28 | 0 | 0 | 25.1% | 74.9% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 0 | 30 | 0 | 0 | 0.0% | 100.0% | 0.0 | L0 Supervised |

### Escalation

Escalation was disabled for this run.

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 2.0 | 1092.0 | 0.0% | 50.0% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 1/0/0/14 | 1/14/0/0 | – |
| add_method_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | – |
| algorithm_single | prose-single-logic | 14/1/0/0 | 14/1/0/0 | – |
| bugfix_from_symptom | bugfix | 0/15/0/0 | 0/15/0/0 | – |
| bugfix_negative_fraction | bugfix | 0/15/0/0 | 0/15/0/0 | – |
| exact_new_file | exact-spec | 15/0/0/0 | 15/0/0/0 | – |
| exact_replace_function_file | exact-spec | 15/0/0/0 | 15/0/0/0 | – |
| feature_single_dates | prose-single-logic | 0/15/0/0 | 0/15/0/0 | – |
| multi_file_cli_flag | multi-file | 15/0/0/0 | 15/0/0/0 | – |
| rename_across_files | multi-file | 1/0/0/14 | 0/15/0/0 | – |
| small_edit_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | – |
| split_evenly_signed | prose-single-logic | 3/12/0/0 | 3/12/0/0 | – |
| tdd_average_transaction | tdd | 0/0/0/15 | 0/15/0/0 | – |
| tdd_budget | tdd | 0/0/0/15 | 0/15/0/0 | – |

### Every silent wrong (175 across 117 trial(s))

**add_currency_field** trial 1 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-d6oahpny/wt/ledger/store.py)
```

**add_currency_field** trial 2 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-l80ij_4y/wt/ledger/store.py)
```

**add_currency_field** trial 3 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-02ek9bg8/wt/ledger/store.py)
```

**add_currency_field** trial 4 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-dr378ipk/wt/ledger/store.py)
```

**add_currency_field** trial 5 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 32, in test_5_columns_currency
    self.assertEqual(ledger.entries[0].currency, "EUR")
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'USD' != 'EUR'
- USD
+ EUR


----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)
```

**add_currency_field** trial 6 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-ie8yhe0s/wt/ledger/store.py)
```

**add_currency_field** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 32, in test_5_columns_currency
    self.assertEqual(ledger.entries[0].currency, "EUR")
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'USD' != 'EUR'
- USD
+ EUR


----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)
```

**add_currency_field** trial 8 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-bylus9z5/wt/ledger/store.py)
```

**add_currency_field** trial 9 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-nvwk2evz/wt/ledger/store.py)
```

**add_currency_field** trial 10 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 32, in test_5_columns_currency
    self.assertEqual(ledger.entries[0].currency, "EUR")
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'USD' != 'EUR'
- USD
+ EUR


----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)
```

**add_currency_field** trial 11 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 32, in test_5_columns_currency
    self.assertEqual(ledger.entries[0].currency, "EUR")
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'USD' != 'EUR'
- USD
+ EUR


----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)
```

**add_currency_field** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 32, in test_5_columns_currency
    self.assertEqual(ledger.entries[0].currency, "EUR")
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'USD' != 'EUR'
- USD
+ EUR


----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)
```

**add_currency_field** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 32, in test_5_columns_currency
    self.assertEqual(ledger.entries[0].currency, "EUR")
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'USD' != 'EUR'
- USD
+ EUR


----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)
```

**add_currency_field** trial 15 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-mg89caq6/wt/ledger/store.py)
```

**algorithm_single** trial 14 - `unchecked` (snapshot), `checked`

```
  File "_leash_grader.py", line 8, in test
    self.assertEqual(split_evenly(2, 5), [1, 1, 0, 0, 0])
                     ~~~~~~~~~~~~^^^^^^
  File "money.py", line 24, in split_evenly
    raise ValueError("Not enough cents to split")
ValueError: Not enough cents to split

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

**bugfix_from_symptom** trial 1 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1205 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 2 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1205 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 3 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1205 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 4 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1205 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 5 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1205 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 6 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1205 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 7 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1205 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 8 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1205 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 9 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1205 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 10 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1205 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 11 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1205 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 12 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1205 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 13 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1205 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 14 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1205 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_from_symptom** trial 15 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1205 != 1250 : 12.5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_negative_fraction** trial 1 - `unchecked` (snapshot), `checked`

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

**bugfix_negative_fraction** trial 2 - `unchecked` (snapshot), `checked`

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

**bugfix_negative_fraction** trial 3 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 7, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: -6200 != -1250 : -12.50

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_negative_fraction** trial 4 - `unchecked` (snapshot), `checked`

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

**bugfix_negative_fraction** trial 5 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 7, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 3800 != -1250 : -12.50

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_negative_fraction** trial 6 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 7, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 3800 != -1250 : -12.50

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_negative_fraction** trial 7 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 7, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1150 != -1250 : -12.50

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_negative_fraction** trial 8 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 7, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: -6200 != -1250 : -12.50

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_negative_fraction** trial 9 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 7, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1250 != -1250 : -12.50

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_negative_fraction** trial 10 - `unchecked` (snapshot), `checked`

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

**bugfix_negative_fraction** trial 11 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 7, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1300 != -1250 : -12.50

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_negative_fraction** trial 12 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 7, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: -6200 != -1250 : -12.50

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_negative_fraction** trial 13 - `unchecked` (snapshot), `checked`

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

**bugfix_negative_fraction** trial 14 - `unchecked` (snapshot), `checked`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 7, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1150 != 1250 : 12.50

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_negative_fraction** trial 15 - `unchecked` (snapshot), `checked`

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

**feature_single_dates** trial 1 - `unchecked` (snapshot), `checked`

```
AssertionError: Lists differ: ['2026-03', '2025-12', '2026-01'] != ['2025-12', '2026-01', '2026-03']

First differing element 0:
'2026-03'
'2025-12'

- ['2026-03', '2025-12', '2026-01']
+ ['2025-12', '2026-01', '2026-03']

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**feature_single_dates** trial 2 - `unchecked` (snapshot), `checked`

```
AssertionError: Lists differ: ['2026-03', '2025-12', '2026-01'] != ['2025-12', '2026-01', '2026-03']

First differing element 0:
'2026-03'
'2025-12'

- ['2026-03', '2025-12', '2026-01']
+ ['2025-12', '2026-01', '2026-03']

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**feature_single_dates** trial 3 - `unchecked` (snapshot), `checked`

```
AssertionError: Lists differ: ['2026-03', '2025-12', '2026-01'] != ['2025-12', '2026-01', '2026-03']

First differing element 0:
'2026-03'
'2025-12'

- ['2026-03', '2025-12', '2026-01']
+ ['2025-12', '2026-01', '2026-03']

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**feature_single_dates** trial 4 - `unchecked` (snapshot), `checked`

```
AssertionError: Lists differ: ['2026-03', '2025-12', '2026-01'] != ['2025-12', '2026-01', '2026-03']

First differing element 0:
'2026-03'
'2025-12'

- ['2026-03', '2025-12', '2026-01']
+ ['2025-12', '2026-01', '2026-03']

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**feature_single_dates** trial 5 - `unchecked` (snapshot), `checked`

```
AssertionError: Lists differ: ['2026-03', '2025-12', '2026-01'] != ['2025-12', '2026-01', '2026-03']

First differing element 0:
'2026-03'
'2025-12'

- ['2026-03', '2025-12', '2026-01']
+ ['2025-12', '2026-01', '2026-03']

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**feature_single_dates** trial 6 - `unchecked` (snapshot), `checked`

```
AssertionError: Lists differ: ['2026-03', '2025-12', '2026-01'] != ['2025-12', '2026-01', '2026-03']

First differing element 0:
'2026-03'
'2025-12'

- ['2026-03', '2025-12', '2026-01']
+ ['2025-12', '2026-01', '2026-03']

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**feature_single_dates** trial 7 - `unchecked` (snapshot), `checked`

```
AssertionError: Lists differ: ['2026-03', '2025-12', '2026-01'] != ['2025-12', '2026-01', '2026-03']

First differing element 0:
'2026-03'
'2025-12'

- ['2026-03', '2025-12', '2026-01']
+ ['2025-12', '2026-01', '2026-03']

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**feature_single_dates** trial 8 - `unchecked` (snapshot), `checked`

```
AssertionError: Lists differ: ['2026-03', '2025-12', '2026-01'] != ['2025-12', '2026-01', '2026-03']

First differing element 0:
'2026-03'
'2025-12'

- ['2026-03', '2025-12', '2026-01']
+ ['2025-12', '2026-01', '2026-03']

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**feature_single_dates** trial 9 - `unchecked` (snapshot), `checked`

```
AssertionError: Lists differ: ['2026-03', '2025-12', '2026-01'] != ['2025-12', '2026-01', '2026-03']

First differing element 0:
'2026-03'
'2025-12'

- ['2026-03', '2025-12', '2026-01']
+ ['2025-12', '2026-01', '2026-03']

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**feature_single_dates** trial 10 - `unchecked` (snapshot), `checked`

```
AssertionError: Lists differ: ['2026-03', '2025-12', '2026-01'] != ['2025-12', '2026-01', '2026-03']

First differing element 0:
'2026-03'
'2025-12'

- ['2026-03', '2025-12', '2026-01']
+ ['2025-12', '2026-01', '2026-03']

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**feature_single_dates** trial 11 - `unchecked` (snapshot), `checked`

```
AssertionError: Lists differ: ['2026-03', '2025-12', '2026-01'] != ['2025-12', '2026-01', '2026-03']

First differing element 0:
'2026-03'
'2025-12'

- ['2026-03', '2025-12', '2026-01']
+ ['2025-12', '2026-01', '2026-03']

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**feature_single_dates** trial 12 - `unchecked` (snapshot), `checked`

```
AssertionError: Lists differ: ['2026-03', '2025-12', '2026-01'] != ['2025-12', '2026-01', '2026-03']

First differing element 0:
'2026-03'
'2025-12'

- ['2026-03', '2025-12', '2026-01']
+ ['2025-12', '2026-01', '2026-03']

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**feature_single_dates** trial 13 - `unchecked` (snapshot), `checked`

```
AssertionError: Lists differ: ['2026-03', '2025-12', '2026-01'] != ['2025-12', '2026-01', '2026-03']

First differing element 0:
'2026-03'
'2025-12'

- ['2026-03', '2025-12', '2026-01']
+ ['2025-12', '2026-01', '2026-03']

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**feature_single_dates** trial 14 - `unchecked` (snapshot), `checked`

```
AssertionError: Lists differ: ['2026-03', '2025-12', '2026-01'] != ['2025-12', '2026-01', '2026-03']

First differing element 0:
'2026-03'
'2025-12'

- ['2026-03', '2025-12', '2026-01']
+ ['2025-12', '2026-01', '2026-03']

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**feature_single_dates** trial 15 - `unchecked` (snapshot), `checked`

```
AssertionError: Lists differ: ['2026-03', '2025-12', '2026-01'] != ['2025-12', '2026-01', '2026-03']

First differing element 0:
'2026-03'
'2025-12'

- ['2026-03', '2025-12', '2026-01']
+ ['2025-12', '2026-01', '2026-03']

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 1 - `unchecked` (snapshot)

```
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-gmjiqn2f/wt/ledger/store.py)
```

**rename_across_files** trial 2 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 3 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 4 - `unchecked` (snapshot)

```
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-bwq0povd/wt/ledger/store.py)
```

**rename_across_files** trial 5 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 6 - `unchecked` (snapshot)

```
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-cyhen23o/wt/ledger/store.py)
```

**rename_across_files** trial 7 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 8 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 9 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 10 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 11 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 12 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 13 - `unchecked` (snapshot)

```
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-3gtkcwd1/wt/ledger/store.py)
```

**rename_across_files** trial 14 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 15 - `unchecked` (snapshot)

```
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-o9ldemnk/wt/ledger/store.py)
```

**split_evenly_signed** trial 2 - `unchecked` (snapshot), `checked`

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

**split_evenly_signed** trial 4 - `unchecked` (snapshot), `checked`

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

**split_evenly_signed** trial 5 - `unchecked` (snapshot), `checked`

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

**split_evenly_signed** trial 6 - `unchecked` (snapshot), `checked`

```
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [-35, -35, -34] != [-34, -33, -33]

First differing element 0:
-35
-34

- [-35, -35, -34]
?    ^    ^    ^

+ [-34, -33, -33]
?    ^    ^    ^


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 7 - `unchecked` (snapshot), `checked`

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

**split_evenly_signed** trial 9 - `unchecked` (snapshot), `checked`

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

**split_evenly_signed** trial 10 - `unchecked` (snapshot), `checked`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [33, 33, 34] != [-34, -33, -33]

First differing element 0:
33
-34

- [33, 33, 34]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 12 - `unchecked` (snapshot), `checked`

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

**split_evenly_signed** trial 13 - `unchecked` (snapshot), `checked`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [33, 33, 34] != [-34, -33, -33]

First differing element 0:
33
-34

- [33, 33, 34]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 14 - `unchecked` (snapshot), `checked`

```
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [-35, -35, -34] != [-34, -33, -33]

First differing element 0:
-35
-34

- [-35, -35, -34]
?    ^    ^    ^

+ [-34, -33, -33]
?    ^    ^    ^


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 15 - `unchecked` (snapshot), `checked`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [33, 33, 34] != [-34, -33, -33]

First differing element 0:
33
-34

- [33, 33, 34]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 1 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-grade-xnimzt_t/wt/ledger/stats.py)
```

**tdd_average_transaction** trial 2 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-grade-3c3wfpst/wt/ledger/stats.py)
```

**tdd_average_transaction** trial 3 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 32, in test_average_transaction_empty_ledger
    ledger.average_transaction("Food")
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Ledger' object has no attribute 'average_transaction'

----------------------------------------------------------------------
Ran 4 tests in 0.000s

FAILED (errors=2)
```

**tdd_average_transaction** trial 4 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 5 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-grade-w4aalter/wt/ledger/stats.py)
```

**tdd_average_transaction** trial 6 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 11, in test_average_transaction
    ledger.average_transaction("nonexistent_category")
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Ledger' object has no attribute 'average_transaction'

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 7 - `unchecked` (snapshot)

```
    module = self._get_module_from_name(name)
  File "loader.py", line 374, in _get_module_from_name
    __import__(name)
    ~~~~~~~~~~^^^^^^
  File "test_stats.py", line 1, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 8 - `unchecked` (snapshot)

```
    module = self._get_module_from_name(name)
  File "loader.py", line 374, in _get_module_from_name
    __import__(name)
    ~~~~~~~~~~^^^^^^
  File "test_stats.py", line 1, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 9 - `unchecked` (snapshot)

```
    module = self._get_module_from_name(name)
  File "loader.py", line 374, in _get_module_from_name
    __import__(name)
    ~~~~~~~~~~^^^^^^
  File "test_stats.py", line 1, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 10 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-grade-6kr8ijeo/wt/ledger/stats.py)
```

**tdd_average_transaction** trial 11 - `unchecked` (snapshot)

```
    module = self._get_module_from_name(name)
  File "loader.py", line 374, in _get_module_from_name
    __import__(name)
    ~~~~~~~~~~^^^^^^
  File "test_stats.py", line 1, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 12 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-grade-tl7rplfz/wt/ledger/stats.py)
```

**tdd_average_transaction** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-grade-5vvfz2uf/wt/ledger/stats.py)
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
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': -550, 'rent': -1000} != {'food': 50}
- {'food': -550, 'rent': -1000}
+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 2 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 11, in test
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {} != {'food': 50}
- {}
+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 3 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 23, in test_over_budget
    self.assertEqual(result, expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
AssertionError: {'Food': 1500} != {'Food': -500}
- {'Food': 1500}
?          ^

+ {'Food': -500}
?          ^


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 4 - `unchecked` (snapshot)

```
  File "test_budget.py", line 21, in test_over_budget_no_limit
    self.assertEqual(result, {"Food": 1000})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'Food': 900} != {'Food': 1000}
- {'Food': 900}
?          ^

+ {'Food': 1000}
?          ^^


----------------------------------------------------------------------
Ran 8 tests in 0.001s

FAILED (failures=3)
```

**tdd_budget** trial 5 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 11, in test
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {} != {'food': 50}
- {}
+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 6 - `unchecked` (snapshot)

```
AssertionError: {'Food': 500, 'Entertainment': 100} != {'Food': 1500, 'Rent': 1000, 'Entertainment': 200}
- {'Entertainment': 100, 'Food': 500}
?                   ^

+ {'Entertainment': 200, 'Food': 1500, 'Rent': 1000}
?                   ^            +   ++++++++++++++


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 7 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 11, in test
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {} != {'food': 50}
- {}
+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 8 - `unchecked` (snapshot)

```
  File "test_budget.py", line 43, in test_over_budget_zero_limit
    self.assertEqual(result, expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
AssertionError: {'Food': 1000, 'Travel': 2000} != {'Food': -1000}
- {'Food': 1000, 'Travel': 2000}
+ {'Food': -1000}

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (failures=3)
```

**tdd_budget** trial 9 - `unchecked` (snapshot)

```
  File "test_budget.py", line 13, in test_over_budget
    self.assertEqual(result, {"Rent": -200})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'Food': 500, 'Travel': 100} != {'Rent': -200}
- {'Food': 500, 'Travel': 100}
+ {'Rent': -200}

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 10 - `unchecked` (snapshot)

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': 550} != {'food': 50}
- {'food': 550}
?          -

+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 11 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 13, in test_over_budget
    self.assertEqual(result, {"Food": -1500})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'Food': 500} != {'Food': -1500}
- {'Food': 500}
+ {'Food': -1500}
?          ++


----------------------------------------------------------------------
Ran 6 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 13, in test_over_budget
    self.assertEqual(result, {"Food": -1000})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'Food': 1000} != {'Food': -1000}
- {'Food': 1000}
+ {'Food': -1000}
?          +


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 13, in test_over_budget
    self.assertEqual(result, {"Food": -1500})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'Food': 500} != {'Food': -1500}
- {'Food': 500}
+ {'Food': -1500}
?          ++


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 21, in test_over_budget
    self.assertEqual(result, expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
AssertionError: {'Food': 500} != {'Food': -500}
- {'Food': 500}
+ {'Food': -500}
?          +


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 15 - `unchecked` (snapshot)

```
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'Food': 500, 'Travel': 100} != {'Food': 1000, 'Rent': 1000}
- {'Food': 500, 'Travel': 100}
?          ^     ^^^^ ^

+ {'Food': 1000, 'Rent': 1000}
?          ^^     ^ ^^      +


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

## Limitations

- Small task set: every task currently uses the same Python fixture (ledger); results say nothing yet about other languages or larger codebases.
- Escalation is repair-only, with one cloud model per run (Gemini via the agy CLI by default, or Claude). TDD items are repaired with a single pass, not re-run red/green.
- Cloud models change behind the same name; escalation results are dated and go stale faster than local-model results.
- Scores are specific to the harness configuration named in each section and are not comparable across harness configurations.
