#!/usr/bin/env python3
"""
GTeam Skill Evaluation Matrix Runner

Runs evaluation scenarios using `claude -p` (CLI subscription) to test each
specialist's SKILL.md against realistic tasks, then judges the output quality.
No API key required — uses your Claude subscription via the CLI.

Usage:
    python scripts/skill-eval-matrix.py                          # Run all specialists
    python scripts/skill-eval-matrix.py --specialist accountant   # Run specific specialist(s)
    python scripts/skill-eval-matrix.py --difficulty standard     # Filter by difficulty
    python scripts/skill-eval-matrix.py --history                 # Show trends
    python scripts/skill-eval-matrix.py --dry-run                 # Show scenarios only
    python scripts/skill-eval-matrix.py --concurrency 4           # Run 4 scenarios in parallel
    python scripts/skill-eval-matrix.py --runs 3                  # pass@k scoring (3 runs each)
    python scripts/skill-eval-matrix.py --baseline latest         # Compare against previous run
"""

import argparse
import asyncio
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
GTEAM_DIR = Path(__file__).resolve().parent.parent
SPECIALISTS_DIR = GTEAM_DIR / "specialists"
RESULTS_DIR = Path.home() / ".gteam-dev" / "evals" / "matrix"

SCENARIO_TIMEOUT = 300  # seconds per claude -p call
VERSION = "2.0.0"

# ---------------------------------------------------------------------------
# Tiered gates
# ---------------------------------------------------------------------------
GATES = {
    "relevance": {"threshold": 70, "tier": "CRITICAL"},
    "completeness": {"threshold": 70, "tier": "HIGH"},
    "actionability": {"threshold": 65, "tier": "HIGH"},
    "methodology_alignment": {"threshold": 70, "tier": "CRITICAL"},
}

PASS_THRESHOLD = 70  # average score >= this means a scenario "passes"

# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------

EXECUTE_PROMPT_TEMPLATE = """You are a professional specialist. Your skill instructions are below.

<skill>
{skill_content}
</skill>

Execute the following task using your skill methodology. Produce a complete, professional deliverable.

TASK: {task}"""

JUDGE_PROMPT_TEMPLATE = """You are a strict evaluator assessing specialist skill output quality.

TASK GIVEN TO SPECIALIST: {task}

EXPECTED CRITERIA:
{expect}

SPECIALIST OUTPUT:
{response}

Score this output on 4 dimensions (0-100). Be critical — only score 90+ for exceptional work:
- relevance: Does the output directly address the specific task asked?
- completeness: Does the output satisfy ALL expected criteria listed above?
- actionability: Are recommendations specific, concrete, and implementable (not vague advice)?
- methodology_alignment: Does the output follow professional best practices for this domain?

Also note:
- issues: List specific problems, gaps, or areas for improvement

Respond in JSON format ONLY (no other text):
{{"relevance": N, "completeness": N, "actionability": N, "methodology_alignment": N, "issues": ["...", "..."]}}"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def discover_scenarios(
    specialists: Optional[List[str]] = None,
    difficulty: Optional[str] = None,
) -> Dict[str, List[dict]]:
    """Discover and load scenarios from specialists/*/evals/scenarios.json."""
    result: Dict[str, List[dict]] = {}

    for spec_dir in sorted(SPECIALISTS_DIR.iterdir()):
        if not spec_dir.is_dir():
            continue
        name = spec_dir.name
        if specialists and name not in specialists:
            continue
        scenarios_file = spec_dir / "evals" / "scenarios.json"
        if not scenarios_file.exists():
            continue
        try:
            scenarios = json.loads(scenarios_file.read_text())
        except (json.JSONDecodeError, OSError) as exc:
            print(f"  WARNING: Failed to load {scenarios_file}: {exc}")
            continue

        if difficulty:
            scenarios = [s for s in scenarios if s.get("difficulty") == difficulty]

        if scenarios:
            result[name] = scenarios

    return result


def load_skill_content(specialist_name: str) -> str:
    """Load the SKILL.md content for a specialist."""
    skill_path = SPECIALISTS_DIR / specialist_name / "SKILL.md"
    if not skill_path.exists():
        return ""
    content = skill_path.read_text()
    # Cap at 12K chars to stay within reasonable prompt size
    if len(content) > 12000:
        content = content[:12000] + "\n\n[... truncated for evaluation ...]"
    return content


def run_claude_cli(prompt: str, timeout: int = SCENARIO_TIMEOUT) -> str:
    """Run a prompt through `claude -p` and return the response text."""
    try:
        result = subprocess.run(
            ["claude", "-p", prompt],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        if result.returncode != 0:
            stderr = result.stderr.strip()[:200]
            return f"[CLI ERROR: exit code {result.returncode}] {stderr}"
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return f"[TIMEOUT after {timeout}s]"
    except FileNotFoundError:
        return "[ERROR: claude CLI not found. Install Claude Code first.]"
    except Exception as exc:
        return f"[ERROR: {exc}]"


async def run_scenario_cli(
    specialist_name: str,
    scenario: dict,
) -> dict:
    """Execute a scenario via claude -p with the specialist's SKILL.md as context."""
    skill_content = load_skill_content(specialist_name)
    if not skill_content:
        return {
            "status": "error",
            "error": f"No SKILL.md found for {specialist_name}",
            "response": "",
            "execution_time": 0,
        }

    prompt = EXECUTE_PROMPT_TEMPLATE.format(
        skill_content=skill_content,
        task=scenario["task"],
    )

    start = time.monotonic()
    # Run in thread to not block the event loop
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, run_claude_cli, prompt)
    elapsed = time.monotonic() - start

    if response.startswith("[") and ("ERROR" in response or "TIMEOUT" in response):
        return {
            "status": "error",
            "error": response,
            "response": "",
            "execution_time": round(elapsed, 1),
        }

    return {
        "status": "success",
        "response": response,
        "execution_time": round(elapsed, 1),
    }


def judge_output_cli(
    scenario: dict,
    response_text: str,
) -> dict:
    """Use claude -p to judge output quality. Returns scores dict."""
    expect_str = "\n".join(f"- {e}" for e in scenario.get("expect", []))
    prompt = JUDGE_PROMPT_TEMPLATE.format(
        task=scenario["task"],
        expect=expect_str,
        response=response_text[:8000],
    )

    for attempt in range(2):
        raw = run_claude_cli(prompt, timeout=60)

        if raw.startswith("[") and "ERROR" in raw:
            if attempt == 0:
                print(f"    Judge retry ({raw[:50]})")
                continue
            return {
                "relevance": None, "completeness": None,
                "actionability": None, "methodology_alignment": None,
                "issues": [f"Judge error: {raw}"],
            }

        try:
            # Strip markdown code fences if present
            cleaned = raw.strip()
            if cleaned.startswith("```"):
                cleaned = cleaned.split("\n", 1)[1] if "\n" in cleaned else cleaned[3:]
                if cleaned.endswith("```"):
                    cleaned = cleaned[:-3]
                cleaned = cleaned.strip()
            return json.loads(cleaned)
        except json.JSONDecodeError as exc:
            if attempt == 0:
                print(f"    Judge retry (JSON parse error)")
                continue
            print(f"    Judge failed: {exc}")
            return {
                "relevance": None, "completeness": None,
                "actionability": None, "methodology_alignment": None,
                "issues": [f"Judge parse error: {raw[:100]}"],
            }


def _run_avg_score(run_scores: dict) -> float:
    """Compute the average of the 4 dimension scores for a single run."""
    dims = ["relevance", "completeness", "actionability", "methodology_alignment"]
    vals = [run_scores.get(d) for d in dims if run_scores.get(d) is not None]
    return round(sum(vals) / len(vals), 1) if vals else 0


def _scenario_passes(run_scores: dict) -> bool:
    """A run passes if its average score >= PASS_THRESHOLD."""
    return _run_avg_score(run_scores) >= PASS_THRESHOLD


def compute_averages(scenario_results: List[dict]) -> dict:
    """Compute average scores across a list of scenario results."""
    dims = ["relevance", "completeness", "actionability", "methodology_alignment"]
    totals = {d: [] for d in dims}

    for sr in scenario_results:
        # Support both legacy flat scores and new multi-run avg_scores
        scores = sr.get("avg_scores") or sr.get("scores", {})
        for d in dims:
            v = scores.get(d)
            if v is not None:
                totals[d].append(v)

    averages = {}
    for d in dims:
        averages[d] = round(sum(totals[d]) / len(totals[d]), 1) if totals[d] else 0

    return averages


def compute_overall(averages: dict) -> float:
    dims = ["relevance", "completeness", "actionability", "methodology_alignment"]
    vals = [averages.get(d, 0) for d in dims]
    return round(sum(vals) / len(vals), 2) if vals else 0


def save_results(run_data: dict) -> Path:
    """Save full results and append to history."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    # Full results file
    ts = run_data["timestamp"].replace(":", "-")
    full_path = RESULTS_DIR / f"{ts}.json"
    full_path.write_text(json.dumps(run_data, indent=2))

    # Append to history
    history_path = RESULTS_DIR / "history.json"
    history: list = []
    if history_path.exists():
        try:
            history = json.loads(history_path.read_text())
        except (json.JSONDecodeError, OSError):
            history = []

    for spec_name, spec_data in run_data.get("specialists", {}).items():
        avgs = spec_data.get("averages", {})
        history.append({
            "timestamp": run_data["timestamp"],
            "specialist": spec_name,
            "overall": spec_data.get("overall", 0),
            "relevance": avgs.get("relevance", 0),
            "completeness": avgs.get("completeness", 0),
            "actionability": avgs.get("actionability", 0),
            "methodology_alignment": avgs.get("methodology_alignment", 0),
        })

    history_path.write_text(json.dumps(history, indent=2))
    return full_path


def load_baseline(baseline_arg: str) -> Optional[dict]:
    """Load a baseline results file for regression comparison."""
    if not RESULTS_DIR.exists():
        return None

    if baseline_arg == "latest":
        # Find the most recent .json file (excluding history.json)
        candidates = [
            f for f in sorted(RESULTS_DIR.iterdir())
            if f.suffix == ".json" and f.name != "history.json"
        ]
        if not candidates:
            return None
        target = candidates[-1]
    else:
        # Try exact filename or timestamp match
        target = RESULTS_DIR / f"{baseline_arg}.json"
        if not target.exists():
            # Try with colons replaced
            target = RESULTS_DIR / f"{baseline_arg.replace(':', '-')}.json"
        if not target.exists():
            # Partial match
            candidates = [
                f for f in sorted(RESULTS_DIR.iterdir())
                if f.suffix == ".json" and f.name != "history.json"
                and baseline_arg in f.name
            ]
            if candidates:
                target = candidates[-1]
            else:
                return None

    if not target.exists():
        return None

    try:
        return json.loads(target.read_text())
    except (json.JSONDecodeError, OSError):
        return None


def print_dashboard(run_data: dict, baseline: Optional[dict] = None) -> None:
    """Print the summary dashboard to stdout."""
    ts = run_data["timestamp"][:10]
    num_runs = run_data.get("num_runs", 1)
    print()
    title = f"GTeam Skill Evaluation Matrix -- {ts}"
    if num_runs > 1:
        title += f" (pass@k, {num_runs} runs)"
    print(title)
    print("=" * 70)

    # Build header
    if baseline:
        header = f"  {'Specialist':<22} {'Overall':>7}  {'D':>5}  {'Rel':>4}  {'Comp':>4}  {'Act':>4}  {'Meth':>4}"
    else:
        header = f"  {'Specialist':<22} {'Overall':>7}  {'Rel':>4}  {'Comp':>4}  {'Act':>4}  {'Meth':>4}"
    print(header)
    print("  " + "-" * (66 if baseline else 56))

    ranking = run_data.get("ranking", [])
    all_scores = {"relevance": [], "completeness": [], "actionability": [], "methodology_alignment": []}

    # Pre-compute baseline overalls
    baseline_overalls = {}
    if baseline:
        for name, spec_data in baseline.get("specialists", {}).items():
            baseline_overalls[name] = spec_data.get("overall", 0)

    for entry in ranking:
        name = entry["specialist"]
        spec = run_data["specialists"][name]
        avgs = spec["averages"]

        for dim in all_scores:
            v = avgs.get(dim, 0)
            if v:
                all_scores[dim].append(v)

        if baseline:
            b_overall = baseline_overalls.get(name)
            if b_overall is not None:
                delta = entry["overall"] - b_overall
                delta_str = f"{delta:>+5.1f}"
            else:
                delta_str = "  new"
            print(
                f"  {name:<22} {entry['overall']:>7.1f}  {delta_str}"
                f"  {avgs.get('relevance', 0):>4.0f}  {avgs.get('completeness', 0):>4.0f}"
                f"  {avgs.get('actionability', 0):>4.0f}  {avgs.get('methodology_alignment', 0):>4.0f}"
            )
        else:
            print(
                f"  {name:<22} {entry['overall']:>7.1f}  {avgs.get('relevance', 0):>4.0f}"
                f"  {avgs.get('completeness', 0):>4.0f}  {avgs.get('actionability', 0):>4.0f}"
                f"  {avgs.get('methodology_alignment', 0):>4.0f}"
            )

    print("  " + "-" * (66 if baseline else 56))

    # Averages row
    avg_overall = round(sum(e["overall"] for e in ranking) / len(ranking), 1) if ranking else 0
    avg_dims = {}
    for dim in all_scores:
        vals = all_scores[dim]
        avg_dims[dim] = round(sum(vals) / len(vals), 0) if vals else 0

    if baseline:
        print(
            f"  {'AVERAGE':<22} {avg_overall:>7.1f}       "
            f"{avg_dims.get('relevance', 0):>4.0f}  {avg_dims.get('completeness', 0):>4.0f}"
            f"  {avg_dims.get('actionability', 0):>4.0f}  {avg_dims.get('methodology_alignment', 0):>4.0f}"
        )
    else:
        print(
            f"  {'AVERAGE':<22} {avg_overall:>7.1f}  {avg_dims.get('relevance', 0):>4.0f}"
            f"  {avg_dims.get('completeness', 0):>4.0f}  {avg_dims.get('actionability', 0):>4.0f}"
            f"  {avg_dims.get('methodology_alignment', 0):>4.0f}"
        )
    print()

    # pass@k summary when runs > 1
    if num_runs > 1:
        print(f"  pass@k summary ({num_runs} runs per scenario):")
        for name in [e["specialist"] for e in ranking]:
            spec = run_data["specialists"][name]
            scenarios = spec.get("scenarios", [])
            total = len(scenarios)
            p1 = sum(1 for s in scenarios if s.get("pass_at_1", False))
            pk = sum(1 for s in scenarios if s.get("pass_at_k", False))
            pa = sum(1 for s in scenarios if s.get("pass_all_k", False))
            print(f"    {name:<22} pass@1: {p1}/{total}  pass@{num_runs}: {pk}/{total}  pass^{num_runs}: {pa}/{total}")
        print()

    # Weakest / strongest
    if ranking:
        weakest = ranking[-1]
        strongest = ranking[0]
        w_spec = run_data["specialists"][weakest["specialist"]]
        print(f"  Weakest:   {weakest['specialist']} ({weakest.get('weakest_dimension', '?')}: "
              f"{_weakest_score(w_spec)})")
        print(f"  Strongest: {strongest['specialist']} (overall: {strongest['overall']})")

    # Regression recommendation
    if baseline:
        print()
        print("  Regression analysis:")
        for entry in ranking:
            name = entry["specialist"]
            b_overall = baseline_overalls.get(name)
            if b_overall is None:
                print(f"    {name}: NEW (no baseline)")
                continue
            delta = entry["overall"] - b_overall
            if delta > 0:
                print(f"    {name}: promote (delta {delta:+.1f})")
            elif delta < -5:
                print(f"    {name}: INVESTIGATE (delta {delta:+.1f})")
            else:
                print(f"    {name}: stable (delta {delta:+.1f})")

    # Recommendations with tiered gates
    print()
    print("  Recommendations:")
    recs = _generate_recommendations(run_data)
    if recs:
        for r in recs:
            print(f"  - {r}")
    else:
        print("  - All specialists above threshold. No fixes needed.")
    print()


def _weakest_score(spec_data: dict) -> float:
    avgs = spec_data.get("averages", {})
    dims = ["relevance", "completeness", "actionability", "methodology_alignment"]
    scores = [(d, avgs.get(d, 0)) for d in dims]
    scores.sort(key=lambda x: x[1])
    return scores[0][1] if scores else 0


def _generate_recommendations(run_data: dict) -> List[str]:
    recs = []

    for name, spec_data in run_data.get("specialists", {}).items():
        avgs = spec_data.get("averages", {})

        for dim, gate in GATES.items():
            score = avgs.get(dim, 0)
            threshold = gate["threshold"]
            tier = gate["tier"]
            if score and score < threshold:
                recs.append(f"[{tier}] FIX {name}: {dim} below threshold ({score} < {threshold})")

    # Sort by tier priority: CRITICAL first, then HIGH
    tier_order = {"CRITICAL": 0, "HIGH": 1}
    recs.sort(key=lambda r: tier_order.get(r.split("]")[0].strip("["), 99))

    return recs


def print_history() -> None:
    """Print historical trend data."""
    history_path = RESULTS_DIR / "history.json"
    if not history_path.exists():
        print("No history found. Run an evaluation first.")
        return

    history = json.loads(history_path.read_text())
    if not history:
        print("History is empty.")
        return

    # Group by timestamp
    runs: Dict[str, List[dict]] = {}
    for entry in history:
        ts = entry["timestamp"][:19]  # group by second
        runs.setdefault(ts, []).append(entry)

    print()
    print("GTeam Evaluation History")
    print("=" * 65)

    for ts in sorted(runs.keys()):
        entries = runs[ts]
        avg_overall = sum(e["overall"] for e in entries) / len(entries) if entries else 0
        n_specs = len(entries)
        print(f"  {ts}  |  {n_specs} specialists  |  avg overall: {avg_overall:.1f}")

        for e in sorted(entries, key=lambda x: -x["overall"]):
            print(f"    {e['specialist']:<22} {e['overall']:>6.1f}  "
                  f"(R:{e['relevance']:.0f} C:{e['completeness']:.0f} "
                  f"A:{e['actionability']:.0f} M:{e['methodology_alignment']:.0f})")
        print()


def print_dry_run(all_scenarios: Dict[str, List[dict]], num_runs: int = 1) -> None:
    """Print scenarios without executing."""
    total = sum(len(s) for s in all_scenarios.values())
    title = f"GTeam Eval Matrix -- Dry Run ({total} scenarios across {len(all_scenarios)} specialists)"
    if num_runs > 1:
        title += f" x {num_runs} runs each"
    print()
    print(title)
    print("=" * 65)

    for name, scenarios in sorted(all_scenarios.items()):
        print(f"\n  {name} ({len(scenarios)} scenarios):")
        for s in scenarios:
            diff = s.get("difficulty", "standard")
            task_preview = s["task"][:70]
            print(f"    [{diff:<10}] {s['id']}: {task_preview}...")
            if s.get("expect"):
                for exp in s["expect"]:
                    print(f"               - {exp[:75]}")
    print()


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------

async def run_matrix(
    specialists: Optional[List[str]] = None,
    difficulty: Optional[str] = None,
    concurrency: int = 2,
    num_runs: int = 1,
    baseline_arg: Optional[str] = None,
) -> dict:
    """Run the full evaluation matrix."""
    all_scenarios = discover_scenarios(specialists, difficulty)
    if not all_scenarios:
        print("No scenarios found. Check specialists/*/evals/scenarios.json files.")
        sys.exit(1)

    total = sum(len(s) for s in all_scenarios.values())
    total_executions = total * num_runs
    print(f"\nGTeam Eval Matrix: {total} scenarios across {len(all_scenarios)} specialists")
    if num_runs > 1:
        print(f"  pass@k mode: {num_runs} runs per scenario ({total_executions} total executions)")
    print(f"Using: claude -p (CLI subscription) | concurrency: {concurrency}")
    print("=" * 60)

    # Verify claude CLI is available
    try:
        subprocess.run(["claude", "--version"], capture_output=True, timeout=5)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print("ERROR: `claude` CLI not found. Install Claude Code first.")
        sys.exit(1)

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    specialists_results: Dict[str, dict] = {}
    completed = 0
    errors = 0
    semaphore = asyncio.Semaphore(concurrency)

    async def execute_and_judge(spec_name: str, scenario: dict) -> dict:
        """Execute a scenario once and judge the result. Returns {scores, issues, execution_time, status}."""
        async with semaphore:
            result = await run_scenario_cli(spec_name, scenario)
            response_text = result.get("response", "")
            exec_time = result.get("execution_time", 0)

            if result.get("status") == "error":
                return {
                    "scores": {
                        "relevance": None, "completeness": None,
                        "actionability": None, "methodology_alignment": None,
                    },
                    "issues": [result.get("error", "execution error")],
                    "execution_time": exec_time,
                    "status": "error",
                }

            loop = asyncio.get_event_loop()
            judge_result = await loop.run_in_executor(
                None, judge_output_cli, scenario, response_text
            )

            scores = {
                "relevance": judge_result.get("relevance"),
                "completeness": judge_result.get("completeness"),
                "actionability": judge_result.get("actionability"),
                "methodology_alignment": judge_result.get("methodology_alignment"),
            }
            issues = judge_result.get("issues", [])

            return {
                "scores": scores,
                "issues": issues,
                "execution_time": exec_time,
                "status": "success",
            }

    async def run_single(spec_name: str, scenario: dict) -> dict:
        """Run a single scenario N times and produce the result record."""
        sid = scenario.get("id", "unknown")

        if num_runs == 1:
            # Legacy single-run path
            print(f"  [{spec_name}] {sid}...", end=" ", flush=True)
            run_result = await execute_and_judge(spec_name, scenario)
            exec_time = run_result["execution_time"]

            if run_result["status"] == "error":
                print(f"ERROR ({exec_time:.0f}s)")
                return {
                    "id": sid,
                    "task": scenario["task"],
                    "difficulty": scenario.get("difficulty", "standard"),
                    "scores": run_result["scores"],
                    "execution_time": exec_time,
                    "issues": run_result["issues"],
                    "status": "error",
                }

            avg = _run_avg_score(run_result["scores"])
            print(f"avg={avg} ({exec_time:.0f}s)")

            return {
                "id": sid,
                "task": scenario["task"],
                "difficulty": scenario.get("difficulty", "standard"),
                "scores": run_result["scores"],
                "execution_time": exec_time,
                "issues": run_result["issues"],
                "status": "success",
            }

        # Multi-run pass@k path
        print(f"  [{spec_name}] {sid} ({num_runs} runs)...", flush=True)
        runs_data = []
        total_time = 0

        for run_idx in range(num_runs):
            print(f"    run {run_idx + 1}/{num_runs}...", end=" ", flush=True)
            run_result = await execute_and_judge(spec_name, scenario)
            runs_data.append({
                "scores": run_result["scores"],
                "issues": run_result["issues"],
            })
            total_time += run_result["execution_time"]

            avg = _run_avg_score(run_result["scores"])
            status_tag = "PASS" if _scenario_passes(run_result["scores"]) else "FAIL"
            print(f"avg={avg} [{status_tag}] ({run_result['execution_time']:.0f}s)")

        # Compute aggregate scores across runs
        dims = ["relevance", "completeness", "actionability", "methodology_alignment"]
        avg_scores = {}
        for d in dims:
            vals = [r["scores"].get(d) for r in runs_data if r["scores"].get(d) is not None]
            avg_scores[d] = round(sum(vals) / len(vals), 1) if vals else None

        # pass@k metrics
        first_passes = _scenario_passes(runs_data[0]["scores"])
        any_passes = any(_scenario_passes(r["scores"]) for r in runs_data)
        all_pass = all(_scenario_passes(r["scores"]) for r in runs_data)

        overall_avg = _run_avg_score(avg_scores)
        pass_count = sum(1 for r in runs_data if _scenario_passes(r["scores"]))
        print(f"    => avg={overall_avg} pass@1={'Y' if first_passes else 'N'} "
              f"pass@{num_runs}={'Y' if any_passes else 'N'} "
              f"pass^{num_runs}={'Y' if all_pass else 'N'} ({pass_count}/{num_runs} passed)")

        return {
            "id": sid,
            "task": scenario["task"],
            "difficulty": scenario.get("difficulty", "standard"),
            "runs": runs_data,
            "pass_at_1": first_passes,
            "pass_at_k": any_passes,
            "pass_all_k": all_pass,
            "avg_scores": avg_scores,
            "execution_time": round(total_time, 1),
            "status": "success",
        }

    # Run all scenarios per specialist
    for spec_name, scenarios in sorted(all_scenarios.items()):
        print(f"\n--- {spec_name} ({len(scenarios)} scenarios) ---")

        tasks = [run_single(spec_name, s) for s in scenarios]
        scenario_results = await asyncio.gather(*tasks)

        for sr in scenario_results:
            if sr.get("status") == "error":
                errors += 1
            else:
                completed += 1

        averages = compute_averages(scenario_results)
        overall = compute_overall(averages)

        specialists_results[spec_name] = {
            "scenarios": scenario_results,
            "averages": averages,
            "overall": overall,
        }

    # Build ranking
    ranking = []
    for name, data in specialists_results.items():
        avgs = data["averages"]
        dims = ["relevance", "completeness", "actionability", "methodology_alignment"]
        weakest = min(dims, key=lambda d: avgs.get(d, 0)) if avgs else "unknown"
        ranking.append({
            "specialist": name,
            "overall": data["overall"],
            "weakest_dimension": weakest,
        })
    ranking.sort(key=lambda x: -x["overall"])

    run_data = {
        "timestamp": timestamp,
        "version": VERSION,
        "backend": "claude-cli",
        "num_runs": num_runs,
        "total_scenarios": total,
        "completed": completed,
        "errors": errors,
        "specialists": specialists_results,
        "ranking": ranking,
    }

    # Save and display
    saved_path = save_results(run_data)
    print(f"\nResults saved to {saved_path}")

    # Load baseline if requested
    baseline = None
    if baseline_arg:
        baseline = load_baseline(baseline_arg)
        if baseline:
            print(f"Baseline loaded: {baseline.get('timestamp', 'unknown')}")
        else:
            print(f"WARNING: Could not load baseline '{baseline_arg}'. Showing results without comparison.")

    print_dashboard(run_data, baseline)

    return run_data


def main():
    parser = argparse.ArgumentParser(
        description="GTeam Skill Evaluation Matrix Runner",
    )
    parser.add_argument(
        "--specialist", nargs="+",
        help="Run only specific specialist(s)",
    )
    parser.add_argument(
        "--difficulty", choices=["standard", "advanced", "edge-case"],
        help="Filter scenarios by difficulty level",
    )
    parser.add_argument(
        "--concurrency", type=int, default=2,
        help="Number of scenarios to run in parallel (default: 2)",
    )
    parser.add_argument(
        "--runs", type=int, default=1,
        help="Number of times to run each scenario for pass@k scoring (default: 1)",
    )
    parser.add_argument(
        "--baseline", type=str, default=None,
        help="Load a previous run for regression comparison (timestamp or 'latest')",
    )
    parser.add_argument(
        "--history", action="store_true",
        help="Show historical evaluation trends",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show scenarios without executing",
    )

    args = parser.parse_args()

    if args.history:
        print_history()
        return

    if args.dry_run:
        scenarios = discover_scenarios(args.specialist, args.difficulty)
        print_dry_run(scenarios, args.runs)
        return

    asyncio.run(run_matrix(
        args.specialist,
        args.difficulty,
        args.concurrency,
        args.runs,
        args.baseline,
    ))


if __name__ == "__main__":
    main()
