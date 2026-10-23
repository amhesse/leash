# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-21T02:04-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| nemotron-3.5-lightning:30b (Q4_K_M) | 24.5 | 7.2 | not measured | +17.3 | – | 210 | 0 |

## nemotron-3.5-lightning:30b (Q4_K_M)

|  |  |
|---|---|
| Model | nemotron-3.5-lightning:30b |
| Digest | e7a64ff15fb174c4 |
| Size / quantization | 32.9B / Q4_K_M |
| Runtime | Ollama 0.33.2, context 1048576 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | disabled |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-21T00:11 → 2026-09-21T02:04 |

### Scores

**Leash 24.5** (uniform-v1, spec 0.1). Raw (no checks): 7.2. System (with escalation): not measured. Harness lift +17.3, escalation lift –.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 29 | 0 | 0 | 1 | 83.3% | 11.4% | 20.3 | L0 Supervised |
| exact-spec | 16.7% | 30 | 29 | 0 | 1 | 0 | 83.3% | 11.4% | 20.3 | L0 Supervised |
| multi-file | 16.7% | 45 | 42 | 0 | 0 | 3 | 82.1% | 7.9% | 39.1 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 42 | 0 | 0 | 3 | 82.1% | 7.9% | 39.1 | L1 Short leash |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 13 | 0 | 0 | 17 | 27.4% | 11.4% | 6.7 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 40 | 5 | 0 | 0 | 76.5% | 23.5% | 0.0 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 42 | 3 | 0 | 0 | 82.1% | 17.9% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 13 | 17 | 0 | 0 | 27.4% | 72.6% | 0.0 | L0 Supervised |

### Escalation

Escalation was disabled for this run.

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 22.9 | 4339.5 | 0.5% | 100.0% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 15/0/0/0 | 15/0/0/0 | – |
| add_method_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | – |
| algorithm_single | prose-single-logic | 15/0/0/0 | 15/0/0/0 | – |
| bugfix_from_symptom | bugfix | 15/0/0/0 | 15/0/0/0 | – |
| bugfix_negative_fraction | bugfix | 14/0/0/1 | 14/1/0/0 | – |
| exact_new_file | exact-spec | 15/0/0/0 | 15/0/0/0 | – |
| exact_replace_function_file | exact-spec | 14/0/1/0 | 15/0/0/0 | – |
| feature_single_dates | prose-single-logic | 15/0/0/0 | 15/0/0/0 | – |
| multi_file_cli_flag | multi-file | 14/0/0/1 | 14/1/0/0 | – |
| rename_across_files | multi-file | 13/0/0/2 | 11/4/0/0 | – |
| small_edit_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | – |
| split_evenly_signed | prose-single-logic | 12/0/0/3 | 12/3/0/0 | – |
| tdd_average_transaction | tdd | 5/0/0/10 | 5/10/0/0 | – |
| tdd_budget | tdd | 8/0/0/7 | 8/7/0/0 | – |

### Every silent wrong (26 across 26 trial(s))

**bugfix_negative_fraction** trial 9 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import parse_amount
  File "money.py", line 1
    """
    ^
SyntaxError: unterminated triple-quoted string literal (detected at line 1)
```

**multi_file_cli_flag** trial 2 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 10
    note: str = """
                ^
SyntaxError: unterminated triple-quoted string literal (detected at line 31)
```

**rename_across_files** trial 5 - `unchecked` (base)

```
----------------------------------------------------------------------
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in test
    self.assertFalse(hasattr(Ledger, "add"))
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: True is not false

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 7 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 10
    note: str = """
                ^
SyntaxError: unterminated triple-quoted string literal (detected at line 24)
```

**rename_across_files** trial 13 - `unchecked` (base)

```
----------------------------------------------------------------------
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in test
    self.assertFalse(hasattr(Ledger, "add"))
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: True is not false

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**rename_across_files** trial 15 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.store import Entry, Ledger
  File "store.py", line 10
    note: str = """
                ^
SyntaxError: unterminated triple-quoted string literal (detected at line 24)
```

**split_evenly_signed** trial 3 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
ImportError: cannot import name 'split_evenly_signed' from 'ledger.money' (/tmp/leash-grade-358l1lsz/wt/ledger/money.py)
```

**split_evenly_signed** trial 4 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
ImportError: cannot import name 'split_evenly_signed' from 'ledger.money' (/tmp/leash-grade-dec2x0o3/wt/ledger/money.py)
```

**split_evenly_signed** trial 6 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
ImportError: cannot import name 'split_evenly_signed' from 'ledger.money' (/tmp/leash-grade-ly2rr8tn/wt/ledger/money.py)
```

**tdd_average_transaction** trial 1 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 6 - `unchecked` (snapshot)

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
  File "test_stats.py", line 4, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 10 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 14 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 15 - `unchecked` (snapshot)

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

**tdd_budget** trial 7 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 8 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 13 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 14 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 15 - `unchecked` (branch_tip)

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
