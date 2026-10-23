# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-22T21:41-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| nemotron-3.5-lightning:30b (Q4_K_M) + ollama:qwen3.8:27b | 20.9 | 7.5 | 21.8 | +13.4 | +0.9 | 210 | 0 |

## nemotron-3.5-lightning:30b (Q4_K_M) + ollama:qwen3.8:27b

|  |  |
|---|---|
| Model | nemotron-3.5-lightning:30b |
| Digest | e7a64ff15fb174c4 |
| Size / quantization | 32.9B / Q4_K_M |
| Runtime | Ollama 0.33.2, context 1048576 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | ollama:qwen3.8:27b (local, forge lite backend) |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-22T18:29 → 2026-09-22T21:40 |

### Scores

**Leash 20.9** (uniform-v1, spec 0.1). Raw (no checks): 7.5. System (with escalation): 21.8. Harness lift +13.4, escalation lift +0.9.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 28 | 0 | 2 | 0 | 78.7% | 11.4% | 19.1 | L0 Supervised |
| multi-file | 16.7% | 45 | 44 | 0 | 0 | 1 | 88.4% | 7.9% | 42.1 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 43 | 0 | 0 | 2 | 85.2% | 7.9% | 40.5 | L1 Short leash |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 6 | 0 | 0 | 24 | 9.5% | 11.4% | 2.3 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 43 | 2 | 0 | 0 | 85.2% | 14.8% | 1.0 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 43 | 2 | 0 | 0 | 85.2% | 14.8% | 1.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 6 | 24 | 0 | 0 | 9.5% | 90.5% | 0.0 | L0 Supervised |

### Escalated - parked work repaired by the cloud model

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 27 | 2 | 0 | 1 | 74.4% | 21.3% | 0.0 | L0 Supervised |

### Escalation

| Needed | Run | Skipped | Failed | Rescue rate | Cloud silent wrong | Median cloud s | Median cloud tokens |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 29 | 29 | 0 | 0 | 89.7% | 2 | 136.1 | 6426 |

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 21.6 | 3782.0 | 1.1% | 96.4% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| add_method_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| algorithm_single | prose-single-logic | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| bugfix_from_symptom | bugfix | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| bugfix_negative_fraction | bugfix | 14/1/0/0 | 14/1/0/0 | 14/1/0/0 |
| exact_new_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| exact_replace_function_file | exact-spec | 13/0/2/0 | 15/0/0/0 | 15/0/0/0 |
| feature_single_dates | prose-single-logic | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| multi_file_cli_flag | multi-file | 14/0/0/1 | 13/2/0/0 | 15/0/0/0 |
| rename_across_files | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| small_edit_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| split_evenly_signed | prose-single-logic | 13/0/0/2 | 13/2/0/0 | 15/0/0/0 |
| tdd_average_transaction | tdd | 3/0/0/12 | 3/12/0/0 | 13/2/0/0 |
| tdd_budget | tdd | 3/0/0/12 | 3/12/0/0 | 14/0/0/1 |

### Every silent wrong (33 across 29 trial(s))

**bugfix_negative_fraction** trial 1 - `unchecked` (snapshot), `checked`, `escalated`

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

**multi_file_cli_flag** trial 7 - `unchecked` (base)

```
----------------------------------------------------------------------
Traceback (most recent call last):
  File "_leash_grader.py", line 19, in test_filtered
    f = l.filtered("a")
        ^^^^^^^^^^
AttributeError: 'Ledger' object has no attribute 'filtered'

----------------------------------------------------------------------
Ran 2 tests in 0.003s

FAILED (errors=2)
```

**multi_file_cli_flag** trial 8 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 10
    note: str = """
                ^
SyntaxError: unterminated triple-quoted string literal (detected at line 31)
```

**split_evenly_signed** trial 3 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
ImportError: cannot import name 'split_evenly_signed' from 'ledger.money' (/tmp/leash-grade-sh9ozltx/wt/ledger/money.py)
```

**split_evenly_signed** trial 15 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
ImportError: cannot import name 'split_evenly_signed' from 'ledger.money' (/tmp/leash-grade-lgelttyo/wt/ledger/money.py)
```

**tdd_average_transaction** trial 1 - `unchecked` (base), `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

Grader output for escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-trial-jf6ehonc/leash-tdd_average_transaction-3751508-1790127288159276261/ledger/stats.py)
```

**tdd_average_transaction** trial 2 - `unchecked` (snapshot)

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
  File "test_stats.py", line 3, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 5 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 7 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 8 - `unchecked` (snapshot)

```
    module = self._get_module_from_name(name)
  File "loader.py", line 374, in _get_module_from_name
    __import__(name)
    ~~~~~~~~~~^^^^^^
  File "test_stats.py", line 2, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 10 - `unchecked` (branch_tip), `escalated`

Grader output for unchecked:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

Grader output for escalated:

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ImportError: cannot import name 'average_transaction' from 'ledger.stats' (/tmp/leash-trial-c0yh3hgs/leash-tdd_average_transaction-3751508-1790134094555505483/ledger/stats.py)
```

**tdd_average_transaction** trial 11 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 12 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 13 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 15 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_budget** trial 1 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 2 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 3 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 4 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 5 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 6 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 7 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 8 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 9 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 10 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 11 - `unchecked` (snapshot)

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

**tdd_budget** trial 12 - `unchecked` (base)

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
