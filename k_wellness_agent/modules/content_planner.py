"""
Content Planner Module
- 30-day content calendar viewer
- Content idea generator by pillar
- Export content calendar to file
"""

import os
import json
from datetime import datetime, timedelta

from k_wellness_agent.data.business_plan import CONTENT_TOPICS_30DAY

EXPORT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "exports")


def print_content_calendar():
    """Display the full 30-day content calendar."""
    print("\n" + "=" * 80)
    print("  30-Day Content Calendar")
    print("=" * 80)

    # Group by pillar
    pillars = {}
    for item in CONTENT_TOPICS_30DAY:
        p = item["pillar"]
        if p not in pillars:
            pillars[p] = 0
        pillars[p] += 1

    print(f"\n  Content Pillar Distribution:")
    for pillar, count in pillars.items():
        bar = "#" * count
        print(f"    {pillar:<16} {bar} ({count})")

    print(f"\n  {'Day':>4} | {'Pillar':<16} | Topic")
    print(f"  {'─'*72}")

    for item in CONTENT_TOPICS_30DAY:
        day = item["day"]
        pillar = item["pillar"]
        topic = item["topic"]
        print(f"  {day:>4} | {pillar:<16} | {topic}")

    print()


def print_content_by_pillar(pillar_name=None):
    """Display content ideas filtered by pillar."""
    if pillar_name is None:
        print("\n  Content Pillars:")
        pillars = set(item["pillar"] for item in CONTENT_TOPICS_30DAY)
        for p in sorted(pillars):
            count = sum(1 for i in CONTENT_TOPICS_30DAY if i["pillar"] == p)
            print(f"    * {p} ({count})")
        print(f"\n  Usage: content pillar <name>")
        return

    filtered = [i for i in CONTENT_TOPICS_30DAY if pillar_name.lower() in i["pillar"].lower()]

    if not filtered:
        print(f"\n  No content found for pillar '{pillar_name}'.")
        return

    pillar = filtered[0]["pillar"]
    print(f"\n" + "=" * 80)
    print(f"  [{pillar}] Content List ({len(filtered)})")
    print("=" * 80)

    for item in filtered:
        print(f"  Day {item['day']:>2}: {item['topic']}")
    print()


def print_this_week_content(start_day=1):
    """Display this week's content (7 days starting from start_day)."""
    end_day = start_day + 6
    filtered = [i for i in CONTENT_TOPICS_30DAY if start_day <= i["day"] <= end_day]

    print(f"\n" + "=" * 80)
    print(f"  This Week's Content (Day {start_day}~{end_day})")
    print("=" * 80)

    start_date = datetime.now()
    for item in filtered:
        day_offset = item["day"] - start_day
        target_date = start_date + timedelta(days=day_offset)
        date_str = target_date.strftime("%m/%d (%a)")
        print(f"\n  Day {item['day']:>2} ({date_str})")
        print(f"    Pillar:  {item['pillar']}")
        print(f"    Topic:   {item['topic']}")
        print(f"    Format:  30~60 sec short-form video")
        print(f"    Channel: TikTok / IG Reels / YouTube Shorts")

    print()


def generate_content_brief(day_number):
    """Generate a detailed content brief for a specific day."""
    item = next((i for i in CONTENT_TOPICS_30DAY if i["day"] == day_number), None)
    if not item:
        print(f"\n  No content found for Day {day_number}. (Range: 1~30)")
        return

    print(f"\n" + "=" * 80)
    print(f"  Content Brief -- Day {item['day']}")
    print("=" * 80)

    print(f"""
  Topic:   {item['topic']}
  Pillar:  {item['pillar']}
  Format:  30~60 sec short-form video

  -----------------------------------------------
  SCRIPT STRUCTURE
  -----------------------------------------------

  [HOOK -- first 3 seconds] (stop the scroll)
  -> "Did you know that in Korea, ..."
  -> "Nobody talks about this truth about [topic]..."

  [BODY -- 20~40 seconds] (core content)
  -> Point 1: ...
  -> Point 2: ...
  -> Point 3: (optional)

  [CTA -- last 5 seconds] (call to action)
  -> "Have you tried this routine? Tell me in the comments"
  -> "Get the free guide at link in bio"
  -> "Follow for Part 2 tomorrow"

  -----------------------------------------------
  PRODUCTION TIPS
  -----------------------------------------------

  * Natural light or ring light (clean background)
  * Always include subtitles (85% watch on mute)
  * Text overlay on first frame (HOOK)
  * Use trending audio when applicable
  * Hashtags: #KBeauty #KGlow #GutSkinAxis #KoreanRoutine #InnerBeauty
""")


def export_content_calendar():
    """Export content calendar to JSON and text file."""
    os.makedirs(EXPORT_DIR, exist_ok=True)

    json_path = os.path.join(EXPORT_DIR, "content_calendar.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(CONTENT_TOPICS_30DAY, f, ensure_ascii=False, indent=2)

    txt_path = os.path.join(EXPORT_DIR, "content_calendar.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("30-DAY K-GLOW CONTENT CALENDAR\n")
        f.write("=" * 60 + "\n\n")
        for item in CONTENT_TOPICS_30DAY:
            f.write(f"Day {item['day']:>2} [{item['pillar']}]\n")
            f.write(f"  {item['topic']}\n\n")

    print(f"  Content calendar exported:")
    print(f"    JSON: {json_path}")
    print(f"    TXT:  {txt_path}")
