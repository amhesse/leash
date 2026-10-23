# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-16T06:33-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| devstral:latest (Q4_K_M) + ollama:qwen3.8:27b | 11.6 | 10.9 | 10.9 | +0.7 | -0.7 | 210 | 0 |

## devstral:latest (Q4_K_M) + ollama:qwen3.8:27b

|  |  |
|---|---|
| Model | devstral:latest |
| Digest | 9bd74193e93935e9 |
| Size / quantization | 23.6B / Q4_K_M |
| Runtime | Ollama 0.33.2, context 131072 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | ollama:qwen3.8:27b (local, forge lite backend) |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-16T04:51 → 2026-09-16T06:28 |

### Scores

**Leash 11.6** (uniform-v1, spec 0.1). Raw (no checks): 10.9. System (with escalation): 10.9. Harness lift +0.7, escalation lift -0.7.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 16 | 14 | 0 | 0 | 36.1% | 63.9% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 29 | 0 | 1 | 0 | 83.3% | 11.4% | 20.3 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 33 | 12 | 0 | 0 | 59.0% | 41.0% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| tdd | 16.7% | 30 | 11 | 0 | 2 | 17 | 21.9% | 11.4% | 5.3 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 16 | 14 | 0 | 0 | 36.1% | 63.9% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 33 | 12 | 0 | 0 | 59.0% | 41.0% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| tdd | 16.7% | 30 | 9 | 21 | 0 | 0 | 16.7% | 83.3% | 0.0 | L0 Supervised |

### Escalated - parked work repaired by the cloud model

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 16 | 14 | 0 | 0 | 36.1% | 63.9% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 33 | 12 | 0 | 0 | 59.0% | 41.0% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| tdd | 16.7% | 30 | 26 | 3 | 0 | 1 | 70.3% | 25.6% | 0.0 | L0 Supervised |

### Escalation

| Needed | Run | Skipped | Failed | Rescue rate | Cloud silent wrong | Median cloud s | Median cloud tokens |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 20 | 20 | 0 | 0 | 80.0% | 3 | 117.2 | 7234.5 |

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 6.4 | 2232.5 | 1.8% | 38.6% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| add_method_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| algorithm_single | prose-single-logic | 10/5/0/0 | 10/5/0/0 | 10/5/0/0 |
| bugfix_from_symptom | bugfix | 11/4/0/0 | 11/4/0/0 | 11/4/0/0 |
| bugfix_negative_fraction | bugfix | 5/10/0/0 | 5/10/0/0 | 5/10/0/0 |
| exact_new_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| exact_replace_function_file | exact-spec | 14/0/1/0 | 15/0/0/0 | 15/0/0/0 |
| feature_single_dates | prose-single-logic | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| multi_file_cli_flag | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| rename_across_files | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| small_edit_single | prose-single-small | 14/1/0/0 | 14/1/0/0 | 14/1/0/0 |
| split_evenly_signed | prose-single-logic | 8/7/0/0 | 8/7/0/0 | 8/7/0/0 |
| tdd_average_transaction | tdd | 6/0/1/8 | 4/11/0/0 | 13/2/0/0 |
| tdd_budget | tdd | 5/0/1/9 | 5/10/0/0 | 13/1/0/1 |

### Every silent wrong (105 across 48 trial(s))

**algorithm_single** trial 3 - `unchecked` (snapshot), `checked`, `escalated`

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

**algorithm_single** trial 5 - `unchecked` (snapshot), `checked`, `escalated`

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

**algorithm_single** trial 6 - `unchecked` (snapshot), `checked`, `escalated`

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

**algorithm_single** trial 13 - `unchecked` (snapshot), `checked`, `escalated`

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
AssertionError: 1150 != -1250 : -12.50

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
AssertionError: 1250 != -1250 : -12.50

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

**small_edit_single** trial 2 - `unchecked` (snapshot), `checked`, `escalated`

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in test
    self.assertEqual(format_cents(-150), "-$1.50")
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: '-$-2.50' != '-$1.50'
- -$-2.50
?   ^^
+ -$1.50
?   ^


----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 2 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 4 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 8 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 10 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 11 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 12 - `unchecked` (snapshot), `checked`, `escalated`

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
    self.assertAlmostEqual(average_transaction(ledger, "Food"), 266.67, places=2)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 233.33 != 266.67 within 2 places (33.34 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 3 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 20, in test_average_transaction
    self.assertEqual(average_transaction(ledger, "groceries"), 500.0)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 375.0 != 500.0

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 4 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

```
  File "test_stats.py", line 46, in test_average_transaction_mixed_entries
    self.assertAlmostEqual(result, 1266.67, places=2)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1900.0 != 1266.67 within 2 places (633.3299999999999 difference)

----------------------------------------------------------------------
Ran 6 tests in 0.000s

FAILED (failures=1)
```

Grader output for escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-trial-ln61ydg7/leash-tdd_average_transaction-526228-1789560822077137694/ledger/stats.py)
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

**tdd_average_transaction** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 18, in test_average_transaction
    self.assertAlmostEqual(avg, 833.33, places=2)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 666.67 != 833.33 within 2 places (166.66000000000008 difference)

----------------------------------------------------------------------
Ran 6 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 9 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "test_stats.py", line 21, in test_average_transaction
    self.assertEqual(average_transaction(ledger, "food"), 1125.00)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1000.0 != 1125.0

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

Grader output for escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-trial-6jhl04m6/leash-tdd_average_transaction-526228-1789563094590900652/ledger/stats.py)
```

**tdd_average_transaction** trial 10 - `unchecked` (snapshot)

```
    self.assertAlmostEqual(average_transaction(ledger, "Salary"), 101250.00)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 101666.67 != 101250.0 within 7 places (416.66999999999825 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 11 - `unchecked` (snapshot)

```
    self.assertAlmostEqual(result, expected_average, places=2)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1000.0 != 333.33 within 2 places (666.6700000000001 difference)

----------------------------------------------------------------------
Ran 6 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 12 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 33, in test_mixed_income_and_spending
    self.assertEqual(average_transaction(ledger, "investment"), 3333.33)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 2333.33 != 3333.33

----------------------------------------------------------------------
Ran 7 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 13 - `unchecked` (snapshot)

```
    self.assertAlmostEqual(average_transaction(ledger, 'groceries'), 133.33, places=2)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 266.67 != 133.33 within 2 places (133.34 difference)

----------------------------------------------------------------------
Ran 6 tests in 0.000s

FAILED (failures=1)
```

**tdd_average_transaction** trial 15 - `unchecked` (snapshot)

```
  File "test_stats.py", line 10, in test_average_transaction
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="Food", cents=1000))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 1 - `unchecked` (snapshot)

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

**tdd_budget** trial 5 - `unchecked` (snapshot)

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

**tdd_budget** trial 6 - `unchecked` (snapshot)

```
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
AssertionError: {'groceries': 700, 'dining': 200} != {'groceries': 800, 'dining': 200}
- {'dining': 200, 'groceries': 700}
?                              ^

+ {'dining': 200, 'groceries': 800}
?                              ^


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 7 - `unchecked` (snapshot), `escalated`

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
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ImportError: cannot import name 'over_budget' from 'ledger.budget' (/tmp/leash-trial-nt82j5dd/leash-tdd_budget-526228-1789562066613882016/ledger/budget.py)
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

**tdd_budget** trial 11 - `unchecked` (snapshot)

```
  File "test_budget.py", line 9, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="groceries", cents=-1000, note="Grocery shopping"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=4)
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

**tdd_budget** trial 15 - `unchecked` (snapshot)

```
- {'Entertainment': 500, 'Groceries': 300, 'Transport': 50}
?                                     ^

+ {'Entertainment': 500, 'Groceries': 100, 'Transport': 50}
?                                     ^


----------------------------------------------------------------------
Ran 6 tests in 0.000s

FAILED (failures=1)
```

## Limitations

- Small task set: every task currently uses the same Python fixture (ledger); results say nothing yet about other languages or larger codebases.
- Escalation is repair-only, with one cloud model per run (Gemini via the agy CLI by default, or Claude). TDD items are repaired with a single pass, not re-run red/green.
- Cloud models change behind the same name; escalation results are dated and go stale faster than local-model results.
- Scores are specific to the harness configuration named in each section and are not comparable across harness configurations.
