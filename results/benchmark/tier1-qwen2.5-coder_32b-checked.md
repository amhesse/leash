# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-20T11:40-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| qwen2.5-coder:32b (Q4_K_M) | 10.9 | 10.9 | not measured | +0.0 | – | 210 | 0 |

## qwen2.5-coder:32b (Q4_K_M)

|  |  |
|---|---|
| Model | qwen2.5-coder:32b |
| Digest | b92d6a0bd47ee791 |
| Size / quantization | 32.8B / Q4_K_M |
| Runtime | Ollama 0.33.2, context 32768 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | disabled |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-20T09:30 → 2026-09-20T11:38 |

### Scores

**Leash 10.9** (uniform-v1, spec 0.1). Raw (no checks): 10.9. System (with escalation): not measured. Harness lift +0.0, escalation lift –.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 26 | 4 | 0 | 0 | 70.3% | 29.7% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 36 | 9 | 0 | 0 | 66.2% | 33.8% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 27 | 3 | 0 | 0 | 74.4% | 25.6% | 0.0 | L0 Supervised |
| tdd | 16.7% | 30 | 0 | 0 | 1 | 29 | 0.0% | 11.4% | 0.0 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 26 | 4 | 0 | 0 | 70.3% | 29.7% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 36 | 9 | 0 | 0 | 66.2% | 33.8% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 27 | 3 | 0 | 0 | 74.4% | 25.6% | 0.0 | L0 Supervised |
| tdd | 16.7% | 30 | 0 | 30 | 0 | 0 | 0.0% | 100.0% | 0.0 | L0 Supervised |

### Escalation

Escalation was disabled for this run.

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 27.8 | 993.0 | 0.6% | 64.4% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 15/0/0/0 | 15/0/0/0 | – |
| add_method_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | – |
| algorithm_single | prose-single-logic | 15/0/0/0 | 15/0/0/0 | – |
| bugfix_from_symptom | bugfix | 15/0/0/0 | 15/0/0/0 | – |
| bugfix_negative_fraction | bugfix | 11/4/0/0 | 11/4/0/0 | – |
| exact_new_file | exact-spec | 15/0/0/0 | 15/0/0/0 | – |
| exact_replace_function_file | exact-spec | 15/0/0/0 | 15/0/0/0 | – |
| feature_single_dates | prose-single-logic | 15/0/0/0 | 15/0/0/0 | – |
| multi_file_cli_flag | multi-file | 15/0/0/0 | 15/0/0/0 | – |
| rename_across_files | multi-file | 15/0/0/0 | 15/0/0/0 | – |
| small_edit_single | prose-single-small | 12/3/0/0 | 12/3/0/0 | – |
| split_evenly_signed | prose-single-logic | 6/9/0/0 | 6/9/0/0 | – |
| tdd_average_transaction | tdd | 0/0/1/14 | 0/15/0/0 | – |
| tdd_budget | tdd | 0/0/0/15 | 0/15/0/0 | – |

### Every silent wrong (62 across 46 trial(s))

**bugfix_negative_fraction** trial 3 - `unchecked` (snapshot), `checked`

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

**bugfix_negative_fraction** trial 7 - `unchecked` (snapshot), `checked`

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

**bugfix_negative_fraction** trial 9 - `unchecked` (snapshot), `checked`

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

**bugfix_negative_fraction** trial 11 - `unchecked` (snapshot), `checked`

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

**small_edit_single** trial 5 - `unchecked` (snapshot), `checked`

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

**small_edit_single** trial 7 - `unchecked` (snapshot), `checked`

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

**small_edit_single** trial 15 - `unchecked` (snapshot), `checked`

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

**split_evenly_signed** trial 1 - `unchecked` (snapshot), `checked`

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

**split_evenly_signed** trial 3 - `unchecked` (snapshot), `checked`

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

**split_evenly_signed** trial 5 - `unchecked` (snapshot), `checked`

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

**split_evenly_signed** trial 6 - `unchecked` (snapshot), `checked`

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

**split_evenly_signed** trial 8 - `unchecked` (snapshot), `checked`

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

**split_evenly_signed** trial 10 - `unchecked` (snapshot), `checked`

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

**split_evenly_signed** trial 12 - `unchecked` (snapshot), `checked`

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

**split_evenly_signed** trial 15 - `unchecked` (snapshot), `checked`

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

**tdd_average_transaction** trial 1 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 25, in test_average_transaction_single_entry
    ledger.add(Entry(datetime.date(2023, 10, 1), "food", -5000))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (errors=3)
```

**tdd_average_transaction** trial 2 - `unchecked` (snapshot)

```
  File "test_stats.py", line 34, in test_average_transaction_with_single_entry
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category='gift', cents=500))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=5)
```

**tdd_average_transaction** trial 3 - `unchecked` (snapshot)

```
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category='food', cents=-500, note='Groceries'))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 5 tests in 0.000s

FAILED (errors=2)
```

**tdd_average_transaction** trial 4 - `unchecked` (snapshot)

```
  File "test_stats.py", line 33, in test_average_transaction_with_single_entry
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="gift", cents=500))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=5)
```

**tdd_average_transaction** trial 5 - `unchecked` (snapshot)

```
  File "test_stats.py", line 21, in test_average_transaction_category_missing
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category='food', cents=1000))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 5 tests in 0.000s

FAILED (errors=2)
```

**tdd_average_transaction** trial 6 - `unchecked` (snapshot)

```
  File "test_stats.py", line 32, in test_average_transaction_zero_entries
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category='food', cents=0))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=4)
```

**tdd_average_transaction** trial 7 - `unchecked` (snapshot)

```
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-5000, note="Groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_average_transaction** trial 8 - `unchecked` (snapshot)

```
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-5000, note="Groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 5 tests in 0.000s

FAILED (errors=2)
```

**tdd_average_transaction** trial 9 - `unchecked` (snapshot)

```
  File "test_stats.py", line 15, in test_average_transaction_with_single_entry
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="transport", cents=-500))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_average_transaction** trial 10 - `unchecked` (snapshot)

```
  File "test_stats.py", line 34, in test_average_transaction_with_single_entry
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category='misc', cents=100))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=5)
```

**tdd_average_transaction** trial 11 - `unchecked` (snapshot)

```
  File "test_stats.py", line 10, in test_average_transaction_with_entries
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category='food', cents=-500))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_average_transaction** trial 12 - `unchecked` (snapshot)

```
  File "test_stats.py", line 27, in test_average_transaction_single_entry
    ledger.add(Entry(datetime.date(2023, 10, 1), "food", -1500, "Groceries"))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 5 tests in 0.000s

FAILED (errors=3)
```

**tdd_average_transaction** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 8, in setUp
    self.ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-5000))
                               ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (errors=3)
```

**tdd_average_transaction** trial 14 - `unchecked` (snapshot)

```
  File "test_stats.py", line 16, in test_average_transaction_with_single_entry
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="travel", cents=-1500))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=4)
```

**tdd_average_transaction** trial 15 - `unchecked` (snapshot)

```
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category='food', cents=-500, note='Groceries'))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_budget** trial 1 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(datetime.date(2023, 10, 1), "food", -1500, "groceries"))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_budget** trial 2 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 29, in test_within_budget
    ledger.add(Entry(datetime.date(2023, 10, 1), "food", -2000, "Groceries"))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=4)
```

**tdd_budget** trial 3 - `unchecked` (snapshot)

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

**tdd_budget** trial 4 - `unchecked` (snapshot)

```
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-1000))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (errors=3)
```

**tdd_budget** trial 5 - `unchecked` (snapshot)

```
  File "test_budget.py", line 42, in test_over_budget_within_limits
    ledger.add(Entry(datetime.date(2023, 10, 1), "food", -5000, "Groceries"))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 5 tests in 0.000s

FAILED (errors=3)
```

**tdd_budget** trial 6 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 8, in setUp
    self.ledger.add(Entry(datetime.date(2023, 10, 1), "food", -2000, "Groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=5)
```

**tdd_budget** trial 7 - `unchecked` (snapshot)

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

**tdd_budget** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 29, in test_under_budget
    ledger.add(Entry(datetime.date(2023, 10, 1), "food", -5000, "Groceries"))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.000s

FAILED (errors=3)
```

**tdd_budget** trial 9 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 29, in test_under_budget
    ledger.add(Entry(datetime.date(2023, 10, 1), "food", -1000, "Groceries"))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.000s

FAILED (errors=3)
```

**tdd_budget** trial 10 - `unchecked` (snapshot)

```
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-2000, note="Groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

**tdd_budget** trial 11 - `unchecked` (snapshot)

```
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-2000, note="Groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 5 tests in 0.000s

FAILED (errors=3)
```

**tdd_budget** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(datetime.date(2023, 10, 1), "food", -5000, "Groceries"))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=5)
```

**tdd_budget** trial 13 - `unchecked` (snapshot)

```
  File "test_budget.py", line 60, in test_single_category_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-1500))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=5)
```

**tdd_budget** trial 14 - `unchecked` (snapshot)

```
  File "test_budget.py", line 28, in test_within_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-800, note="Groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=3)
```

**tdd_budget** trial 15 - `unchecked` (snapshot)

```
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="food", cents=-5000, note="groceries"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=4)
```

## Limitations

- Small task set: every task currently uses the same Python fixture (ledger); results say nothing yet about other languages or larger codebases.
- Escalation is repair-only, with one cloud model per run (Gemini via the agy CLI by default, or Claude). TDD items are repaired with a single pass, not re-run red/green.
- Cloud models change behind the same name; escalation results are dated and go stale faster than local-model results.
- Scores are specific to the harness configuration named in each section and are not comparable across harness configurations.
