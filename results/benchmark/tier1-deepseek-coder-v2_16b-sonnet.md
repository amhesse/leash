# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-20T09:30-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| deepseek-coder-v2:16b (Q4_0) + claude:claude-sonnet-5 | 9.2 | 7.2 | 14.5 | +2.0 | +5.3 | 210 | 0 |

## deepseek-coder-v2:16b (Q4_0) + claude:claude-sonnet-5

|  |  |
|---|---|
| Model | deepseek-coder-v2:16b |
| Digest | 63fb193b3a9b4322 |
| Size / quantization | 15.7B / Q4_0 |
| Runtime | Ollama 0.33.2, context 163840 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | claude:claude-sonnet-5 via claude CLI 2.1.275 (Claude Code) |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-20T08:31 → 2026-09-20T09:29 |

### Scores

**Leash 9.2** (uniform-v1, spec 0.1). Raw (no checks): 7.2. System (with escalation): 14.5. Harness lift +2.0, escalation lift +5.3.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 0 | 29 | 0 | 1 | 0.0% | 99.4% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 17 | 0 | 0 | 28 | 25.1% | 7.9% | 11.9 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 18 | 27 | 0 | 0 | 27.0% | 73.0% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 0 | 0 | 1 | 29 | 0.0% | 11.4% | 0.0 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 0 | 30 | 0 | 0 | 0.0% | 100.0% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 17 | 28 | 0 | 0 | 25.1% | 74.9% | 0.0 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 18 | 27 | 0 | 0 | 27.0% | 73.0% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 1 | 29 | 0 | 0 | 0.6% | 99.4% | 0.0 | L0 Supervised |

### Escalated - parked work repaired by the cloud model

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 1 | 29 | 0 | 0 | 0.6% | 99.4% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 18 | 27 | 0 | 0 | 27.0% | 73.0% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 19 | 6 | 0 | 5 | 45.5% | 37.3% | 0.0 | L0 Supervised |

### Escalation

| Needed | Run | Skipped | Failed | Rescue rate | Cloud silent wrong | Median cloud s | Median cloud tokens |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 59 | 59 | 0 | 0 | 81.4% | 6 | 33.1 | 369555 |

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 2.0 | 1112.0 | 1.0% | 50.9% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 2/0/0/13 | 2/13/0/0 | 15/0/0/0 |
| add_method_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| algorithm_single | prose-single-logic | 14/1/0/0 | 14/1/0/0 | 14/1/0/0 |
| bugfix_from_symptom | bugfix | 0/15/0/0 | 0/15/0/0 | 0/15/0/0 |
| bugfix_negative_fraction | bugfix | 0/14/0/1 | 0/15/0/0 | 1/14/0/0 |
| exact_new_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| exact_replace_function_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| feature_single_dates | prose-single-logic | 3/12/0/0 | 3/12/0/0 | 3/12/0/0 |
| multi_file_cli_flag | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| rename_across_files | multi-file | 0/0/0/15 | 0/15/0/0 | 15/0/0/0 |
| small_edit_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| split_evenly_signed | prose-single-logic | 1/14/0/0 | 1/14/0/0 | 1/14/0/0 |
| tdd_average_transaction | tdd | 0/0/0/15 | 0/15/0/0 | 14/0/0/1 |
| tdd_budget | tdd | 0/0/1/14 | 1/14/0/0 | 5/6/0/4 |

### Every silent wrong (232 across 114 trial(s))

**add_currency_field** trial 1 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-hue8dblz/wt/ledger/store.py)
```

**add_currency_field** trial 3 - `unchecked` (snapshot)

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

**add_currency_field** trial 4 - `unchecked` (snapshot)

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
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-1a_nre69/wt/ledger/store.py)
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
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-quezhtgl/wt/ledger/store.py)
```

**add_currency_field** trial 9 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-0ui2x7n7/wt/ledger/store.py)
```

**add_currency_field** trial 10 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-e1rb4d42/wt/ledger/store.py)
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

**add_currency_field** trial 12 - `unchecked` (snapshot)

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
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-8pespoof/wt/ledger/store.py)
```

**algorithm_single** trial 14 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly(2, 5), [1, 1, 0, 0, 0])
                     ~~~~~~~~~~~~^^^^^^
  File "money.py", line 24, in split_evenly
    raise ValueError("Cents must be at least as large as parts")
ValueError: Cents must be at least as large as parts

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

**bugfix_from_symptom** trial 1 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_from_symptom** trial 2 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_from_symptom** trial 3 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_from_symptom** trial 4 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_from_symptom** trial 5 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_from_symptom** trial 6 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_from_symptom** trial 7 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_from_symptom** trial 8 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_from_symptom** trial 9 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_from_symptom** trial 10 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_from_symptom** trial 11 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_from_symptom** trial 12 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_from_symptom** trial 13 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_from_symptom** trial 14 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_from_symptom** trial 15 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 1 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 797
    return int(whole) *
                       ^
SyntaxError: invalid syntax
```

**bugfix_negative_fraction** trial 2 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 3 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 4 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 5 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 6 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 7 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 8 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 9 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 10 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 11 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 12 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 13 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 14 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 15 - `unchecked` (snapshot), `checked`, `escalated`

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

**feature_single_dates** trial 1 - `unchecked` (snapshot), `checked`, `escalated`

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

**feature_single_dates** trial 2 - `unchecked` (snapshot), `checked`, `escalated`

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

**feature_single_dates** trial 3 - `unchecked` (snapshot), `checked`, `escalated`

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

**feature_single_dates** trial 4 - `unchecked` (snapshot), `checked`, `escalated`

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

**feature_single_dates** trial 5 - `unchecked` (snapshot), `checked`, `escalated`

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

**feature_single_dates** trial 6 - `unchecked` (snapshot), `checked`, `escalated`

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

**feature_single_dates** trial 7 - `unchecked` (snapshot), `checked`, `escalated`

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

**feature_single_dates** trial 9 - `unchecked` (snapshot), `checked`, `escalated`

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

**feature_single_dates** trial 11 - `unchecked` (snapshot), `checked`, `escalated`

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

**feature_single_dates** trial 12 - `unchecked` (snapshot), `checked`, `escalated`

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

**feature_single_dates** trial 13 - `unchecked` (snapshot), `checked`, `escalated`

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

**feature_single_dates** trial 15 - `unchecked` (snapshot), `checked`, `escalated`

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

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 2 - `unchecked` (snapshot)

```
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-vg73bk01/wt/ledger/store.py)
```

**rename_across_files** trial 3 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 4 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 5 - `unchecked` (snapshot)

```
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-gr1a5r_z/wt/ledger/store.py)
```

**rename_across_files** trial 6 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 7 - `unchecked` (snapshot)

```
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-hz9ncsm6/wt/ledger/store.py)
```

**rename_across_files** trial 8 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 9 - `unchecked` (snapshot)

```
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-w3r8zg40/wt/ledger/store.py)
```

**rename_across_files** trial 10 - `unchecked` (snapshot)

```
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-gimvglfv/wt/ledger/store.py)
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

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
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
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-fnefgy53/wt/ledger/store.py)
```

**split_evenly_signed** trial 1 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 2 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 3 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 4 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 5 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 6 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 7 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 8 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 9 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 10 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 11 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 12 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 14 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 15 - `unchecked` (snapshot), `checked`, `escalated`

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
  File "stats.py", line 2, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'
```

**tdd_average_transaction** trial 2 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 3 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 4 - `unchecked` (snapshot)

```
    module = self._get_module_from_name(name)
  File "loader.py", line 374, in _get_module_from_name
    __import__(name)
    ~~~~~~~~~~^^^^^^
  File "test_stats.py", line 5, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 5 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 6 - `unchecked` (snapshot)

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
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
  File "stats.py", line 2, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'
```

**tdd_average_transaction** trial 9 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 10 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 13 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 11, in test_average_transaction
    ledger.average_transaction("unknown_category")
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Ledger' object has no attribute 'average_transaction'

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 15 - `unchecked` (snapshot)

```
  File "test_stats.py", line 47, in test_average_transaction_zero_spending
    self.assertEqual(ledger.average_transaction("Food"), 1000.0)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Ledger' object has no attribute 'average_transaction'

----------------------------------------------------------------------
Ran 14 tests in 0.001s

FAILED (errors=12)
```

**tdd_budget** trial 1 - `unchecked` (branch_tip), `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

Grader output for escalated:

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': -550} != {'food': 50}
- {'food': -550}
?          --

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
  File "test_budget.py", line 20, in test_over_budget
    self.assertEqual(result, {'food': -1500})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': 1400, 'travel': 1500} != {'food': -1500}
- {'food': 1400, 'travel': 1500}
+ {'food': -1500}

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 5 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

```
    module = self._get_module_from_name(name)
  File "loader.py", line 374, in _get_module_from_name
    __import__(name)
    ~~~~~~~~~~^^^^^^
  File "test_budget.py", line 1, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

Grader output for escalated:

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': 550, 'rent': 1000} != {'food': 50}
- {'food': 550, 'rent': 1000}
+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 6 - `unchecked` (snapshot)

```
  File "test_budget.py", line 27, in test_over_budget_zero_limit
    self.assertEqual(result, {"Food": -1000})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'Food': 1000} != {'Food': -1000}
- {'Food': 1000}
+ {'Food': -1000}
?          +


----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (failures=4)
```

**tdd_budget** trial 7 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 8 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

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

Grader output for escalated:

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

**tdd_budget** trial 9 - `unchecked` (snapshot)

```
    self.assertEqual(result, expected_result)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {} != {'Rent': 500, 'Clothing': 500, 'Entertainment': 300, 'Travel': 0}
- {}
+ {'Clothing': 500, 'Entertainment': 300, 'Rent': 500, 'Travel': 0}

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 10 - `unchecked` (snapshot), `escalated`

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

**tdd_budget** trial 11 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

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

Grader output for escalated:

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': -550} != {'food': 50}
- {'food': -550}
?          --

+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 12 - `unchecked` (snapshot)

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

**tdd_budget** trial 13 - `unchecked` (snapshot)

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

**tdd_budget** trial 14 - `unchecked` (snapshot)

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

**tdd_budget** trial 15 - `unchecked` (snapshot), `escalated`

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

## Limitations

- Small task set: every task currently uses the same Python fixture (ledger); results say nothing yet about other languages or larger codebases.
- Escalation is repair-only, with one cloud model per run (Gemini via the agy CLI by default, or Claude). TDD items are repaired with a single pass, not re-run red/green.
- Cloud models change behind the same name; escalation results are dated and go stale faster than local-model results.
- Scores are specific to the harness configuration named in each section and are not comparable across harness configurations.
