# Leash report

Leash Score spec **0.1**, profile **uniform-v1**, generated 2026-09-21T00:11-07:00. Headline score = the `checked` condition (forge's automated checks). Bounds are 95% Wilson intervals; categories with fewer than 30 trials score 0 and are marked insufficient.

## Summary

| Model / escalation | Leash Score | Raw (unchecked) | System (escalated) | Harness lift | Escalation lift | Trials | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| muse-glimmer:30b (Q4_K_M) | 27.1 | 25.4 | not measured | +1.7 | – | 210 | 0 |

## muse-glimmer:30b (Q4_K_M)

|  |  |
|---|---|
| Model | muse-glimmer:30b |
| Digest | de878ce33ad81d06 |
| Size / quantization | 27.9B / Q4_K_M |
| Runtime | Ollama 0.33.2, context 131072 |
| Hardware | NVIDIA GeForce RTX 3090 Ti |
| Harness | forge / lite (config d4ca3ed71d1a), forge 0.1.0 @ 16f0f4c47c77 |
| Escalation | disabled |
| Tasks / categories | 14 / 6 |
| Trials scored / errors | 210 / 0 |
| Dates | 2026-09-20T20:54 → 2026-09-21T00:09 |

### Scores

**Leash 27.1** (uniform-v1, spec 0.1). Raw (no checks): 25.4. System (with escalation): not measured. Harness lift +1.7, escalation lift –.

### Checked - forge's automated checks (headline)

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 18 | 0 | 2 | 10 | 42.3% | 11.4% | 10.3 | L0 Supervised |

### Unchecked - the first attempt, no safety net

| Category | Weight | n | pass | silent wrong | parked ok | parked | P_lo | S_hi | Score | Level |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bugfix | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| exact-spec | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| multi-file | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-logic | 16.7% | 45 | 45 | 0 | 0 | 0 | 92.1% | 7.9% | 43.8 | L1 Short leash |
| prose-single-small | 16.7% | 30 | 30 | 0 | 0 | 0 | 88.6% | 11.4% | 21.6 | L0 Supervised |
| tdd | 16.7% | 30 | 17 | 13 | 0 | 0 | 39.2% | 60.8% | 0.0 | L0 Supervised |

### Escalation

Escalation was disabled for this run.

### Efficiency

| Median local s | Median local tokens | Friction rate | Catch rate |
|---:|---:|---:|---:|
| 39.2 | 2984.5 | 1.0% | 100.0% |

Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.

### Per task (pass / silent wrong / parked ok / parked)

| Task | Category | Checked | Unchecked | Escalated |
|---|---|---:|---:|---:|
| add_currency_field | multi-file | 15/0/0/0 | 15/0/0/0 | – |
| add_method_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | – |
| algorithm_single | prose-single-logic | 15/0/0/0 | 15/0/0/0 | – |
| bugfix_from_symptom | bugfix | 15/0/0/0 | 15/0/0/0 | – |
| bugfix_negative_fraction | bugfix | 15/0/0/0 | 15/0/0/0 | – |
| exact_new_file | exact-spec | 15/0/0/0 | 15/0/0/0 | – |
| exact_replace_function_file | exact-spec | 15/0/0/0 | 15/0/0/0 | – |
| feature_single_dates | prose-single-logic | 15/0/0/0 | 15/0/0/0 | – |
| multi_file_cli_flag | multi-file | 15/0/0/0 | 15/0/0/0 | – |
| rename_across_files | multi-file | 15/0/0/0 | 15/0/0/0 | – |
| small_edit_single | prose-single-small | 15/0/0/0 | 15/0/0/0 | – |
| split_evenly_signed | prose-single-logic | 15/0/0/0 | 15/0/0/0 | – |
| tdd_average_transaction | tdd | 6/0/2/7 | 5/10/0/0 | – |
| tdd_budget | tdd | 12/0/0/3 | 12/3/0/0 | – |

### Every silent wrong (13 across 13 trial(s))

**tdd_average_transaction** trial 4 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 5 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 6 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 7 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 9 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 10 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 11 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 13 - `unchecked` (snapshot)

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

**tdd_average_transaction** trial 15 - `unchecked` (snapshot)

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

**tdd_budget** trial 6 - `unchecked` (branch_tip)

```
Traceback (most recent call last):
  File "_leash_grader.py", line 5, in <module>
    from ledger.budget import over_budget
ModuleNotFoundError: No module named 'ledger.budget'
```

**tdd_budget** trial 13 - `unchecked` (branch_tip)

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

## Limitations

- Small task set: every task currently uses the same Python fixture (ledger); results say nothing yet about other languages or larger codebases.
- Escalation is repair-only, with one cloud model per run (Gemini via the agy CLI by default, or Claude). TDD items are repaired with a single pass, not re-run red/green.
- Cloud models change behind the same name; escalation results are dated and go stale faster than local-model results.
- Scores are specific to the harness configuration named in each section and are not comparable across harness configurations.
