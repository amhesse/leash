# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-16T03:27-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| qwen2.5-coder:14b (Q4_K_M) + ollama:qwen3.8:27b | 10.5 | 7.4 | 10.6 | +3.1 | +0.1 | 210 | 0 |

## qwen2.5-coder:14b (Q4_K_M) + ollama:qwen3.8:27b

|  |  |
|---|---|
| Model | qwen2.5-coder:14b |
| Digest | 9ec8897f747e246e |
| Size / quantization | 14.8B / Q4_K_M |
| Runtime | Ollama 0.33.2, context 32768 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | ollama:qwen3.8:27b (local, forge lite backend) |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-16T02:12 → 2026-09-16T03:26 |

### Scores

**Leash 10.5** (uniform-v1, spec 0.1). Raw (no checks): 7.4. System (with escalation): 10.6. Harness lift +3.1, escalation lift +0.1.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 43 | 1 | 0 | 1 | 85.2% | 11.6% | 19.5 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 35 | 9 | 0 | 1 | 63.7% | 33.8% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 1 | 0 | 1 | 28 | 0.6% | 11.4% | 0.1 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 43 | 2 | 0 | 0 | 85.2% | 14.8% | 1.0 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 34 | 11 | 0 | 0 | 61.3% | 38.7% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 1 | 29 | 0 | 0 | 0.6% | 99.4% | 0.0 | L0 Supervised |

### Escalated - parked work repaired by the cloud model

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 44 | 1 | 0 | 0 | 88.4% | 11.6% | 20.2 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 36 | 9 | 0 | 0 | 66.2% | 33.8% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 25 | 5 | 0 | 0 | 66.4% | 33.6% | 0.0 | L0 Supervised |

### Escalation

| Needed | Run | Skipped | Failed | Rescue rate | Cloud silent wrong | Median cloud s | Median cloud tokens |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 31 | 31 | 0 | 0 | 83.9% | 5 | 88.6 | 5263 |

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 4.6 | 1034.5 | 0.6% | 73.2% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 14/1/0/0 | 14/1/0/0 | 14/1/0/0 |
| add_method_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| algorithm_single | prose-single-logic | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| bugfix_from_symptom | bugfix | 14/1/0/0 | 14/1/0/0 | 14/1/0/0 |
| bugfix_negative_fraction | bugfix | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| exact_new_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| exact_replace_function_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| feature_single_dates | prose-single-logic | 15/0/0/0 | 14/1/0/0 | 15/0/0/0 |
| multi_file_cli_flag | multi-file | 14/0/0/1 | 14/1/0/0 | 15/0/0/0 |
| rename_across_files | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| small_edit_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| split_evenly_signed | prose-single-logic | 5/9/0/1 | 5/10/0/0 | 6/9/0/0 |
| tdd_average_transaction | tdd | 0/0/1/14 | 0/15/0/0 | 10/5/0/0 |
| tdd_budget | tdd | 1/0/0/14 | 1/14/0/0 | 15/0/0/0 |

### Every silent wrong (70 across 43 trial(s))

**add_currency_field** trial 10 - `unchecked` (snapshot), `checked`, `escalated`

Grader output for unchecked:

```
    print(summary(load(args.csv)))
                  ~~~~^^^^^^^^^^
  File "cli.py", line 16, in load
    date, category, amount, note, *currency = row[:5]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: not enough values to unpack (expected at least 4, got 3)

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (errors=2)
```

Grader output for checked, escalated:

```
    print(summary(load(args.csv)))
                  ~~~~^^^^^^^^^^
  File "cli.py", line 16, in load
    date, category, amount, note, *currency = row[:5]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: not enough values to unpack (expected at least 4, got 3)

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (errors=2)
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

**feature_single_dates** trial 6 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 4, in <module>
    from typing import dict
ImportError: cannot import name 'dict' from 'typing' (/usr/lib/python3.14/typing.py). Did you mean: 'Dict'?
```

**multi_file_cli_flag** trial 5 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 1
    ```python
    ^
SyntaxError: invalid syntax
```

**split_evenly_signed** trial 1 - `unchecked` (snapshot), `checked`, `escalated`

```
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [34, 34, 33] != [-34, -33, -33]

First differing element 0:
34
-34

- [34, 34, 33]
?       ^

+ [-34, -33, -33]
?  +    + ^  +


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 2 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [34, 33, 33] != [-34, -33, -33]

First differing element 0:
34
-34

- [34, 33, 33]
+ [-34, -33, -33]
?  +    +    +


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 3 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [34, 33, 33] != [-34, -33, -33]

First differing element 0:
34
-34

- [34, 33, 33]
+ [-34, -33, -33]
?  +    +    +


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 4 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 6 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [34, 33, 33] != [-34, -33, -33]

First differing element 0:
34
-34

- [34, 33, 33]
+ [-34, -33, -33]
?  +    +    +


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 7 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [34, 33, 33] != [-34, -33, -33]

First differing element 0:
34
-34

- [34, 33, 33]
+ [-34, -33, -33]
?  +    +    +


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 8 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [34, 33, 33] != [-34, -33, -33]

First differing element 0:
34
-34

- [34, 33, 33]
+ [-34, -33, -33]
?  +    +    +


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

**split_evenly_signed** trial 13 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [34, 33, 33] != [-34, -33, -33]

First differing element 0:
34
-34

- [34, 33, 33]
+ [-34, -33, -33]
?  +    +    +


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 14 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
ImportError: cannot import name 'split_evenly_signed' from 'ledger.money' (/tmp/leash-grade-im306j6c/wt/ledger/money.py)
```

**tdd_average_transaction** trial 1 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-grade-wq8dfvvj/wt/ledger/stats.py)
```

Grader output for escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-trial-coemyq0q/leash-tdd_average_transaction-492568-1789550005647444125/ledger/stats.py)
```

**tdd_average_transaction** trial 2 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 6 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

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

Grader output for escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-trial-1eaz_rwx/leash-tdd_average_transaction-492568-1789551754186798925/ledger/stats.py)
```

**tdd_average_transaction** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-grade-f0oasoup/wt/ledger/stats.py)
```

**tdd_average_transaction** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-grade-eqhc_rf5/wt/ledger/stats.py)
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
  File "test_stats.py", line 7, in test_average_transaction
    ledger.add(Entry(date=datetime.date.today(), category='Food', cents=1000))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (errors=1)
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

**tdd_average_transaction** trial 12 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

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

**tdd_average_transaction** trial 13 - `unchecked` (snapshot)

```
  File "test_stats.py", line 8, in test_average_transaction
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="Food", cents=1000))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 14 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

```
  File "test_stats.py", line 8, in test_average_transaction_single_entry
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="Food", cents=1500, note="Lunch"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=3)
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

**tdd_average_transaction** trial 15 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

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

**tdd_budget** trial 1 - `unchecked` (snapshot)

```
  File "test_budget.py", line 11, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category='Food', cents=-500, note='Lunch'))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 2 - `unchecked` (snapshot)

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

**tdd_budget** trial 4 - `unchecked` (snapshot)

```
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="Food", cents=-1000))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 5 - `unchecked` (snapshot)

```
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="Food", cents=-1000))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 6 - `unchecked` (snapshot)

```
  File "test_budget.py", line 11, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="Food", cents=-500, note="Lunch"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 7 - `unchecked` (snapshot)

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

**tdd_budget** trial 8 - `unchecked` (snapshot)

```
  File "test_budget.py", line 7, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category='Food', cents=-1000))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 9 - `unchecked` (snapshot)

```
  File "test_budget.py", line 9, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 10, 1), category="Food", cents=-1000, note="Lunch"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 10 - `unchecked` (snapshot)

```
  File "test_budget.py", line 11, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="Food", cents=-1000, note="Lunch"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 11 - `unchecked` (snapshot)

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

**tdd_budget** trial 12 - `unchecked` (snapshot)

```
  File "test_budget.py", line 11, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="Food", cents=-1000, note="Lunch"))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 13 - `unchecked` (snapshot)

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

**tdd_budget** trial 14 - `unchecked` (base)

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
