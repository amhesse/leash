# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-20T20:03-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| qwen2.5-coder:32b (Q4_K_M) + claude:claude-sonnet-5 | 10.9 | 10.9 | 10.9 | +0.0 | +0.0 | 210 | 0 |

## qwen2.5-coder:32b (Q4_K_M) + claude:claude-sonnet-5

|  |  |
|---|---|
| Model | qwen2.5-coder:32b |
| Digest | b92d6a0bd47ee791 |
| Size / quantization | 32.8B / Q4_K_M |
| Runtime | Ollama 0.33.2, context 32768 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | claude:claude-sonnet-5 via claude CLI 2.1.275 (Claude Code) |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-20T11:40 → 2026-09-20T20:01 |

### Scores

**Leash 10.9** (uniform-v1, spec 0.1). Raw (no checks): 10.9. System (with escalation): 10.9. Harness lift +0.0, escalation lift +0.0.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 28 | 2 | 0 | 0 | 78.7% | 21.3% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 37 | 8 | 0 | 0 | 68.7% | 31.3% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| tdd | 16.7% | 30 | 0 | 0 | 0 | 30 | 0.0% | 11.4% | 0.0 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 28 | 2 | 0 | 0 | 78.7% | 21.3% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 37 | 8 | 0 | 0 | 68.7% | 31.3% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| tdd | 16.7% | 30 | 0 | 30 | 0 | 0 | 0.0% | 100.0% | 0.0 | L0 Supervised |

### Escalated - parked work repaired by the cloud model

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 28 | 2 | 0 | 0 | 78.7% | 21.3% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 37 | 8 | 0 | 0 | 68.7% | 31.3% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| tdd | 16.7% | 30 | 28 | 1 | 0 | 1 | 78.7% | 16.7% | 0.0 | L0 Supervised |

### Escalation

| Needed | Run | Skipped | Failed | Rescue rate | Cloud silent wrong | Median cloud s | Median cloud tokens |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 30 | 30 | 0 | 0 | 93.3% | 1 | 21.2 | 245200.0 |

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 29.1 | 1010.5 | 0.0% | 73.2% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| add_method_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| algorithm_single | prose-single-logic | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| bugfix_from_symptom | bugfix | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| bugfix_negative_fraction | bugfix | 13/2/0/0 | 13/2/0/0 | 13/2/0/0 |
| exact_new_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| exact_replace_function_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| feature_single_dates | prose-single-logic | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| multi_file_cli_flag | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| rename_across_files | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| small_edit_single | prose-single-small | 14/1/0/0 | 14/1/0/0 | 14/1/0/0 |
| split_evenly_signed | prose-single-logic | 7/8/0/0 | 7/8/0/0 | 7/8/0/0 |
| tdd_average_transaction | tdd | 0/0/0/15 | 0/15/0/0 | 14/0/0/1 |
| tdd_budget | tdd | 0/0/0/15 | 0/15/0/0 | 14/1/0/0 |

### Every silent wrong (64 across 41 trial(s))

**bugfix_negative_fraction** trial 2 - `unchecked` (snapshot), `checked`, `escalated`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 7, in test
    self.assertEqual(parse_amount(text), cents, text)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: -12 != -1200 : -12

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
AssertionError: -12 != -1200 : -12

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**small_edit_single** trial 5 - `unchecked` (snapshot), `checked`, `escalated`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 6, in test
    self.assertEqual(format_cents(-5), "-$0.05")
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: '-$0.95' != '-$0.05'
- -$0.95
?     ^
+ -$0.05
?     ^


----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 1 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [32, 31, 31] != [-34, -33, -33]

First differing element 0:
32
-34

- [32, 31, 31]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 5 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [32, 31, 31] != [-34, -33, -33]

First differing element 0:
32
-34

- [32, 31, 31]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 6 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [33, 33, 32] != [-34, -33, -33]

First differing element 0:
33
-34

- [33, 33, 32]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 7 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [32, 31, 31] != [-34, -33, -33]

First differing element 0:
32
-34

- [32, 31, 31]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 9 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [32, 31, 31] != [-34, -33, -33]

First differing element 0:
32
-34

- [32, 31, 31]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 12 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 13 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [32, 31, 31] != [-34, -33, -33]

First differing element 0:
32
-34

- [32, 31, 31]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 15 - `unchecked` (snapshot), `checked`, `escalated`

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

**tdd_average_transaction** trial 1 - `unchecked` (snapshot)

```
  File "test_stats.py", line 16, in test_average_transaction_with_single_entry
    ledger.add(Entry(datetime.date(2023, 10, 1), "transport", -200))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=3)
```

**tdd_average_transaction** trial 2 - `unchecked` (snapshot)

```
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-5000, note="Groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_average_transaction** trial 3 - `unchecked` (snapshot)

```
  File "test_stats.py", line 22, in test_average_transaction_with_single_entry
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category='food', cents=-500))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=3)
```

**tdd_average_transaction** trial 4 - `unchecked` (snapshot)

```
  File "test_stats.py", line 15, in test_average_transaction_with_single_entry
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="transport", cents=-150))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=4)
```

**tdd_average_transaction** trial 5 - `unchecked` (snapshot)

```
  File "test_stats.py", line 21, in test_average_transaction_single_entry
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category='travel', cents=2000))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_average_transaction** trial 6 - `unchecked` (snapshot)

```
  File "test_stats.py", line 8, in test_average_transaction
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-500))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 7 - `unchecked` (snapshot)

```
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="income", cents=10000, note="Salary"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=3)
```

**tdd_average_transaction** trial 8 - `unchecked` (snapshot)

```
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category='entertainment', cents=-10000, note='Movie ticket'))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 8 tests in 0.001s

FAILED (errors=5)
```

**tdd_average_transaction** trial 9 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 10 - `unchecked` (snapshot)

```
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="food", cents=-5000, note="Groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 5 tests in 0.000s

FAILED (errors=2)
```

**tdd_average_transaction** trial 11 - `unchecked` (snapshot)

```
  File "test_stats.py", line 22, in test_average_transaction_single_entry
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=1500))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=5)
```

**tdd_average_transaction** trial 12 - `unchecked` (snapshot)

```
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-5000, note="Groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=4)
```

**tdd_average_transaction** trial 13 - `unchecked` (snapshot)

```
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="salary", cents=20000, note="Monthly salary"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_average_transaction** trial 14 - `unchecked` (snapshot)

```
  File "test_stats.py", line 22, in test_average_transaction_single_entry
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category='travel', cents=1500))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=3)
```

**tdd_average_transaction** trial 15 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 21, in test
    self.assertEqual(average_transaction(l2, "x"), 99.67)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Decimal('100.00') != 99.67

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 1 - `unchecked` (snapshot)

```
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-1000, note="Groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (errors=3)
```

**tdd_budget** trial 2 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(datetime.date(2023, 10, 1), "food", -5000, "Groceries"))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_budget** trial 3 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 30, in test_under_budget
    ledger.add(Entry(datetime.date(2023, 10, 1), "food", -2000, "Groceries"))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.000s

FAILED (errors=3)
```

**tdd_budget** trial 4 - `unchecked` (snapshot)

```
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(datetime.date(2023, 10, 1), "groceries", -2000, "Weekly groceries"))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=3)
```

**tdd_budget** trial 5 - `unchecked` (snapshot)

```
  File "test_budget.py", line 27, in test_under_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-2000, note="groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (errors=3)
```

**tdd_budget** trial 6 - `unchecked` (snapshot)

```
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-2000, note="groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 5 tests in 0.000s

FAILED (errors=3)
```

**tdd_budget** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(datetime.date(2023, 10, 1), "food", -5000))  # $50
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 8, in setUp
    self.ledger.add(Entry(datetime.date(2023, 10, 1), "food", -2000, "Groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_budget** trial 9 - `unchecked` (snapshot)

```
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category='food', cents=-500, note='Groceries'))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_budget** trial 10 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-500))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_budget** trial 11 - `unchecked` (snapshot)

```
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-1500, note="Groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_budget** trial 12 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "test_budget.py", line 28, in test_under_budget
    ledger.add(Entry(datetime.date(2023, 10, 1), "food", -5000))  # $50
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=4)
```

Grader output for escalated:

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': 50, 'rent': 0} != {'food': 50}
- {'food': 50, 'rent': 0}
+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 13 - `unchecked` (snapshot)

```
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-1500, note="Groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_budget** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(datetime.date(2023, 10, 1), "food", -5000))  # $50
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 15 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(datetime.date(2023, 10, 1), "food", -1500, "Groceries"))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

## Limitations

- Small task set: every task currently uses the same Python fixture (ledger); results say nothing yet about other languages or larger codebases.
- Escalation is repair-only, with one cloud model per run (Gemini via the agy CLI by default, or Claude). TDD items are repaired with a single pass, not re-run red/green.
- Cloud models change behind the same name; escalation results are dated and go stale faster than local-model results.
- Scores are specific to the harness configuration named in each section and are not comparable across harness configurations.
