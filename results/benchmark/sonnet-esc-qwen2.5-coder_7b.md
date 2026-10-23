# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-20T07:48-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| qwen2.5-coder:7b (Q4_K_M) + claude:claude-sonnet-5 | 7.2 | 7.2 | 7.2 | +0.0 | +0.0 | 210 | 0 |

## qwen2.5-coder:7b (Q4_K_M) + claude:claude-sonnet-5

|  |  |
|---|---|
| Model | qwen2.5-coder:7b |
| Digest | dae161e27b0e90dd |
| Size / quantization | 7.6B / Q4_K_M |
| Runtime | Ollama 0.33.2, context 32768 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | claude:claude-sonnet-5 via claude CLI 2.1.275 (Claude Code) |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-20T01:55 → 2026-09-20T02:28 |

### Scores

**Leash 7.2** (uniform-v1, spec 0.1). Raw (no checks): 7.2. System (with escalation): 7.2. Harness lift +0.0, escalation lift +0.0.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 26 | 3 | 0 | 1 | 70.3% | 25.6% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 41 | 4 | 0 | 0 | 79.3% | 20.7% | 0.0 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 24 | 21 | 0 | 0 | 39.1% | 60.9% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 1 | 0 | 0 | 29 | 0.6% | 11.4% | 0.1 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 26 | 4 | 0 | 0 | 70.3% | 29.7% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 41 | 4 | 0 | 0 | 79.3% | 20.7% | 0.0 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 24 | 21 | 0 | 0 | 39.1% | 60.9% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 1 | 29 | 0 | 0 | 0.6% | 99.4% | 0.0 | L0 Supervised |

### Escalated - parked work repaired by the cloud model

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 27 | 3 | 0 | 0 | 74.4% | 25.6% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 41 | 4 | 0 | 0 | 79.3% | 20.7% | 0.0 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 24 | 21 | 0 | 0 | 39.1% | 60.9% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 23 | 3 | 0 | 4 | 59.1% | 25.6% | 0.0 | L0 Supervised |

### Escalation

| Needed | Run | Skipped | Failed | Rescue rate | Cloud silent wrong | Median cloud s | Median cloud tokens |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 30 | 30 | 0 | 0 | 76.7% | 3 | 34.2 | 431944.0 |

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 2.0 | 970.0 | 0.0% | 51.7% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| add_method_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| algorithm_single | prose-single-logic | 14/1/0/0 | 14/1/0/0 | 14/1/0/0 |
| bugfix_from_symptom | bugfix | 14/1/0/0 | 14/1/0/0 | 14/1/0/0 |
| bugfix_negative_fraction | bugfix | 12/2/0/1 | 12/3/0/0 | 13/2/0/0 |
| exact_new_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| exact_replace_function_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| feature_single_dates | prose-single-logic | 7/8/0/0 | 7/8/0/0 | 7/8/0/0 |
| multi_file_cli_flag | multi-file | 11/4/0/0 | 11/4/0/0 | 11/4/0/0 |
| rename_across_files | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| small_edit_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| split_evenly_signed | prose-single-logic | 3/12/0/0 | 3/12/0/0 | 3/12/0/0 |
| tdd_average_transaction | tdd | 1/0/0/14 | 1/14/0/0 | 13/1/0/1 |
| tdd_budget | tdd | 0/0/0/15 | 0/15/0/0 | 10/2/0/3 |

### Every silent wrong (117 across 58 trial(s))

**algorithm_single** trial 15 - `unchecked` (snapshot), `checked`, `escalated`

```
  File "money.py", line 26, in split_evenly
    return ([base_amount + 1] * remainder + [base_amount]) * parts // parts
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^~~~~~~
TypeError: unsupported operand type(s) for //: 'list' and 'int'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
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

**bugfix_negative_fraction** trial 3 - `unchecked` (snapshot), `checked`, `escalated`

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

**bugfix_negative_fraction** trial 7 - `unchecked` (base)

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

**multi_file_cli_flag** trial 3 - `unchecked` (snapshot), `checked`, `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 9, in <module>
    from .store import Entry, Ledger, filtered
ImportError: cannot import name 'filtered' from 'ledger.store' (/tmp/leash-grade-157yz7wg/wt/ledger/store.py)
```

Grader output for checked, escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 9, in <module>
    from .store import Entry, Ledger, filtered
ImportError: cannot import name 'filtered' from 'ledger.store' (/tmp/leash-trial-xhkno_0p/leash-multi_file_cli_flag-8658-1789894783392327378/ledger/store.py)
```

**multi_file_cli_flag** trial 5 - `unchecked` (snapshot), `checked`, `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 9, in <module>
    from .store import Entry, Ledger, filtered
ImportError: cannot import name 'filtered' from 'ledger.store' (/tmp/leash-grade-qrlqzi04/wt/ledger/store.py)
```

Grader output for checked, escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 9, in <module>
    from .store import Entry, Ledger, filtered
ImportError: cannot import name 'filtered' from 'ledger.store' (/tmp/leash-trial-4l15oik3/leash-multi_file_cli_flag-8658-1789895056747446898/ledger/store.py)
```

**multi_file_cli_flag** trial 8 - `unchecked` (snapshot), `checked`, `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 9, in <module>
    from .store import Entry, Ledger, filtered
ImportError: cannot import name 'filtered' from 'ledger.store' (/tmp/leash-grade-g60546hf/wt/ledger/store.py)
```

Grader output for checked, escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 9, in <module>
    from .store import Entry, Ledger, filtered
ImportError: cannot import name 'filtered' from 'ledger.store' (/tmp/leash-trial-o5i1ubcf/leash-multi_file_cli_flag-8658-1789895471340354628/ledger/store.py)
```

**multi_file_cli_flag** trial 13 - `unchecked` (snapshot), `checked`, `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 9, in <module>
    from .store import Entry, Ledger, filtered
ImportError: cannot import name 'filtered' from 'ledger.store' (/tmp/leash-grade-g7u26o41/wt/ledger/store.py)
```

Grader output for checked, escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger import cli
  File "cli.py", line 9, in <module>
    from .store import Entry, Ledger, filtered
ImportError: cannot import name 'filtered' from 'ledger.store' (/tmp/leash-trial-yhk9602g/leash-multi_file_cli_flag-8658-1789896333089816641/ledger/store.py)
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
AssertionError: Lists differ: [] != [-34, -33, -33]

Second list contains 3 additional elements.
First extra element 0:
-34

- []
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 7 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [33, 34, 34] != [-34, -33, -33]

First differing element 0:
33
-34

- [33, 34, 34]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 8 - `unchecked` (snapshot), `checked`, `escalated`

```
    self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [-1, -1, -1] != [-34, -33, -33]

First differing element 0:
-1
-34

- [-1, -1, -1]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 10 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 11 - `unchecked` (snapshot), `checked`, `escalated`

```
AssertionError: Lists differ: [-33, -33, -33, -33] != [-34, -33, -33]

First differing element 0:
-33
-34

First list contains 1 additional elements.
First extra element 3:
-33

- [-33, -33, -33, -33]
+ [-34, -33, -33]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**split_evenly_signed** trial 13 - `unchecked` (snapshot), `checked`, `escalated`

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

**split_evenly_signed** trial 14 - `unchecked` (snapshot), `checked`, `escalated`

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
Traceback (most recent call last):
  File "test_stats.py", line 10, in test_average_transaction
    ledger.add(Entry(datetime.date(2023, 1, 1), "Food", 100))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 2 - `unchecked` (snapshot)

```
    result = average_transaction(None, 'test_category')
  File "stats.py", line 4, in average_transaction
    entries = [e for e in ledger.entries if e.category == category]
                          ^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'entries'

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (errors=1)
```

**tdd_average_transaction** trial 3 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 7, in test_average_transaction
    ledger.add(Entry(datetime.date(2023, 1, 1), 'Groceries', -500))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 4 - `unchecked` (snapshot), `escalated`

Grader output for unchecked:

```
  File "test_stats.py", line 7, in test_average_transaction
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="Groceries", cents=200))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

Grader output for escalated:

```
                     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^
  File "stats.py", line 6, in average_transaction
    raise ValueError("Not enough entries in the specified category")
ValueError: Not enough entries in the specified category

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 5 - `unchecked` (snapshot)

```
  File "test_stats.py", line 9, in test_average_transaction
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="Groceries", cents=-500))
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
                      ~~~~~~~~~~~~~~~~~^^
  File "mock.py", line 1480, in get_original
    raise AttributeError(
        "%s does not have the attribute %r" % (target, name)
    )
AttributeError: <class 'ledger.store.Ledger'> does not have the attribute 'entries'

----------------------------------------------------------------------
Ran 6 tests in 0.002s

FAILED (errors=4)
```

**tdd_average_transaction** trial 8 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 9 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 10 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 11 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 13 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 14 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 8, in test_average_transaction
    ledger.add(Entry(datetime.date(2023, 1, 1), "Groceries", 100))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 15 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "test_stats.py", line 7, in test_average_transaction
    ledger.add(Entry(datetime.date(2023, 10, 1), 'Groceries', -200))
                     ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 1 - `unchecked` (snapshot)

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
  File "test_budget.py", line 8, in test_over_budget
    ledger.add(Entry(date=datetime.date(2023, 1, 1), category="Groceries", cents=-100))
                          ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_budget** trial 6 - `unchecked` (snapshot)

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

**tdd_budget** trial 7 - `unchecked` (snapshot), `escalated`

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
                     ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "budget.py", line 31, in over_budget
    category_spending[entry.category] += entry.cents
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
KeyError: 'fun'

----------------------------------------------------------------------
Ran 2 tests in 0.000s

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

**tdd_budget** trial 12 - `unchecked` (snapshot), `escalated`

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

**tdd_budget** trial 14 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 15 - `unchecked` (base)

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
