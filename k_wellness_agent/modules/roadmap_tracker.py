"""
Roadmap & Task Tracker Module
- Phase-based roadmap display
- Week-1 checklist management
- Task status updates with persistence
"""

import json
import os
from datetime import datetime, date

from k_wellness_agent.data.business_plan import ROADMAP, WEEK1_CHECKLIST

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "exports")
TRACKER_FILE = os.path.join(DATA_DIR, "task_tracker.json")


def _load_tracker():
    """Load task tracker from file."""
    if os.path.exists(TRACKER_FILE):
        with open(TRACKER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return _init_tracker()


def _save_tracker(data):
    """Save task tracker to file."""
    os.makedirs(DATA_DIR, exist_ok=True)
    data["updated_at"] = datetime.now().isoformat()
    with open(TRACKER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _init_tracker():
    """Initialize tracker with week-1 checklist and roadmap tasks."""
    tracker = {
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "week1_checklist": [
            {**item, "notes": "", "completed_at": None}
            for item in WEEK1_CHECKLIST
        ],
        "roadmap_status": {
            f"phase_{phase['phase']}": {
                "name": phase["name"],
                "period": phase["period"],
                "status": "pending" if phase["phase"] > 1 else "in_progress",
                "goals": [{"text": g, "done": False} for g in phase["goals"]],
                "deliverables": [{"text": d, "done": False} for d in phase["deliverables"]],
            }
            for phase in ROADMAP
        },
        "custom_tasks": [],
    }
    _save_tracker(tracker)
    return tracker


def get_current_phase():
    """Determine current roadmap phase based on today's date."""
    today = date.today()
    phase_dates = [
        (1, date(2026, 2, 1), date(2026, 3, 31)),
        (2, date(2026, 4, 1), date(2026, 5, 31)),
        (3, date(2026, 6, 1), date(2026, 8, 31)),
        (4, date(2026, 9, 1), date(2026, 12, 31)),
    ]
    for phase_num, start, end in phase_dates:
        if start <= today <= end:
            return phase_num
    return 1


def print_roadmap():
    """Display the full roadmap with status."""
    tracker = _load_tracker()
    current = get_current_phase()

    print("\n" + "=" * 80)
    print("  2026 10-Month Roadmap")
    print("=" * 80)

    for phase in ROADMAP:
        phase_key = f"phase_{phase['phase']}"
        is_current = phase["phase"] == current
        marker = " <-- CURRENT" if is_current else ""

        ps = tracker.get("roadmap_status", {}).get(phase_key, {})
        st = ps.get("status", "pending")
        if st == "completed":
            status = "[DONE]"
        elif st == "in_progress" or is_current:
            status = "[ACTIVE]"
        else:
            status = "[PENDING]"

        print(f"\n  {status} Phase {phase['phase']}: {phase['name']}{marker}")
        print(f"     Period: {phase['period']}")

        print(f"     Goals:")
        if phase_key in tracker.get("roadmap_status", {}):
            goals = tracker["roadmap_status"][phase_key]["goals"]
            for g in goals:
                mark = "[x]" if g["done"] else "[ ]"
                print(f"       {mark} {g['text']}")
        else:
            for g in phase["goals"]:
                print(f"       [ ] {g}")

        print(f"     Deliverables:")
        if phase_key in tracker.get("roadmap_status", {}):
            deliverables = tracker["roadmap_status"][phase_key]["deliverables"]
            for d in deliverables:
                mark = "[x]" if d["done"] else "[ ]"
                print(f"       {mark} {d['text']}")
        else:
            for d in phase["deliverables"]:
                print(f"       [ ] {d}")

    print("\n" + "=" * 80)


def print_week1_checklist():
    """Display week-1 checklist with status."""
    tracker = _load_tracker()
    checklist = tracker["week1_checklist"]

    done_count = sum(1 for item in checklist if item["status"] == "done")
    total = len(checklist)
    pct = (done_count / total * 100) if total > 0 else 0

    print("\n" + "=" * 80)
    print("  Week 1 Checklist (10 Action Items)")
    print("=" * 80)
    print(f"  Progress: {done_count}/{total} ({pct:.0f}%)")
    print(f"  {'─'*70}")

    for item in checklist:
        if item["status"] == "done":
            mark = "[x]"
        elif item["status"] == "in_progress":
            mark = "[>]"
        else:
            mark = "[ ]"
        print(f"  {mark} {item['id']:>2}. {item['task']}")
        if item.get("notes"):
            print(f"        Note: {item['notes']}")

    print()
    return checklist


def complete_task(task_id):
    """Mark a week-1 checklist task as done."""
    tracker = _load_tracker()
    for item in tracker["week1_checklist"]:
        if item["id"] == task_id:
            item["status"] = "done"
            item["completed_at"] = datetime.now().isoformat()
            _save_tracker(tracker)
            print(f"  OK: [{task_id}] {item['task']}")
            return
    print(f"  Error: Task #{task_id} not found.")


def uncomplete_task(task_id):
    """Revert a week-1 checklist task to pending."""
    tracker = _load_tracker()
    for item in tracker["week1_checklist"]:
        if item["id"] == task_id:
            item["status"] = "pending"
            item["completed_at"] = None
            _save_tracker(tracker)
            print(f"  Reverted: [{task_id}] {item['task']}")
            return
    print(f"  Error: Task #{task_id} not found.")


def add_custom_task(task_text):
    """Add a custom task to the tracker."""
    tracker = _load_tracker()
    custom = tracker.get("custom_tasks", [])
    new_id = max([t.get("id", 0) for t in custom], default=0) + 1
    custom.append({
        "id": new_id,
        "task": task_text,
        "status": "pending",
        "created_at": datetime.now().isoformat(),
        "completed_at": None,
    })
    tracker["custom_tasks"] = custom
    _save_tracker(tracker)
    print(f"  Added: [{new_id}] {task_text}")


def complete_custom_task(task_id):
    """Mark a custom task as done."""
    tracker = _load_tracker()
    for t in tracker.get("custom_tasks", []):
        if t["id"] == task_id:
            t["status"] = "done"
            t["completed_at"] = datetime.now().isoformat()
            _save_tracker(tracker)
            print(f"  OK: [{task_id}] {t['task']}")
            return
    print(f"  Error: Custom task #{task_id} not found.")


def print_custom_tasks():
    """Display custom tasks."""
    tracker = _load_tracker()
    custom = tracker.get("custom_tasks", [])

    if not custom:
        print("\n  No custom tasks yet. Use 'task add <text>' to create one.")
        return

    print("\n" + "=" * 80)
    print("  Custom Tasks")
    print("=" * 80)

    for t in custom:
        mark = "[x]" if t["status"] == "done" else "[ ]"
        print(f"  {mark} {t['id']:>2}. {t['task']}")
    print()


def reset_tasks():
    """Reset all tasks to initial state."""
    tracker = _init_tracker()
    print("  All tasks have been reset.")
