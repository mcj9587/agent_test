"""
KPI Dashboard Module
- Weekly/monthly KPI tracking
- Persistent KPI data storage
- Progress visualization
"""

import json
import os
from datetime import datetime

from k_wellness_agent.data.business_plan import KPI_CATEGORIES

EXPORT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "exports")
KPI_FILE = os.path.join(EXPORT_DIR, "kpi_data.json")


def _load_kpi_data():
    """Load persisted KPI data."""
    if os.path.exists(KPI_FILE):
        with open(KPI_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"entries": [], "weekly": []}


def _save_kpi_data(data):
    """Save KPI data."""
    os.makedirs(EXPORT_DIR, exist_ok=True)
    with open(KPI_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def print_kpi_framework():
    """Display the full KPI tracking framework."""
    print("\n" + "=" * 80)
    print("  KPI Tracking Framework")
    print("=" * 80)

    for cat_key, cat_data in KPI_CATEGORIES.items():
        print(f"\n  --- {cat_data['label']} ---")
        print(f"  {'Metric':<25} | {'Monthly Target':<20} | {'Unit':<6}")
        print(f"  {'─'*60}")
        for metric in cat_data["metrics"]:
            print(f"  {metric['name']:<25} | {metric['target_monthly']:<20} | {metric['unit']:<6}")

    print("\n" + "=" * 80)


def log_weekly_kpi(week_number, kpi_dict):
    """
    Log weekly KPI data.
    kpi_dict example: {
        "revenue": 50000000,
        "orders": 100,
        "meetings": 5,
        "pos": 1,
        "content_count": 8,
        "ugc_count": 3,
        "email_list": 500,
        "followers": 1200
    }
    """
    data = _load_kpi_data()
    entry = {
        "week": week_number,
        "date": datetime.now().isoformat(),
        "kpis": kpi_dict,
    }

    existing = next((i for i, e in enumerate(data["weekly"]) if e["week"] == week_number), None)
    if existing is not None:
        data["weekly"][existing] = entry
    else:
        data["weekly"].append(entry)

    data["weekly"].sort(key=lambda x: x["week"])
    _save_kpi_data(data)
    print(f"  OK: Week {week_number} KPI saved")


def print_weekly_summary():
    """Display weekly KPI summary with trend."""
    data = _load_kpi_data()
    weekly = data.get("weekly", [])

    if not weekly:
        print("\n  No KPI data recorded yet.")
        print("  Use 'kpi log <week> <metric>=<value>' to record data.")
        print("  Example: kpi log 1 revenue=50000000 orders=100 meetings=5")
        return

    print("\n" + "=" * 80)
    print("  Weekly KPI Summary")
    print("=" * 80)

    all_metrics = set()
    for w in weekly:
        all_metrics.update(w["kpis"].keys())

    metrics_list = sorted(all_metrics)

    header = f"  {'Metric':<18}"
    for w in weekly[-8:]:
        header += f" | {'W'+str(w['week']):>10}"
    print(header)
    print(f"  {'─'*len(header)}")

    for metric in metrics_list:
        row = f"  {metric:<18}"
        prev_val = None
        for w in weekly[-8:]:
            val = w["kpis"].get(metric, "-")
            if val != "-" and prev_val is not None and prev_val != "-":
                if val > prev_val:
                    trend = " ^"
                elif val < prev_val:
                    trend = " v"
                else:
                    trend = " ="
            else:
                trend = "  "
            if isinstance(val, (int, float)) and val >= 1000000:
                display = f"{val/1000000:.1f}M"
            elif isinstance(val, (int, float)):
                display = f"{val:,}"
            else:
                display = str(val)
            row += f" | {display:>8}{trend}"
            prev_val = val
        print(row)

    print("\n" + "=" * 80)


def print_kpi_input_guide():
    """Show guide for inputting KPI data."""
    print("\n" + "=" * 80)
    print("  KPI Input Guide")
    print("=" * 80)

    print("""
  Available KPI metrics:

  Sales/Orders:
    revenue       - Monthly revenue (KRW)
    orders        - Order count
    aov           - Average order value (KRW)
    subscribers   - Subscriber count

  Wholesale/B2B:
    meetings      - Buyer meeting count
    pos           - PO (Purchase Order) count
    po_amount     - PO total amount (KRW)
    accounts      - Account count

  Marketing/Content:
    content_count - Published content count
    ugc_count     - UGC count
    email_list    - Email list size
    followers     - SNS follower count

  Financial:
    gross_margin  - Gross margin (%)
    cac           - Customer acquisition cost (KRW)
    ltv           - Customer lifetime value (KRW)
    cash_flow     - Cash flow (KRW)

  Examples:
    kpi log 1 revenue=50000000 orders=100 meetings=5
    kpi log 2 revenue=80000000 orders=180 meetings=8 content_count=15
""")


def export_kpi_report():
    """Export KPI data to a report file."""
    data = _load_kpi_data()
    os.makedirs(EXPORT_DIR, exist_ok=True)

    filepath = os.path.join(EXPORT_DIR, "kpi_report.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"  KPI report exported: {filepath}")
    return filepath
