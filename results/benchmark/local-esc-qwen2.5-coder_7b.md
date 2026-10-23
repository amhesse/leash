# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-16T02:12-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| qwen2.5-coder:7b (Q4_K_M) + ollama:qwen3.8:27b | 7.2 | 7.2 | 10.6 | +0.0 | +3.4 | 210 | 0 |

## qwen2.5-coder:7b (Q4_K_M) + ollama:qwen3.8:27b

|  |  |
|---|---|
| Model | qwen2.5-coder:7b |
| Digest | dae161e27b0e90dd |
| Size / quantization | 7.6B / Q4_K_M |
| Runtime | Ollama 0.33.2, context 32768 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | ollama:qwen3.8:27b (local, forge lite backend) |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-16T00:53 → 2026-09-16T02:08 |

### Scores

**Leash 7.2** (uniform-v1, spec 0.1). Raw (no checks): 7.2. System (with escalation): 10.6. Harness lift +0.0, escalation lift +3.4.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 24 | 6 | 0 | 0 | 62.7% | 37.3% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 42 | 3 | 0 | 0 | 82.1% | 17.9% | 0.0 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 26 | 19 | 0 | 0 | 43.3% | 56.7% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 1 | 0 | 0 | 29 | 0.6% | 11.4% | 0.1 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 24 | 6 | 0 | 0 | 62.7% | 37.3% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 42 | 3 | 0 | 0 | 82.1% | 17.9% | 0.0 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 26 | 19 | 0 | 0 | 43.3% | 56.7% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 1 | 29 | 0 | 0 | 0.6% | 99.4% | 0.0 | L0 Supervised |

### Escalated - parked work repaired by the cloud model

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 24 | 6 | 0 | 0 | 62.7% | 37.3% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 42 | 3 | 0 | 0 | 82.1% | 17.9% | 0.0 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 26 | 19 | 0 | 0 | 43.3% | 56.7% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 29 | 0 | 0 | 1 | 83.3% | 11.4% | 20.3 | L0 Supervised |

### Escalation

| Needed | Run | Skipped | Failed | Rescue rate | Cloud silent wrong | Median cloud s | Median cloud tokens |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 29 | 29 | 0 | 0 | 96.6% | 0 | 122.0 | 6858 |

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 2.0 | 971.5 | 0.0% | 50.9% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| add_method_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| algorithm_single | prose-single-logic | 14/1/0/0 | 14/1/0/0 | 14/1/0/0 |
| bugfix_from_symptom | bugfix | 13/2/0/0 | 13/2/0/0 | 13/2/0/0 |
| bugfix_negative_fraction | bugfix | 11/4/0/0 | 11/4/0/0 | 11/4/0/0 |
| exact_new_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| exact_replace_function_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| feature_single_dates | prose-single-logic | 8/7/0/0 | 8/7/0/0 | 8/7/0/0 |
| multi_file_cli_flag | multi-file | 12/3/0/0 | 12/3/0/0 | 12/3/0/0 |
| rename_across_files | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| small_edit_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| split_evenly_signed | prose-single-logic | 4/11/0/0 | 4/11/0/0 | 4/11/0/0 |
| tdd_average_transaction | tdd | 1/0/0/14 | 1/14/0/0 | 15/0/0/0 |
| tdd_budget | tdd | 0/0/0/15 | 0/15/0/0 | 14/0/0/1 |

### Every silent wrong (113 across 57 trial(s))

**algorithm_single** trial 10 - `unchecked` (snapshot), `checked`, `escalated`

```
                     ~~~~~~~~~~~~^^^^^^^^
  File "money.py", line 25, in split_evenly
    raise ValueError("Cannot split cents evenly among the given number of parts")
ValueError: Cannot split cents evenly among the given number of parts

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
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

**bugfix_negative_fraction** trial 10 - `unchecked` (snapshot), `checked`, `escalated`

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
AssertionError: -1150 != -1250 : -12.50

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

**multi_file_cli_flag** trial 4 - `unchecked` (snapshot), `checked`, `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 9, in <module>
    from .store import Entry, Ledger, filtered
ImportError: cannot import name 'filtered' from 'ledger.store' (/tmp/leash-grade-yh2_3zzo/wt/ledger/store.py)
```

Grader output for checked, escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 9, in <module>
    from .store import Entry, Ledger, filtered
ImportError: cannot import name 'filtered' from 'ledger.store' (/tmp/leash-trial-eikvty9x/leash-multi_file_cli_flag-475107-1789546070000618475/ledger/store.py)
```

**multi_file_cli_flag** trial 8 - `unchecked` (snapshot), `checked`, `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 9, in <module>
    from .store import Entry, Ledger, filtered
ImportError: cannot import name 'filtered' from 'ledger.store' (/tmp/leash-grade-lo2o9ief/wt/ledger/store.py)
```

Grader output for checked, escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 9, in <module>
    from .store import Entry, Ledger, filtered
ImportError: cannot import name 'filtered' from 'ledger.store' (/tmp/leash-trial-_vjqi9z5/leash-multi_file_cli_flag-475107-1789547255413105504/ledger/store.py)
```

**multi_file_cli_flag** trial 13 - `unchecked` (snapshot), `checked`, `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 9, in <module>
    from .store import Entry, Ledger, filtered
ImportError: cannot import name 'filtered' from 'ledger.store' (/tmp/leash-grade-77gk6oq8/wt/ledger/store.py)
```

Grader output for checked, escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 9, in <module>
    from .store import Entry, Ledger, filtered
ImportError: cannot import name 'filtered' from 'ledger.store' (/tmp/leash-trial-1cz9jfry/leash-multi_file_cli_flag-475107-1789548983204873450/ledger/store.py)
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

**split_evenly_signed** trial 3 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [31, 32, 32] != [-34, -33, -33]

First differing element 0:
31
-34

- [31, 32, 32]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 4 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [-35, -34, -34] != [-34, -33, -33]

First differing element 0:
-35
-34

- [-35, -34, -34]
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
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [33, 33, 33, 33] != [-34, -33, -33]

First differing element 0:
33
-34

First list contains 1 additional elements.
First extra element 3:
33

- [33, 33, 33, 33]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 8 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 9 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [31, 32, 32] != [-34, -33, -33]

First differing element 0:
31
-34

- [31, 32, 32]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 10 - `unchecked` (snapshot), `checked`, `escalated`

```
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [-32, -33, -33] != [-34, -33, -33]

First differing element 0:
-32
-34

- [-32, -33, -33]
?    ^

+ [-34, -33, -33]
?    ^


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 12 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [-35, -34, -34] != [-34, -33, -33]

First differing element 0:
-35
-34

- [-35, -34, -34]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 14 - `unchecked` (snapshot), `checked`, `escalated`

```
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [-34, -34, -34] != [-34, -33, -33]

First differing element 1:
-34
-33

- [-34, -34, -34]
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
  File "test_stats.py", line 7, in test_average_transaction
    ledger.add(Entry(datetime.date(2023, 1, 1), "Food", 100))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 2 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 23, in test_average_transaction_single_entry
    ledger.add(Entry(datetime.date(2023, 10, 1), "Salary", 3000))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=3)
```

**tdd_average_transaction** trial 3 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 8, in test_average_transaction
    ledger.add(Entry(datetime.date(2023, 1, 1), 'Food', -100))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 4 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 8, in test_average_transaction
    ledger.add(Entry(datetime.date(2023, 1, 1), "Food", 100))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 5 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 7, in test_average_transaction
    ledger.add(Entry(datetime.date(2023, 1, 1), 'Food', 1000, 'lunch'))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 6 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 8, in test_average_transaction
    ledger.add(Entry(datetime.date(2023, 1, 1), "food", 100))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 7, in test_average_transaction
    ledger.add(Entry(datetime.date(2023, 1, 1), 'food', 100))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
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
  File "test_stats.py", line 7, in test_average_transaction
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="Groceries", cents=100))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 11 - `unchecked` (snapshot)

```
  File "test_stats.py", line 11, in test_average_transaction
    entry1 = Entry(date=datetime.date(2023, 1, 1), category="food", cents=100)
                        ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (errors=1)
```

**tdd_average_transaction** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 9, in test_average_transaction
    ledger.add(Entry(datetime.date(2023, 1, 1), "category1", 100))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 14 - `unchecked` (snapshot)

```
  File "stats.py", line 4, in average_transaction
    entries_in_category = [entry for entry in ledger.entries if entry.category == category]
                                              ^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'entries'

----------------------------------------------------------------------
Ran 4 tests in 0.000s

FAILED (errors=2)
```

**tdd_average_transaction** trial 15 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 8, in test_average_transaction
    ledger.add(Entry(datetime.date(2023, 1, 1), "Food", 100))
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

**tdd_budget** trial 2 - `unchecked` (snapshot)

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': -50} != {'food': 50}
- {'food': -50}
?          -

+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 3 - `unchecked` (snapshot)

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': -50} != {'food': 50}
- {'food': -50}
?          -

+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 4 - `unchecked` (snapshot)

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': -50} != {'food': 50}
- {'food': -50}
?          -

+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 5 - `unchecked` (snapshot)

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': -50} != {'food': 50}
- {'food': -50}
?          -

+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 6 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_budget.py", line 7, in test_over_budget
    ledger.add(Entry(datetime.date(2023, 1, 1), "Groceries", -500, "Weekly shopping"))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (errors=1)
```

**tdd_budget** trial 7 - `unchecked` (snapshot)

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': -50} != {'food': 50}
- {'food': -50}
?          -

+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 8 - `unchecked` (snapshot)

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': -50} != {'food': 50}
- {'food': -50}
?          -

+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 9 - `unchecked` (snapshot)

```
  File "test_budget.py", line 7, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="Groceries", cents=-100))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 10 - `unchecked` (snapshot)

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': -50} != {'food': 50}
- {'food': -50}
?          -

+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 11 - `unchecked` (snapshot)

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': -50} != {'food': 50}
- {'food': -50}
?          -

+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 12 - `unchecked` (snapshot)

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': -50} != {'food': 50}
- {'food': -50}
?          -

+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 13 - `unchecked` (snapshot)

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': -50} != {'food': 50}
- {'food': -50}
?          -

+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 14 - `unchecked` (snapshot)

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': -50} != {'food': 50}
- {'food': -50}
?          -

+ {'food': 50}

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

**tdd_budget** trial 15 - `unchecked` (snapshot)

```
    self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'food': -50} != {'food': 50}
- {'food': -50}
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
