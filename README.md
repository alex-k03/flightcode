# Offline LeetCode

A self-contained interview prep repo. Zero dependencies (Python 3 stdlib only) — works fully offline.

## Usage

```
./run.py list                     # all questions, ● = solved
./run.py list --module graphs --difficulty medium
./run.py test two-sum             # run tests with time limits
./run.py test --all               # everything
./run.py test-solutions --all     # verify example/reference solutions
./run.py status                   # progress bars per module
./run.py reset-completion --all   # clear solved markers
./run.py new dp/climbing-stairs   # scaffold a blank question
./run.py agent-prompt dp/climbing-stairs --title "Climbing Stairs"
```

## Question shape

```
questions/<module>/<slug>/
    QUESTION.md        problem statement
    meta.json          {"difficulty", "time_limit_seconds", "function"}
    code.py            user solution starter tested by the runner
    solution.py        example/reference solution if you get stuck
    tests/cases.json   [{"input": {kwargs}, "expected": ...}, ...]
```

Drop a new folder matching this shape anywhere under `questions/` and it just works — no registration.

See `questions.md` for the human-readable module and question index.

Test case options: add `"order_insensitive": true` to a case when the expected output is a list whose order doesn't matter (e.g. "return all triplets").

## Adding questions with AI agents

Use the prompt helper:

```
./run.py agent-prompt arrays-hashing/group-anagrams --title "Group Anagrams"
```

Give the printed prompt to an agent. It tells the agent to read `AGENTS.md`, create the complete question folder, write a starter `code.py` and reference `solution.py`, update `questions.md`, add 5-8 tests, and run the local verification commands.

Always spot-check generated expected outputs against a reference solution before trusting them.
