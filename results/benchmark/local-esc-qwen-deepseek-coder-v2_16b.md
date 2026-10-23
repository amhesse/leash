# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-23T04:12-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| deepseek-coder-v2:16b (Q4_0) + ollama:qwen3.8:27b | 8.2 | 7.2 | 9.9 | +1.0 | +1.7 | 210 | 0 |

## deepseek-coder-v2:16b (Q4_0) + ollama:qwen3.8:27b

|  |  |
|---|---|
| Model | deepseek-coder-v2:16b |
| Digest | 63fb193b3a9b4322 |
| Size / quantization | 15.7B / Q4_0 |
| Runtime | Ollama 0.33.2, context 163840 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | ollama:qwen3.8:27b (local, forge lite backend) |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-23T00:37 → 2026-09-23T04:09 |

### Scores

**Leash 8.2** (uniform-v1, spec 0.1). Raw (no checks): 7.2. System (with escalation): 9.9. Harness lift +1.0, escalation lift +1.7.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 0 | 29 | 0 | 1 | 0.0% | 99.4% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 26 | 0 | 4 | 0 | 70.3% | 11.4% | 17.1 | L0 Supervised |
| multi-file | 16.7% | 45 | 15 | 0 | 0 | 30 | 21.4% | 7.9% | 10.2 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 18 | 27 | 0 | 0 | 27.0% | 73.0% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 0 | 0 | 0 | 30 | 0.0% | 11.4% | 0.0 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 0 | 30 | 0 | 0 | 0.0% | 100.0% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 15 | 30 | 0 | 0 | 21.4% | 78.6% | 0.0 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 18 | 27 | 0 | 0 | 27.0% | 73.0% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 0 | 30 | 0 | 0 | 0.0% | 100.0% | 0.0 | L0 Supervised |

### Escalated - parked work repaired by the cloud model

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 0 | 29 | 0 | 1 | 0.0% | 99.4% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 38 | 1 | 0 | 6 | 71.2% | 11.6% | 16.3 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 18 | 27 | 0 | 0 | 27.0% | 73.0% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 25 | 2 | 0 | 3 | 66.4% | 21.3% | 0.0 | L0 Supervised |

### Escalation

| Needed | Run | Skipped | Failed | Rescue rate | Cloud silent wrong | Median cloud s | Median cloud tokens |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 65 | 65 | 0 | 0 | 80.0% | 3 | 108.4 | 6243 |

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 3.4 | 1079.5 | 4.3% | 52.1% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 0/0/0/15 | 0/15/0/0 | 8/1/0/6 |
| add_method_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| algorithm_single | prose-single-logic | 14/1/0/0 | 14/1/0/0 | 14/1/0/0 |
| bugfix_from_symptom | bugfix | 0/15/0/0 | 0/15/0/0 | 0/15/0/0 |
| bugfix_negative_fraction | bugfix | 0/14/0/1 | 0/15/0/0 | 0/14/0/1 |
| exact_new_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| exact_replace_function_file | exact-spec | 11/0/4/0 | 15/0/0/0 | 15/0/0/0 |
| feature_single_dates | prose-single-logic | 2/13/0/0 | 2/13/0/0 | 2/13/0/0 |
| multi_file_cli_flag | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| rename_across_files | multi-file | 0/0/0/15 | 0/15/0/0 | 15/0/0/0 |
| small_edit_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| split_evenly_signed | prose-single-logic | 2/13/0/0 | 2/13/0/0 | 2/13/0/0 |
| tdd_average_transaction | tdd | 0/0/0/15 | 0/15/0/0 | 13/1/0/1 |
| tdd_budget | tdd | 0/0/0/15 | 0/15/0/0 | 12/1/0/2 |

### Every silent wrong (232 across 117 trial(s))

**add_currency_field** trial 1 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-0dx8fhs_/wt/ledger/store.py)
```

**add_currency_field** trial 2 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-s7yha_bp/wt/ledger/store.py)
```

**add_currency_field** trial 3 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-1vxw6162/wt/ledger/store.py)
```

**add_currency_field** trial 4 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-fm6_lre1/wt/ledger/store.py)
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
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-sx4ismwa/wt/ledger/store.py)
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
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-7uoqc53x/wt/ledger/store.py)
```

**add_currency_field** trial 9 - `unchecked` (snapshot)

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

**add_currency_field** trial 12 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-5219pbac/wt/ledger/store.py)
```

**add_currency_field** trial 13 - `unchecked` (snapshot)

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-8tip_gom/wt/ledger/store.py)
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

**add_currency_field** trial 15 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

```
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-wws38j0a/wt/ledger/store.py)
```

Grader output for escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 17, in test_default
    self.assertEqual(Entry.__dataclass_fields__["currency"].default, "USD")
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: type object 'Entry' has no attribute '__dataclass_fields__'

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (errors=1)
```

**algorithm_single** trial 15 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 1 - `unchecked` (snapshot), `checked`, `escalated`

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

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 696
    if
      ^
SyntaxError: invalid syntax
```

Grader output for checked, escalated:

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
AssertionError: 1150 != -1250 : -12.50

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_negative_fraction** trial 7 - `unchecked` (snapshot), `checked`, `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 698
    return int(whole) * 100 + int(frac) if whole and frac else int(
                                                                  ^
SyntaxError: '(' was never closed
```

Grader output for checked, escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 7, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: -120 != -1250 : -12.50

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
AssertionError: 1150 != -1250 : -12.50

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
AssertionError: -1150 != -1250 : -12.50

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
AssertionError: -1150 != -1250 : -12.50

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
AssertionError: -6200 != -1250 : -12.50

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

**bugfix_negative_fraction** trial 15 - `unchecked` (snapshot)

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

**feature_single_dates** trial 8 - `unchecked` (snapshot), `checked`, `escalated`

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

**feature_single_dates** trial 14 - `unchecked` (snapshot), `checked`, `escalated`

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
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-_mj2cyd2/wt/ledger/store.py)
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
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-sdlm3squ/wt/ledger/store.py)
```

**rename_across_files** trial 6 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 7 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 8 - `unchecked` (snapshot)

```
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-xojj8a6o/wt/ledger/store.py)
```

**rename_across_files** trial 9 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 10 - `unchecked` (snapshot)

```
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-5u0vazrt/wt/ledger/store.py)
```

**rename_across_files** trial 11 - `unchecked` (snapshot)

```
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-wbt22afo/wt/ledger/store.py)
```

**rename_across_files** trial 12 - `unchecked` (snapshot)

```
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-m_jx1wet/wt/ledger/store.py)
```

**rename_across_files** trial 13 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 14 - `unchecked` (snapshot)

```
    from ledger.store import Entry, Ledger
  File "store.py", line 8, in <module>
    from .report import summary
  File "report.py", line 2, in <module>
    from .store import Ledger
ImportError: cannot import name 'Ledger' from partially initialized module 'ledger.store' (most likely due to a circular import) (/tmp/leash-grade-9c78szfi/wt/ledger/store.py)
```

**rename_across_files** trial 15 - `unchecked` (snapshot)

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 1 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(0, 3), [0, 0, 0])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [] != [0, 0, 0]

Second list contains 3 additional elements.
First extra element 0:
0

- []
+ [0, 0, 0]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 2 - `unchecked` (snapshot), `checked`, `escalated`

```
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [-34, -35, -35] != [-34, -33, -33]

First differing element 1:
-35
-33

- [-34, -35, -35]
?         ^    ^

+ [-34, -33, -33]
?         ^    ^


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 3 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 4 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [35, 35, 34] != [-34, -33, -33]

First differing element 0:
35
-34

- [35, 35, 34]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 5 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 6 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [-33, -33, -33] != [-34, -33, -33]

First differing element 0:
-33
-34

- [-33, -33, -33]
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
AssertionError: Lists differ: [-33, -35, -35] != [-34, -33, -33]

First differing element 0:
-33
-34

- [-33, -35, -35]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 9 - `unchecked` (snapshot), `checked`, `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
  File "money.py", line 48
    In `ledger/money.py`, add a function `split_evenly_signed(cents: int, parts: int) -> list[int]`
       ^
SyntaxError: invalid syntax
```

Grader output for checked, escalated:

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
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [-34, -35, -35] != [-34, -33, -33]

First differing element 1:
-35
-33

- [-34, -35, -35]
?         ^    ^

+ [-34, -33, -33]
?         ^    ^


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 15 - `unchecked` (snapshot), `checked`, `escalated`

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

**tdd_average_transaction** trial 1 - `unchecked` (snapshot)

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
  File "test_stats.py", line 3, in <module>
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
  File "test_stats.py", line 1, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 5 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 6 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 17, in test_average_transaction
    average = ledger.average_transaction("Food")
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
  File "test_stats.py", line 5, in <module>
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
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-grade-dk3d6_eb/wt/ledger/stats.py)
```

**tdd_average_transaction** trial 10 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-grade-3s1vd7_q/wt/ledger/stats.py)
```

**tdd_average_transaction** trial 11 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-grade-0oa64y5a/wt/ledger/stats.py)
```

**tdd_average_transaction** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-grade-ehyt9y2i/wt/ledger/stats.py)
```

**tdd_average_transaction** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 30, in test_average_transaction_zero_entries
    ledger.average_transaction("Travel")
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Ledger' object has no attribute 'average_transaction'

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_average_transaction** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 21, in test
    self.assertEqual(average_transaction(l2, "x"), 99.67)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Decimal('99.67') != 99.67

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 15 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

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

Grader output for escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-trial-ha91fnd2/leash-tdd_average_transaction-3112378-1790161564417336271/ledger/stats.py)
```

**tdd_budget** trial 1 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
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

**tdd_budget** trial 4 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "test_budget.py", line 14, in test_over_budget
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

Grader output for escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ImportError: cannot import name 'over_budget' from 'ledger.budget' (/tmp/leash-trial-m0v5szcp/leash-tdd_budget-3112378-1790152337627291909/ledger/budget.py)
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

**tdd_budget** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 21, in test_over_budget_no_limit
    self.assertEqual(result, {})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
AssertionError: {'Food': 500} != {}
- {'Food': 500}
+ {}

----------------------------------------------------------------------
Ran 8 tests in 0.001s

FAILED (failures=3)
```

**tdd_budget** trial 8 - `unchecked` (snapshot)

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

**tdd_budget** trial 9 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 14, in test_over_budget
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

**tdd_budget** trial 10 - `unchecked` (snapshot)

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

**tdd_budget** trial 11 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 15, in test_over_budget
    self.assertEqual(result, expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
AssertionError: {'Food': 500} != {'Food': -1500}
- {'Food': 500}
+ {'Food': -1500}
?          ++


----------------------------------------------------------------------
Ran 3 tests in 0.000s

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

**tdd_budget** trial 15 - `unchecked` (snapshot)

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

## Limitations

- Small task set: every task currently uses the same Python fixture (ledger); results say nothing yet about other languages or larger codebases.
- Escalation is repair-only, with one cloud model per run (Gemini via the agy CLI by default, or Claude). TDD items are repaired with a single pass, not re-run red/green.
- Cloud models change behind the same name; escalation results are dated and go stale faster than local-model results.
- Scores are specific to the harness configuration named in each section and are not comparable across harness configurations.
