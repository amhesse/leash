# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-21T05:23-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| nemotron-3.5-lightning:30b (Q4_K_M) + ollama:muse-glimmer:30b | 20.0 | 3.6 | 25.2 | +16.4 | +5.2 | 210 | 0 |

## nemotron-3.5-lightning:30b (Q4_K_M) + ollama:muse-glimmer:30b

|  |  |
|---|---|
| Model | nemotron-3.5-lightning:30b |
| Digest | e7a64ff15fb174c4 |
| Size / quantization | 32.9B / Q4_K_M |
| Runtime | Ollama 0.33.2, context 1048576 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | ollama:muse-glimmer:30b (local, forge lite backend) |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-21T02:36 → 2026-09-21T05:20 |

### Scores

**Leash 20.0** (uniform-v1, spec 0.1). Raw (no checks): 3.6. System (with escalation): 25.2. Harness lift +16.4, escalation lift +5.2.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 27 | 0 | 3 | 0 | 74.4% | 11.4% | 18.1 | L0 Supervised |
| multi-file | 16.7% | 45 | 42 | 0 | 0 | 3 | 82.1% | 7.9% | 39.1 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 41 | 0 | 0 | 4 | 79.3% | 7.9% | 37.7 | L1 Short leash |
| prose-single-small | 16.7% | 30 | 29 | 0 | 0 | 1 | 83.3% | 11.4% | 20.3 | L0 Supervised |
| tdd | 16.7% | 30 | 10 | 0 | 0 | 20 | 19.2% | 11.4% | 4.7 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 42 | 3 | 0 | 0 | 82.1% | 17.9% | 0.0 | L0 Supervised |
| prose-single-logic | 16.7% | 45 | 40 | 5 | 0 | 0 | 76.5% | 23.5% | 0.0 | L0 Supervised |
| prose-single-small | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| tdd | 16.7% | 30 | 9 | 21 | 0 | 0 | 16.7% | 83.3% | 0.0 | L0 Supervised |

### Escalated - parked work repaired by the cloud model

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 29 | 1 | 0 | 0 | 83.3% | 16.7% | 0.0 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 29 | 0 | 0 | 1 | 83.3% | 11.4% | 20.3 | L0 Supervised |

### Escalation

| Needed | Run | Skipped | Failed | Rescue rate | Cloud silent wrong | Median cloud s | Median cloud tokens |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 31 | 31 | 0 | 0 | 96.8% | 0 | 71.9 | 4269 |

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 26.0 | 4175.0 | 1.7% | 96.6% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| add_method_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| algorithm_single | prose-single-logic | 15/0/0/0 | 14/1/0/0 | 15/0/0/0 |
| bugfix_from_symptom | bugfix | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| bugfix_negative_fraction | bugfix | 14/1/0/0 | 14/1/0/0 | 14/1/0/0 |
| exact_new_file | exact-spec | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| exact_replace_function_file | exact-spec | 12/0/3/0 | 15/0/0/0 | 15/0/0/0 |
| feature_single_dates | prose-single-logic | 15/0/0/0 | 15/0/0/0 | 15/0/0/0 |
| multi_file_cli_flag | multi-file | 14/0/0/1 | 14/1/0/0 | 15/0/0/0 |
| rename_across_files | multi-file | 13/0/0/2 | 13/2/0/0 | 15/0/0/0 |
| small_edit_single | prose-single-small | 14/0/0/1 | 14/1/0/0 | 15/0/0/0 |
| split_evenly_signed | prose-single-logic | 11/0/0/4 | 11/4/0/0 | 15/0/0/0 |
| tdd_average_transaction | tdd | 4/0/0/11 | 4/11/0/0 | 15/0/0/0 |
| tdd_budget | tdd | 6/0/0/9 | 5/10/0/0 | 14/0/0/1 |

### Every silent wrong (33 across 31 trial(s))

**algorithm_single** trial 10 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly, format_cents
  File "money.py", line 15
    def split_evenly(cents: int, parts: int
                    ^
SyntaxError: '(' was never closed
```

**bugfix_negative_fraction** trial 9 - `unchecked` (snapshot), `checked`, `escalated`

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

**multi_file_cli_flag** trial 5 - `unchecked` (base)

```
----------------------------------------------------------------------
Traceback (most recent call last):
  File "_leash_grader.py", line 19, in test_filtered
    f = l.filtered("a")
        ^^^^^^^^^^
AttributeError: 'Ledger' object has no attribute 'filtered'

----------------------------------------------------------------------
Ran 2 tests in 0.002s

FAILED (errors=2)
```

**rename_across_files** trial 4 - `unchecked` (base)

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

**rename_across_files** trial 10 - `unchecked` (base)

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

**small_edit_single** trial 13 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import format_cents, parse_amount
  File "money.py", line 1
    """Money is always an int number of cents; strings only at the edges."""
IndentationError: unexpected indent
```

**split_evenly_signed** trial 5 - `unchecked` (snapshot)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
  File "money.py", line 14
    """
    ^
SyntaxError: unterminated triple-quoted string literal (detected at line 14)
```

**split_evenly_signed** trial 7 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
ImportError: cannot import name 'split_evenly_signed' from 'ledger.money' (/tmp/leash-grade-alabvk5d/wt/ledger/money.py)
```

**split_evenly_signed** trial 12 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
ImportError: cannot import name 'split_evenly_signed' from 'ledger.money' (/tmp/leash-grade-zxlwefsw/wt/ledger/money.py)
```

**split_evenly_signed** trial 13 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 2, in <module>
    from ledger.money import split_evenly_signed
ImportError: cannot import name 'split_evenly_signed' from 'ledger.money' (/tmp/leash-grade-1f2a3sau/wt/ledger/money.py)
```

**tdd_average_transaction** trial 3 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 4 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 5 - `unchecked` (snapshot)

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
  File "test_stats.py", line 3, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'


----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (errors=1)
```

**tdd_average_transaction** trial 8 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 9 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 13 - `unchecked` (base)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 3, in <module>
    from ledger.stats import average_transaction
ModuleNotFoundError: No module named 'ledger.stats'
```

**tdd_average_transaction** trial 14 - `unchecked` (snapshot)

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

**tdd_budget** trial 1 - `unchecked` (snapshot)

```
  File "test_budget.py", line 18, in test_spending_within_limit
    ledger.add(Ledger.Entry(date=datetime.date(2023, 1, 1), category="food", cents=-50, note="dinner"))
               ^^^^^^^^^^^^
AttributeError: type object 'Ledger' has no attribute 'Entry'

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=5)
```

**tdd_budget** trial 2 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 3 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 5 - `unchecked` (base)

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

**tdd_budget** trial 8 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 9 - `unchecked` (branch_tip)

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

**tdd_budget** trial 12 - `unchecked` (branch_tip)

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
