# Agent Guide

This repo is an offline, dependency-free LeetCode-style practice set. Keep it simple: one Python runner, convention-based question folders, and no central registration.

## Question Contract

Every question lives at:

```text
questions/<module>/<slug>/
    QUESTION.md
    meta.json
    code.py
    solution.py
    tests/cases.json
```

`meta.json` must include:

```json
{
  "difficulty": "easy",
  "time_limit_seconds": 3,
  "function": "two_sum"
}
```

The function name must match the question slug converted to snake_case. For example, `valid-palindrome` uses `valid_palindrome`.

`code.py` is the user's working solution starter and is what `./run.py test` executes. It must define the function named by `meta.json`, but new questions should leave the body blank or `pass`.

`solution.py` is the example/reference solution for someone who gets stuck. It should define the same function and be correct.

Test cases call the target function with keyword arguments from each case's `input` object.

`tests/cases.json` is an array of cases:

```json
[
  {
    "input": {"nums": [2, 7, 11, 15], "target": 9},
    "expected": [0, 1]
  }
]
```

Add `"order_insensitive": true` only when the expected output is a list whose order should not matter.

## Question Index

`questions.md` is the human-readable index of all modules and questions. Update it whenever you add, rename, move, or remove a question.

When adding a question, put it under the matching module heading. If the module does not exist yet, add a new heading and table using the same columns as the rest of the file: Question, Slug, Difficulty, and Pattern.

## Adding A Question

Preferred workflow:

```sh
./run.py agent-prompt <module>/<slug> --title "Problem Title"
```

Use the printed prompt as the task for the agent adding the question.

When creating a question:

- Write a complete `QUESTION.md` with title, difficulty, problem, examples, constraints, and any pattern note that helps.
- Write `meta.json` with the question slug converted to snake_case as the function name.
- Write `code.py` with the user-facing starter function. Keep the implementation blank or `pass`.
- Write a correct reference/example implementation in `solution.py`.
- Add 5-8 deterministic test cases.
- Update `questions.md` with the new question.
- Cover meaningful edge cases: empty or minimal input when allowed, duplicates, negatives, ties, already-sorted or reverse cases, and large-shape cases when relevant.
- Run `./run.py test-solutions <slug>` to verify the reference solution and expected outputs.
- Do not make `code.py` pass unless the task explicitly asks for solved user code.
- Do not edit unrelated question folders.

## Local Commands

```sh
./run.py list
./run.py test <slug>
./run.py test --all
./run.py test-solutions <slug>
./run.py test-solutions --all
./run.py status
./run.py reset-completion <slug>
./run.py reset-completion --all
./run.py new <module>/<slug>
./run.py agent-prompt <module>/<slug> --title "Problem Title"
```

## Design Preferences

- Keep `run.py` self-contained unless there is a strong reason to split it.
- Prefer stdlib-only Python.
- Prefer JSON test data over custom parsing.
- Keep question folders modular and copyable.
- Keep `meta.json`, `code.py`, and `solution.py` function names/signatures in sync.
- Treat `.solved` files as local completion state. Use `./run.py reset-completion` to clear them.
- Avoid generated artifacts such as `__pycache__` and runner scratch files in commits.
