# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-20T07:56-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| mistral-small:24b (Q4_K_M) + claude:claude-sonnet-5 | 17.9 | 17.9 | 17.9 | +0.0 | +0.0 | 210 | 0 |

## mistral-small:24b (Q4_K_M) + claude:claude-sonnet-5

|  |  |
|---|---|
| Model | mistral-small:24b |
| Digest | 8039dd90c1138d77 |
| Size / quantization | 23.6B / Q4_K_M |
| Runtime | Ollama 0.33.2, context 32768 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | claude:claude-sonnet-5 via claude CLI 2.1.275 (Claude Code) |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-20T03:09 → 2026-09-20T07:55 |

### Scores

**Leash 17.9** (uniform-v1, spec 0.1). Raw (no checks): 17.9. System (with escalation): 17.9. Harness lift +0.0, escalation lift +0.0.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 0 | 30 | 0 | 0 | 0.0% | 100.0% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 44 | 1 | 0 | 0 | 88.4% | 11.6% | 20.2 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 10 | 1 | 5 | 14 | 19.2% | 16.7% | 0.0 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 0 | 30 | 0 | 0 | 0.0% | 100.0% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 44 | 1 | 0 | 0 | 88.4% | 11.6% | 20.2 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 10 | 20 | 0 | 0 | 19.2% | 80.8% | 0.0 | L0 Supervised |

### Escalated - parked work repaired by the cloud model

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 0 | 30 | 0 | 0 | 0.0% | 100.0% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 44 | 1 | 0 | 0 | 88.4% | 11.6% | 20.2 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 22 | 6 | 2 | 0 | 55.6% | 37.3% | 0.0 | L0 Supervised |

### Escalation

| Needed | Run | Skipped | Failed | Rescue rate | Cloud silent wrong | Median cloud s | Median cloud tokens |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 19 | 19 | 0 | 0 | 63.2% | 5 | 34.3 | 292523 |

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 5.3 | 1125.0 | 3.0% | 30.4% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| add_method_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| algorithm_single | prose-single-logic | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| bugfix_from_symptom | bugfix | 0/15/0/0 | 0/15/0/0 | 0/15/0/0 |
| bugfix_negative_fraction | bugfix | 0/15/0/0 | 0/15/0/0 | 0/15/0/0 |
| exact_new_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| exact_replace_function_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| feature_single_dates | prose-single-logic | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| multi_file_cli_flag | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| rename_across_files | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| small_edit_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| split_evenly_signed | prose-single-logic | 14/1/0/0 | 14/1/0/0 | 14/1/0/0 |
| tdd_average_transaction | tdd | 10/1/0/4 | 10/5/0/0 | 12/3/0/0 |
| tdd_budget | tdd | 0/0/5/10 | 0/15/0/0 | 10/3/2/0 |

### Every silent wrong (120 across 51 trial(s))

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
AssertionError: 1150 != -1250 : -12.50

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
AssertionError: 1150 != -1250 : -12.50

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
AssertionError: -1150 != -1250 : -12.50

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
AssertionError: 1150 != -1250 : -12.50

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
AssertionError: 50 != -50 : -0.50

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
AssertionError: 1150 != -1250 : -12.50

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

**tdd_average_transaction** trial 1 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "test_stats.py", line 15, in test_average_transaction
    self.assertAlmostEqual(average_transaction(ledger, "groceries"), 1166.67, places=2)
                           ^^^^^^^^^^^^^^^^^^^
NameError: name 'average_transaction' is not defined

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

Grader output for escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 11, in test
    self.assertEqual(average_transaction(l, "food"), -150.0)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 216.67 != -150.0

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 2 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

```
    self.assertAlmostEqual(average_transaction(ledger, "groceries"), 1166.67)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 833.33 != 1166.67 within 7 places (333.34000000000003 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

Grader output for escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 11, in test
    self.assertEqual(average_transaction(l, "food"), -150.0)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 216.67 != -150.0

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 3 - `unchecked` (snapshot), `checked`, `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "test_stats.py", line 16, in test_average_transaction
    self.assertEqual(average_transaction(ledger, "groceries"), 1166.67)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 833.33 != 1166.67

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

Grader output for checked, escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 11, in test
    self.assertEqual(average_transaction(l, "food"), -150.0)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 216.67 != -150.0

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 5 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 16, in test_average_transaction
    self.assertEqual(average_transaction(ledger, "groceries"), 333.33)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 233.33 != 333.33

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 1 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 2 - `unchecked` (snapshot)

```
  File "test_budget.py", line 9, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="groceries", cents=-1000, note=""))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (errors=3)
```

**tdd_budget** trial 3 - `unchecked` (snapshot), `escalated`

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

**tdd_budget** trial 4 - `unchecked` (snapshot)

```
  File "test_budget.py", line 9, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="groceries", cents=-1000, note=""))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 5 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 6 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': 1050, 'rent': 2000} != {'food': 50}
- {'food': 1050, 'rent': 2000}
+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
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

**tdd_budget** trial 7 - `unchecked` (snapshot)

```
  File "test_budget.py", line 9, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="groceries", cents=-1000, note=""))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 8 - `unchecked` (snapshot)

```
  File "test_budget.py", line 9, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="groceries", cents=-5000, note=""))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 9 - `unchecked` (snapshot)

```
  File "test_budget.py", line 9, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="groceries", cents=-5000))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 10 - `unchecked` (snapshot)

```
  File "test_budget.py", line 9, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="groceries", cents=-5000))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 11 - `unchecked` (snapshot)

```
  File "test_budget.py", line 9, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="groceries", cents=-5000))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 12 - `unchecked` (snapshot)

```
  File "test_budget.py", line 9, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="groceries", cents=-1000, note=""))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 13 - `unchecked` (snapshot), `escalated`

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
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'groceries': 300, 'entertainment': 500} != {'groceries': 300, 'entertainment': 0}
- {'entertainment': 500, 'groceries': 300}
?                   --

+ {'entertainment': 0, 'groceries': 300}

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```

**tdd_budget** trial 15 - `unchecked` (snapshot)

```
AssertionError: {'groceries': 1000, 'entertainment': 1000} != {'groceries': 1000, 'entertainment': 500}
- {'entertainment': 1000, 'groceries': 1000}
?                   ^^

+ {'entertainment': 500, 'groceries': 1000}
?                   ^


----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```

## Limitations

- Small task set: every task currently uses the same Python fixture (ledger); results say nothing yet about other languages or larger codebases.
- Escalation is repair-only, with one cloud model per run (Gemini via the agy CLI by default, or Claude). TDD items are repaired with a single pass, not re-run red/green.
- Cloud models change behind the same name; escalation results are dated and go stale faster than local-model results.
- Scores are specific to the harness configuration named in each section and are not comparable across harness configurations.
