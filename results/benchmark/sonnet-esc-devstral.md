# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-20T08:16-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| devstral:latest (Q4_K_M) + claude:claude-sonnet-5 | 14.5 | 14.5 | 14.5 | +0.0 | +0.0 | 210 | 0 |

## devstral:latest (Q4_K_M) + claude:claude-sonnet-5

|  |  |
|---|---|
| Model | devstral:latest |
| Digest | 9bd74193e93935e9 |
| Size / quantization | 23.6B / Q4_K_M |
| Runtime | Ollama 0.33.2, context 131072 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | claude:claude-sonnet-5 via claude CLI 2.1.275 (Claude Code) |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-20T03:46 → 2026-09-20T08:13 |

### Scores

**Leash 14.5** (uniform-v1, spec 0.1). Raw (no checks): 14.5. System (with escalation): 14.5. Harness lift +0.0, escalation lift +0.0.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 23 | 7 | 0 | 0 | 59.1% | 40.9% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 40 | 5 | 0 | 0 | 76.5% | 23.5% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 16 | 2 | 1 | 11 | 36.1% | 21.3% | 0.0 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 23 | 7 | 0 | 0 | 59.1% | 40.9% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 40 | 5 | 0 | 0 | 76.5% | 23.5% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 14 | 16 | 0 | 0 | 30.2% | 69.8% | 0.0 | L0 Supervised |

### Escalated - parked work repaired by the cloud model

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 23 | 7 | 0 | 0 | 59.1% | 40.9% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 40 | 5 | 0 | 0 | 76.5% | 23.5% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 26 | 4 | 0 | 0 | 70.3% | 29.7% | 0.0 | L0 Supervised |

### Escalation

| Needed | Run | Skipped | Failed | Rescue rate | Cloud silent wrong | Median cloud s | Median cloud tokens |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 12 | 12 | 0 | 0 | 83.3% | 2 | 45.2 | 261040.0 |

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 6.0 | 2212.5 | 0.5% | 44.0% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| add_method_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| algorithm_single | prose-single-logic | 14/1/0/0 | 14/1/0/0 | 14/1/0/0 |
| bugfix_from_symptom | bugfix | 14/1/0/0 | 14/1/0/0 | 14/1/0/0 |
| bugfix_negative_fraction | bugfix | 9/6/0/0 | 9/6/0/0 | 9/6/0/0 |
| exact_new_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| exact_replace_function_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| feature_single_dates | prose-single-logic | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| multi_file_cli_flag | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| rename_across_files | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| small_edit_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| split_evenly_signed | prose-single-logic | 11/4/0/0 | 11/4/0/0 | 11/4/0/0 |
| tdd_average_transaction | tdd | 8/0/1/6 | 7/8/0/0 | 13/2/0/0 |
| tdd_budget | tdd | 8/2/0/5 | 7/8/0/0 | 13/2/0/0 |

### Every silent wrong (58 across 28 trial(s))

**algorithm_single** trial 15 - `unchecked` (snapshot), `checked`, `escalated`

```
  File "_leash_grader.py", line 5, in test
    self.assertEqual(split_evenly(100, 3), [34, 33, 33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [33, 33, 34] != [34, 33, 33]

First differing element 0:
33
34

- [33, 33, 34]
+ [34, 33, 33]

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

**bugfix_negative_fraction** trial 4 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 5 - `unchecked` (snapshot), `checked`, `escalated`

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
AssertionError: 1150 != -1250 : -12.50

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**bugfix_negative_fraction** trial 10 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(parse_amount(text), cents, text)
                     ~~~~~~~~~~~~^^^^^^
  File "money.py", line 11, in parse_amount
    return int(whole) * 100 + int(frac)
           ~~~^^^^^^^
ValueError: invalid literal for int() with base 10: '--12'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

**bugfix_negative_fraction** trial 14 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 1 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 7 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 13 - `unchecked` (snapshot), `checked`, `escalated`

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

**tdd_average_transaction** trial 2 - `unchecked` (snapshot)

```
    self.assertAlmostEqual(average_transaction(ledger, "groceries"), 1333.67)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1333.5 != 1333.67 within 7 places (0.17000000000007276 difference)

----------------------------------------------------------------------
Ran 9 tests in 0.000s

FAILED (failures=2)
```

**tdd_average_transaction** trial 3 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

```
  File "test_stats.py", line 21, in test_single_entry_returns_its_value
    self.assertEqual(average_transaction(ledger, "groceries"), -150.00)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: -15000.0 != -150.0

----------------------------------------------------------------------
Ran 8 tests in 0.001s

FAILED (failures=3)
```

Grader output for escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 11, in test
    self.assertEqual(average_transaction(l, "food"), -150.0)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: -1.5 != -150.0

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 8 - `unchecked` (snapshot)

```
  File "test_stats.py", line 16, in test_average_transaction_with_single_entry
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="rent", cents=10000))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=3)
```

**tdd_average_transaction** trial 9 - `unchecked` (snapshot)

```
    self.assertAlmostEqual(average_transaction(ledger, "Food"), 1000.00)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 833.33 != 1000.0 within 7 places (166.66999999999996 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 11 - `unchecked` (snapshot), `escalated`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 11, in test
    self.assertEqual(average_transaction(l, "food"), -150.0)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: -1.5 != -150.0

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 29, in test_multiple_entries_same_category
    self.assertEqual(average_transaction(ledger, "groceries"), 1000.00)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 833.33 != 1000.0

----------------------------------------------------------------------
Ran 8 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 35, in test_mixed_income_and_spending
    self.assertEqual(average_transaction(ledger, "investments"), 2333.33)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 2000.0 != 2333.33

----------------------------------------------------------------------
Ran 8 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 14 - `unchecked` (snapshot)

```
  File "test_stats.py", line 19, in test_single_entry_in_category
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="groceries", cents=1000))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 8 tests in 0.001s

FAILED (errors=5)
```

**tdd_budget** trial 1 - `unchecked` (snapshot)

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': 1050} != {'food': 50}
- {'food': 1050}
?          --

+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 2 - `unchecked` (snapshot), `checked`, `escalated`

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
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'entertainment': 1000} != {'groceries': 2500, 'entertainment': 1000}
- {'entertainment': 1000}
+ {'entertainment': 1000, 'groceries': 2500}

----------------------------------------------------------------------
Ran 7 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 8 - `unchecked` (snapshot)

```
AssertionError: {'Entertainment': 1000, 'Groceries': 1500} != {'Groceries': 2000, 'Entertainment': 1000}
- {'Entertainment': 1000, 'Groceries': 1500}
?                                      ^^

+ {'Entertainment': 1000, 'Groceries': 2000}
?                                      ^^


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 10 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 31, in test_over_budget
    self.assertEqual(result, expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
AssertionError: {'food': 600, 'transport': 100} != {'food': 600}
- {'food': 600, 'transport': 100}
+ {'food': 600}

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 12 - `unchecked` (snapshot)

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': 1050} != {'food': 50}
- {'food': 1050}
?          --

+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 14 - `unchecked` (snapshot)

```
  File "test_budget.py", line 26, in test_over_budget
    self.assertEqual(result, expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
AssertionError: {'groceries': 200, 'dining': 500} != {'groceries': 200}
- {'dining': 500, 'groceries': 200}
+ {'groceries': 200}

----------------------------------------------------------------------
Ran 7 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 15 - `unchecked` (snapshot), `checked`, `escalated`

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
