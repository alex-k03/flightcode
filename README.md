# Offline LeetCode

A self-contained interview prep repo. Zero dependencies (Python 3 stdlib only) — works fully offline.

## Usage

```
./run.py list                     # all questions, ● = solved
./run.py list --module graphs --difficulty medium
./run.py test two-sum             # run tests with time limits
./run.py test --all               # everything
./run.py status                   # progress bars per module
./run.py new dp/climbing-stairs   # scaffold a blank question
```

## Question shape

```
questions/<module>/<slug>/
    QUESTION.md        problem statement
    meta.json          {"difficulty", "time_limit_seconds", "function"}
    code.py            your solution (defines the function named in meta.json)
    tests/cases.json   [{"input": {kwargs}, "expected": ...}, ...]
```

Drop a new folder matching this shape anywhere under `questions/` and it just works — no registration.

Test case options: add `"order_insensitive": true` to a case when the expected output is a list whose order doesn't matter (e.g. "return all triplets").

## Generating questions with AI agents

Prompt template: "Create a question folder for <problem> in the shape described in README.md. Include 5-8 test cases covering edge cases (empty, single element, duplicates, negatives, max constraints). Set function name in meta.json. Leave code.py absent."

Always spot-check generated expected outputs against a reference solution before trusting them.
