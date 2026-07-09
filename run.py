#!/usr/bin/env python3
"""Offline LeetCode runner.

Discovers question folders under questions/, runs solution against JSON
test cases in a subprocess with a per-question time limit.

Usage:
    ./run.py list [--module MODULE] [--difficulty easy|medium|hard]
    ./run.py test <question-slug> [--case N]
    ./run.py test --all [--module MODULE]
    ./run.py test-solutions [<question-slug>] [--all] [--module MODULE]
    ./run.py status               # progress overview
    ./run.py reset-completion <question-slug>|--all [--module MODULE]
    ./run.py new <module>/<slug>  # scaffold a blank question
    ./run.py agent-prompt <module>/<slug> [--title TITLE]

Question shape (convention over configuration):
    questions/<module>/<slug>/
        QUESTION.md      problem statement
        meta.json        {"difficulty": "...", "time_limit_seconds": N,
                          "function": "two_sum"}
        code.py          your solution; must define the function named in meta
        solution.py      example/reference solution if you get stuck
        tests/cases.json [{"input": {...kwargs...}, "expected": ...}, ...]
"""

import argparse
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUESTIONS = ROOT / "questions"
USER_SOLUTION_FILE = "code.py"
REFERENCE_SOLUTION_FILE = "solution.py"

GREEN, RED, YELLOW, DIM, BOLD, RESET = (
    "\033[92m", "\033[91m", "\033[93m", "\033[2m", "\033[1m", "\033[0m",
)

HARNESS = r"""
import json, sys, importlib.util

code_path, func_name, case_json = sys.argv[1], sys.argv[2], sys.argv[3]
spec = importlib.util.spec_from_file_location("solution", code_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

fn = getattr(mod, func_name, None)
if fn is None:
    print(json.dumps({"error": f"function '{func_name}' not found in code.py"}))
    sys.exit(2)

case = json.loads(case_json)
try:
    result = fn(**case["input"])
    print(json.dumps({"result": result}))
except Exception as e:
    print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
    sys.exit(1)
"""


def discover():
    """Yield (module, slug, path) for every valid question folder."""
    if not QUESTIONS.exists():
        return
    for module_dir in sorted(QUESTIONS.iterdir()):
        if not module_dir.is_dir():
            continue
        for q_dir in sorted(module_dir.iterdir()):
            if (q_dir / "meta.json").exists():
                yield module_dir.name, q_dir.name, q_dir


def load_meta(q_dir):
    meta = json.loads((q_dir / "meta.json").read_text())
    meta.setdefault("time_limit_seconds", 5)
    meta.setdefault("difficulty", "medium")
    return meta


def find_question(slug):
    matches = [(m, s, p) for m, s, p in discover() if s == slug]
    if not matches:
        sys.exit(f"{RED}No question '{slug}' found. Run ./run.py list{RESET}")
    if len(matches) > 1:
        sys.exit(f"{RED}Ambiguous slug '{slug}' in modules: "
                 f"{[m for m, _, _ in matches]}{RESET}")
    return matches[0]


def normalise(value, order_insensitive=False):
    if order_insensitive and isinstance(value, list):
        return sorted(json.dumps(v, sort_keys=True) for v in value)
    return value


def run_case(q_dir, meta, case, harness_file, target_file):
    """Run one test case in a subprocess. Returns (status, detail, elapsed)."""
    start = time.monotonic()
    try:
        proc = subprocess.run(
            [sys.executable, str(harness_file), str(q_dir / target_file),
             meta["function"], json.dumps(case)],
            capture_output=True, text=True,
            timeout=meta["time_limit_seconds"],
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT", f"exceeded {meta['time_limit_seconds']}s", \
               time.monotonic() - start
    elapsed = time.monotonic() - start

    if proc.returncode != 0 or not proc.stdout.strip():
        try:
            err = json.loads(proc.stdout).get("error", "")
        except (json.JSONDecodeError, ValueError):
            err = (proc.stderr or proc.stdout).strip()[-400:]
        return "ERROR", err, elapsed

    result = json.loads(proc.stdout)["result"]
    oi = case.get("order_insensitive", False)
    if normalise(result, oi) == normalise(case["expected"], oi):
        return "PASS", None, elapsed
    return "FAIL", f"expected {case['expected']!r}, got {result!r}", elapsed


def test_question(module, slug, q_dir, only_case=None, target_file=USER_SOLUTION_FILE,
                  mark_solved=False):
    meta = load_meta(q_dir)
    cases = json.loads((q_dir / "tests" / "cases.json").read_text())
    if not (q_dir / target_file).exists():
        print(f"{YELLOW}∅ {slug}: no {target_file} yet{RESET}")
        return None

    harness_file = Path(tempfile.gettempdir()) / "flightcode-harness.py"
    harness_file.write_text(HARNESS)

    print(f"{BOLD}{module}/{slug}{RESET} "
          f"{DIM}({target_file}, {meta['difficulty']}, "
          f"{meta['time_limit_seconds']}s limit){RESET}")
    passed = 0
    selected = [(i, c) for i, c in enumerate(cases)
                if only_case is None or i == only_case]
    if not selected:
        label = "no cases" if only_case is None else f"case {only_case} not found"
        print(f"{YELLOW}∅ {slug}: {label}{RESET}")
        return False
    for i, case in selected:
        status, detail, elapsed = run_case(
            q_dir, meta, case, harness_file, target_file)
        if status == "PASS":
            passed += 1
            print(f"  {GREEN}✓{RESET} case {i} {DIM}({elapsed:.3f}s){RESET}")
        else:
            colour = YELLOW if status == "TIMEOUT" else RED
            print(f"  {colour}✗ case {i} [{status}]{RESET} {detail}")
            if "input" in case and status != "TIMEOUT":
                print(f"    {DIM}input: {json.dumps(case['input'])[:200]}{RESET}")
    total = len(selected)
    ok = passed == total
    colour = GREEN if ok else RED
    print(f"  {colour}{passed}/{total} passed{RESET}\n")
    if ok and mark_solved:
        (q_dir / ".solved").touch()
        print(f"{GREEN}Marked solved.{RESET}")
    return ok


def cmd_list(args):
    rows = []
    for module, slug, q_dir in discover():
        meta = load_meta(q_dir)
        if args.module and module != args.module:
            continue
        if args.difficulty and meta["difficulty"] != args.difficulty:
            continue
        solved = "●" if (q_dir / ".solved").exists() else "○"
        rows.append((module, slug, meta["difficulty"], solved))
    if not rows:
        print("No questions found.")
        return
    current_module = None
    for module, slug, diff, solved in rows:
        if module != current_module:
            print(f"\n{BOLD}{module}{RESET}")
            current_module = module
        print(f"  {solved} {slug:<30} {DIM}{diff}{RESET}")
    print()


def cmd_test(args):
    if args.all:
        results = {}
        for module, slug, q_dir in discover():
            if args.module and module != args.module:
                continue
            results[f"{module}/{slug}"] = test_question(module, slug, q_dir)
        print_summary(results)
        return
    module, slug, q_dir = find_question(args.slug)
    test_question(module, slug, q_dir, only_case=args.case, mark_solved=True)


def print_summary(results):
    attempted = {k: v for k, v in results.items() if v is not None}
    print(f"{BOLD}Summary:{RESET} "
          f"{sum(1 for v in attempted.values() if v)}/{len(attempted)} "
          f"questions fully passing "
          f"{DIM}({len(results) - len(attempted)} unattempted){RESET}")


def cmd_test_solutions(args):
    if args.all or not args.slug:
        results = {}
        for module, slug, q_dir in discover():
            if args.module and module != args.module:
                continue
            results[f"{module}/{slug}"] = test_question(
                module, slug, q_dir, target_file=REFERENCE_SOLUTION_FILE)
        print_summary(results)
        return
    module, slug, q_dir = find_question(args.slug)
    test_question(
        module, slug, q_dir, only_case=args.case,
        target_file=REFERENCE_SOLUTION_FILE)


def cmd_status(args):
    by_module = {}
    for module, slug, q_dir in discover():
        solved = (q_dir / ".solved").exists()
        by_module.setdefault(module, []).append(solved)
    if not by_module:
        print("No questions yet.")
        return
    print()
    for module, flags in by_module.items():
        done, total = sum(flags), len(flags)
        bar = "█" * done + "░" * (total - done)
        print(f"  {module:<20} {bar} {done}/{total}")
    print()


def cmd_reset_completion(args):
    if args.all:
        reset = 0
        total = 0
        for module, slug, q_dir in discover():
            if args.module and module != args.module:
                continue
            total += 1
            marker = q_dir / ".solved"
            if marker.exists():
                marker.unlink()
                reset += 1
        scope = f"module '{args.module}'" if args.module else "all questions"
        print(f"Reset completion for {reset}/{total} questions in {scope}.")
        return

    module, slug, q_dir = find_question(args.slug)
    marker = q_dir / ".solved"
    if marker.exists():
        marker.unlink()
        print(f"Reset completion for {module}/{slug}.")
    else:
        print(f"{module}/{slug} was not marked solved.")


TEMPLATE_META = {"difficulty": "medium", "time_limit_seconds": 5,
                 "function": "solve"}
TEMPLATE_QUESTION = "# {title}\n\n**Difficulty:** medium\n\n## Problem\n\nTODO\n\n## Examples\n\n```\nInput: \nOutput: \n```\n\n## Constraints\n\n- TODO\n"
TEMPLATE_CODE = "def solve():\n    pass\n"
TEMPLATE_REFERENCE = "# Example solution. Replace this with a complete reference answer.\n\n\ndef solve():\n    pass\n"
TEMPLATE_CASES = []


def cmd_new(args):
    if "/" not in args.path:
        sys.exit("Format: ./run.py new <module>/<slug>")
    module, slug = args.path.split("/", 1)
    q_dir = QUESTIONS / module / slug
    if q_dir.exists():
        sys.exit(f"{q_dir} already exists")
    (q_dir / "tests").mkdir(parents=True)
    (q_dir / "meta.json").write_text(json.dumps(TEMPLATE_META, indent=2))
    title = slug.replace("-", " ").title()
    (q_dir / "QUESTION.md").write_text(TEMPLATE_QUESTION.format(title=title))
    (q_dir / USER_SOLUTION_FILE).write_text(TEMPLATE_CODE)
    (q_dir / REFERENCE_SOLUTION_FILE).write_text(TEMPLATE_REFERENCE)
    (q_dir / "tests" / "cases.json").write_text(
        json.dumps(TEMPLATE_CASES, indent=2))
    print(f"Scaffolded {q_dir}")


def cmd_agent_prompt(args):
    if "/" not in args.path:
        sys.exit("Format: ./run.py agent-prompt <module>/<slug>")
    module, slug = args.path.split("/", 1)
    title = args.title or slug.replace("-", " ").title()
    prompt = f"""Add a new Offline LeetCode question to this repo.

Target folder:
questions/{module}/{slug}/

Use exactly this shape:
- QUESTION.md
- meta.json
- code.py
- solution.py
- tests/cases.json

Problem title: {title}

Requirements:
- Read AGENTS.md first and follow the repository contract.
- Put the complete problem statement in QUESTION.md with examples and constraints.
- Set meta.json with difficulty, time_limit_seconds, and function.
- Implement a correct reference/example solution in solution.py using the function named in meta.json.
- Create code.py with the same function signature as a starter for the user. Leave the body blank/pass.
- Add 5-8 deterministic JSON test cases in tests/cases.json.
- Update questions.md with the question title, slug, difficulty, and pattern.
- Cover edge cases such as empty/minimal input when allowed, duplicates, negatives, ties, and max-shape cases relevant to the problem.
- Use order_insensitive only for list outputs where order should not matter.
- Run ./run.py test-solutions {slug} to verify solution.py.
- Run ./run.py test {slug} and fix any failures when code.py contains the intended working solution.
- Do not edit unrelated questions.
"""
    print(prompt)


def main():
    p = argparse.ArgumentParser(description="Offline LeetCode runner")
    sub = p.add_subparsers(dest="cmd", required=True)

    pl = sub.add_parser("list")
    pl.add_argument("--module")
    pl.add_argument("--difficulty", choices=["easy", "medium", "hard"])
    pl.set_defaults(fn=cmd_list)

    pt = sub.add_parser("test")
    pt.add_argument("slug", nargs="?")
    pt.add_argument("--all", action="store_true")
    pt.add_argument("--module")
    pt.add_argument("--case", type=int)
    pt.set_defaults(fn=cmd_test)

    pts = sub.add_parser(
        "test-solutions", aliases=["test_solutions"],
        help="run tests against solution.py instead of code.py")
    pts.add_argument("slug", nargs="?")
    pts.add_argument("--all", action="store_true")
    pts.add_argument("--module")
    pts.add_argument("--case", type=int)
    pts.set_defaults(fn=cmd_test_solutions)

    ps = sub.add_parser("status")
    ps.set_defaults(fn=cmd_status)

    pr = sub.add_parser(
        "reset-completion", aliases=["reset_completion"],
        help="clear .solved markers")
    pr.add_argument("slug", nargs="?")
    pr.add_argument("--all", action="store_true")
    pr.add_argument("--module")
    pr.set_defaults(fn=cmd_reset_completion)

    pn = sub.add_parser("new")
    pn.add_argument("path", help="<module>/<slug>")
    pn.set_defaults(fn=cmd_new)

    pa = sub.add_parser("agent-prompt")
    pa.add_argument("path", help="<module>/<slug>")
    pa.add_argument("--title")
    pa.set_defaults(fn=cmd_agent_prompt)

    args = p.parse_args()
    if args.cmd == "test" and not args.all and not args.slug:
        p.error("provide a slug or --all")
    if args.cmd in ("reset-completion", "reset_completion") and not args.all \
            and not args.slug:
        p.error("provide a slug or --all")
    args.fn(args)


if __name__ == "__main__":
    main()
