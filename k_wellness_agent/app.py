#!/usr/bin/env python3
"""
K-Wellness Agent Bot
====================
Korean Wellness / K-Beauty / K-Food Business Execution Agent

An interactive CLI application for managing and executing the
K-Glow business plan targeting 100억 KRW revenue in 2026.

Usage:
    python -m k_wellness_agent.app
    # or
    python k_wellness_agent/app.py
"""

import sys
import os

# Ensure project root is in path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k_wellness_agent.modules.financial_model import (
    run_financial_dashboard,
    print_margin_analysis,
    print_projection,
    revenue_projection,
    default_aggressive_projection,
    format_krw,
)
from k_wellness_agent.modules.roadmap_tracker import (
    print_roadmap,
    print_week1_checklist,
    complete_task,
    uncomplete_task,
    add_custom_task,
    complete_custom_task,
    print_custom_tasks,
    reset_tasks,
    get_current_phase,
)
from k_wellness_agent.modules.templates import (
    generate_all_templates,
    generate_line_sheet,
    generate_buyer_pitch_script,
    generate_email_templates,
    generate_brand_story_1pager,
    generate_founder_story_worksheet,
)
from k_wellness_agent.modules.compliance import (
    check_marketing_copy,
    print_compliance_overview,
    print_supplement_checklist,
    print_cosmetics_checklist,
)
from k_wellness_agent.modules.content_planner import (
    print_content_calendar,
    print_content_by_pillar,
    print_this_week_content,
    generate_content_brief,
    export_content_calendar,
)
from k_wellness_agent.modules.kpi_dashboard import (
    print_kpi_framework,
    log_weekly_kpi,
    print_weekly_summary,
    print_kpi_input_guide,
    export_kpi_report,
)
from k_wellness_agent.data.business_plan import (
    THREE_TRACKS,
    POSITIONING_ADVANTAGES,
    HERO_PRODUCTS,
    OFFER_TIERS,
    PRICE_AMPLIFIERS,
    REVENUE_TARGET_KRW,
    CHANNEL_MIX,
)


BANNER = r"""
 ┌─────────────────────────────────────────────────────────────┐
 │                                                             │
 │   K-Wellness Agent Bot  v1.0                                │
 │   Korean Wellness / K-Beauty / K-Food Business Agent        │
 │                                                             │
 │   Target: 100억 KRW Revenue | 50억 KRW Assets | 2026       │
 │                                                             │
 │   Type 'help' for available commands                        │
 │   Type 'quit' to exit                                       │
 │                                                             │
 └─────────────────────────────────────────────────────────────┘
"""


HELP_TEXT = """
 ┌─────────────────────────────────────────────────────────────┐
 │  AVAILABLE COMMANDS                                         │
 ├─────────────────────────────────────────────────────────────┤
 │                                                             │
 │  DASHBOARD & OVERVIEW                                       │
 │    dashboard      Full business overview                    │
 │    status          Current phase & progress                 │
 │    strategy        3-track strategy overview                │
 │    positioning     5 Korean advantages                      │
 │    products        Hero product candidates                  │
 │    offers          Offer tier structure                      │
 │                                                             │
 │  FINANCIAL MODELING                                         │
 │    finance         Full financial dashboard                 │
 │    projection      10-month revenue projection              │
 │    margin          Product margin analysis                  │
 │                                                             │
 │  ROADMAP & TASKS                                            │
 │    roadmap         10-month roadmap                         │
 │    week1           This week's 10 action items              │
 │    done <id>       Mark week-1 task as done                 │
 │    undo <id>       Revert week-1 task to pending            │
 │    tasks           View custom tasks                        │
 │    task add <text> Add a custom task                        │
 │    task done <id>  Complete a custom task                   │
 │    reset           Reset all tasks                          │
 │                                                             │
 │  TEMPLATES                                                  │
 │    templates       Generate all templates                   │
 │    linesheet       Generate wholesale line sheet            │
 │    pitch           Generate buyer pitch script              │
 │    emails          Generate email templates                 │
 │    story           Generate brand story 1-pager             │
 │    worksheet       Generate founder story worksheet         │
 │                                                             │
 │  COMPLIANCE                                                 │
 │    compliance      Full compliance overview                 │
 │    scan <text>     Scan marketing copy for risks            │
 │    supplement      Supplement compliance checklist          │
 │    cosmetics       Cosmetics (MoCRA) checklist              │
 │                                                             │
 │  CONTENT                                                    │
 │    calendar        30-day content calendar                  │
 │    week [n]        This week's content (starts at day n)    │
 │    brief <day>     Detailed brief for a specific day        │
 │    pillar [name]   Content by pillar                        │
 │    export content  Export content calendar                  │
 │                                                             │
 │  KPI TRACKING                                               │
 │    kpi             KPI tracking framework                   │
 │    kpi summary     Weekly KPI summary                       │
 │    kpi guide       KPI input guide                          │
 │    kpi log <week> <k>=<v> ...  Log weekly KPIs              │
 │    kpi export      Export KPI report                        │
 │                                                             │
 │  GENERAL                                                    │
 │    help            Show this help message                   │
 │    clear           Clear the screen                         │
 │    quit / exit     Exit the application                     │
 │                                                             │
 └─────────────────────────────────────────────────────────────┘
"""


def print_status():
    """Print current business status overview."""
    phase = get_current_phase()
    print("\n" + "=" * 80)
    print("  Current Status")
    print("=" * 80)
    print(f"\n  Current Phase: {phase}")
    print(f"  Revenue Target: {format_krw(REVENUE_TARGET_KRW)}")
    print(f"\n  Channel Mix:")
    for key, ch in CHANNEL_MIX.items():
        print(f"    {ch['label']}: {format_krw(ch['target_krw'])} (margin ~{ch['margin_pct']*100:.0f}%)")
    print()
    print_week1_checklist()


def print_strategy():
    """Print the 3-track strategy."""
    print("\n" + "=" * 80)
    print("  3-Track Strategy for 100억 Revenue")
    print("=" * 80)

    for key, track in THREE_TRACKS.items():
        print(f"\n  --- [{track['priority']}] {track['name']} ---")
        print(f"  {track['description']}")
        print(f"  Pros: {track['pros']}")
        print(f"  Cons: {track['cons']}")

    print("\n  Core Formula:")
    print("  1) Distribution for VOLUME")
    print("  2) Brand for MARGIN + VALUE")
    print("  3) Media for CAC REDUCTION")
    print("\n" + "=" * 80)


def print_positioning():
    """Print the 5 Korean positioning advantages."""
    print("\n" + "=" * 80)
    print("  5 Korean Advantages (Positioning)")
    print("=" * 80)

    for adv in POSITIONING_ADVANTAGES:
        print(f"\n  {adv['id']}. {adv['title']}")
        print(f"     {adv['detail']}")
        print(f"     Action: {adv['action']}")

    print("\n" + "=" * 80)


def print_products():
    """Print hero product candidates."""
    print("\n" + "=" * 80)
    print("  Hero Product Candidates")
    print("=" * 80)

    for p in HERO_PRODUCTS:
        rec = " [RECOMMENDED]" if p.get("recommended") else ""
        print(f"\n  {p['id']}. {p['name']}{rec}")
        print(f"     {p['description']}")
        print(f"     Pros: {p['pros']}")
        print(f"     Cons: {p['cons']}")
        print(f"     Est. COGS: {format_krw(p['est_cogs_krw'])}")
        print(f"     Est. Retail: {format_krw(p['est_retail_krw'])}")
        print(f"     Est. Wholesale: {format_krw(p['est_wholesale_krw'])}")

    print("\n  Recommendation: Inner Beauty Stick/Powder")
    print("  (Distribution for volume) + (Inner beauty stick for DTC margin/subscription)")
    print("\n" + "=" * 80)


def print_offers():
    """Print offer tier structure."""
    print("\n" + "=" * 80)
    print("  Offer Tier Structure")
    print("=" * 80)

    print("\n  Conversion Flow: Routine(Problem) -> Kit(Solution) -> Subscription(Retention)")

    for tier in OFFER_TIERS:
        print(f"\n  --- {tier['name']} ---")
        print(f"  {tier['description']}")
        print(f"  Strategy: {tier['pricing_strategy']}")
        print(f"  Price Range: ${tier['suggested_price_range_usd']}")

    print(f"\n  Price Amplifiers:")
    for i, amp in enumerate(PRICE_AMPLIFIERS, 1):
        print(f"    {i}. {amp}")

    print("\n" + "=" * 80)


def print_full_dashboard():
    """Print the comprehensive business dashboard."""
    print_status()
    print_strategy()
    run_financial_dashboard()


def handle_command(raw_input):
    """Parse and execute a command."""
    parts = raw_input.strip().split(None, 2)
    if not parts:
        return True

    cmd = parts[0].lower()
    arg1 = parts[1] if len(parts) > 1 else None
    arg2 = parts[2] if len(parts) > 2 else None

    # -- General --
    if cmd in ("quit", "exit", "q"):
        print("\n  Goodbye! Keep building!\n")
        return False
    elif cmd == "help":
        print(HELP_TEXT)
    elif cmd == "clear":
        os.system("clear" if os.name == "posix" else "cls")

    # -- Dashboard --
    elif cmd == "dashboard":
        print_full_dashboard()
    elif cmd == "status":
        print_status()
    elif cmd == "strategy":
        print_strategy()
    elif cmd == "positioning":
        print_positioning()
    elif cmd == "products":
        print_products()
    elif cmd == "offers":
        print_offers()

    # -- Financial --
    elif cmd == "finance":
        run_financial_dashboard()
    elif cmd == "projection":
        monthly = default_aggressive_projection()
        proj = revenue_projection(monthly)
        print_projection(proj)
    elif cmd == "margin":
        print_margin_analysis(HERO_PRODUCTS)

    # -- Roadmap & Tasks --
    elif cmd == "roadmap":
        print_roadmap()
    elif cmd == "week1":
        print_week1_checklist()
    elif cmd == "done" and arg1:
        try:
            complete_task(int(arg1))
        except ValueError:
            print("  Usage: done <task_id>  (e.g., done 1)")
    elif cmd == "undo" and arg1:
        try:
            uncomplete_task(int(arg1))
        except ValueError:
            print("  Usage: undo <task_id>")
    elif cmd == "tasks":
        print_custom_tasks()
    elif cmd == "task" and arg1 == "add" and arg2:
        add_custom_task(arg2)
    elif cmd == "task" and arg1 == "done" and arg2:
        try:
            complete_custom_task(int(arg2))
        except ValueError:
            print("  Usage: task done <task_id>")
    elif cmd == "reset":
        reset_tasks()

    # -- Templates --
    elif cmd == "templates":
        generate_all_templates()
    elif cmd == "linesheet":
        generate_line_sheet()
    elif cmd == "pitch":
        generate_buyer_pitch_script()
    elif cmd == "emails":
        generate_email_templates()
    elif cmd == "story":
        generate_brand_story_1pager()
    elif cmd == "worksheet":
        generate_founder_story_worksheet()

    # -- Compliance --
    elif cmd == "compliance":
        print_compliance_overview()
    elif cmd == "scan":
        text = " ".join(parts[1:]) if len(parts) > 1 else ""
        if text:
            check_marketing_copy(text)
        else:
            print("  Usage: scan <marketing text to check>")
            print("  Example: scan This product cures acne and prevents aging")
    elif cmd == "supplement":
        print_supplement_checklist()
    elif cmd == "cosmetics":
        print_cosmetics_checklist()

    # -- Content --
    elif cmd == "calendar":
        print_content_calendar()
    elif cmd == "week":
        start = 1
        if arg1:
            try:
                start = int(arg1)
            except ValueError:
                pass
        print_this_week_content(start)
    elif cmd == "brief":
        if arg1:
            try:
                generate_content_brief(int(arg1))
            except ValueError:
                print("  Usage: brief <day_number>  (e.g., brief 5)")
        else:
            print("  Usage: brief <day_number>  (1~30)")
    elif cmd == "pillar":
        print_content_by_pillar(arg1)
    elif cmd == "export" and arg1 == "content":
        export_content_calendar()

    # -- KPI --
    elif cmd == "kpi":
        if arg1 is None:
            print_kpi_framework()
        elif arg1 == "summary":
            print_weekly_summary()
        elif arg1 == "guide":
            print_kpi_input_guide()
        elif arg1 == "export":
            export_kpi_report()
        elif arg1 == "log":
            # Parse: kpi log <week> key=val key=val ...
            rest = raw_input.strip().split()[2:]  # everything after 'kpi log'
            if len(rest) < 2:
                print("  Usage: kpi log <week> <metric>=<value> ...")
                print("  Example: kpi log 1 revenue=50000000 orders=100")
            else:
                try:
                    week_num = int(rest[0])
                    kpi_dict = {}
                    for pair in rest[1:]:
                        if "=" in pair:
                            k, v = pair.split("=", 1)
                            try:
                                kpi_dict[k] = float(v) if "." in v else int(v)
                            except ValueError:
                                kpi_dict[k] = v
                    if kpi_dict:
                        log_weekly_kpi(week_num, kpi_dict)
                    else:
                        print("  No valid key=value pairs found.")
                except ValueError:
                    print("  Usage: kpi log <week_number> <metric>=<value> ...")
        else:
            print(f"  Unknown KPI command: {arg1}")
            print("  Try: kpi, kpi summary, kpi guide, kpi log, kpi export")

    else:
        print(f"  Unknown command: '{raw_input.strip()}'")
        print("  Type 'help' to see available commands.")

    return True


def main():
    """Main entry point for the interactive CLI."""
    print(BANNER)

    running = True
    while running:
        try:
            user_input = input("\n  K-Wellness> ").strip()
            if user_input:
                running = handle_command(user_input)
        except KeyboardInterrupt:
            print("\n\n  (Ctrl+C) Type 'quit' to exit.\n")
        except EOFError:
            print("\n  Goodbye!\n")
            break


if __name__ == "__main__":
    main()
