"""
Financial Modeling Module
- Revenue projection calculator
- Margin analysis
- Channel mix optimizer
- Break-even analysis
"""

import json
import os
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "exports")


def format_krw(amount):
    """Format KRW amount with commas and 억/만 notation."""
    if amount >= 100_000_000:
        eok = amount / 100_000_000
        return f"{eok:,.1f}억원 ({amount:,.0f}원)"
    elif amount >= 10_000:
        man = amount / 10_000
        return f"{man:,.0f}만원 ({amount:,.0f}원)"
    return f"{amount:,.0f}원"


def calculate_orders_needed(target_revenue, aov):
    """Calculate number of orders needed to hit revenue target."""
    return int(target_revenue / aov)


def calculate_margin_table(product):
    """Calculate detailed margin breakdown for a product."""
    cogs = product["est_cogs_krw"]
    retail = product["est_retail_krw"]
    wholesale = product["est_wholesale_krw"]

    dtc_margin = retail - cogs
    dtc_margin_pct = (dtc_margin / retail) * 100

    ws_margin = wholesale - cogs
    ws_margin_pct = (ws_margin / wholesale) * 100

    # Assume Amazon takes ~30% (referral + FBA)
    amazon_net = retail * 0.70
    amazon_margin = amazon_net - cogs
    amazon_margin_pct = (amazon_margin / retail) * 100

    return {
        "product": product["name"],
        "cogs": cogs,
        "channels": {
            "DTC (자사몰)": {
                "selling_price": retail,
                "margin": dtc_margin,
                "margin_pct": round(dtc_margin_pct, 1),
            },
            "Amazon": {
                "selling_price": retail,
                "net_after_fees": round(amazon_net),
                "margin": round(amazon_margin),
                "margin_pct": round(amazon_margin_pct, 1),
            },
            "Wholesale (도매)": {
                "selling_price": wholesale,
                "margin": ws_margin,
                "margin_pct": round(ws_margin_pct, 1),
            },
        },
    }


def revenue_projection(monthly_targets):
    """
    Generate monthly revenue projection.
    monthly_targets: list of 12 dicts with keys:
      - dtc_orders, dtc_aov, wholesale_revenue
    """
    results = []
    cumulative = 0
    for i, m in enumerate(monthly_targets):
        dtc_rev = m.get("dtc_orders", 0) * m.get("dtc_aov", 75000)
        ws_rev = m.get("wholesale_revenue", 0)
        total = dtc_rev + ws_rev
        cumulative += total
        results.append({
            "month": i + 1,
            "dtc_revenue": dtc_rev,
            "wholesale_revenue": ws_rev,
            "total_revenue": total,
            "cumulative_revenue": cumulative,
        })
    return results


def default_aggressive_projection():
    """
    Default aggressive projection to hit 100억 in 10 months.
    B2B ramps up early, DTC grows mid-year.
    """
    monthly = [
        # Month 1-2 (Feb-Mar): Setup phase
        {"dtc_orders": 50, "dtc_aov": 75000, "wholesale_revenue": 0},
        {"dtc_orders": 100, "dtc_aov": 75000, "wholesale_revenue": 100_000_000},
        # Month 3-4 (Apr-May): First POs
        {"dtc_orders": 300, "dtc_aov": 85000, "wholesale_revenue": 500_000_000},
        {"dtc_orders": 500, "dtc_aov": 90000, "wholesale_revenue": 800_000_000},
        # Month 5-6 (Jun-Jul): Acceleration
        {"dtc_orders": 1000, "dtc_aov": 95000, "wholesale_revenue": 1_000_000_000},
        {"dtc_orders": 1500, "dtc_aov": 100000, "wholesale_revenue": 1_200_000_000},
        # Month 7-8 (Aug-Sep): Scale
        {"dtc_orders": 2000, "dtc_aov": 110000, "wholesale_revenue": 1_000_000_000},
        {"dtc_orders": 2500, "dtc_aov": 115000, "wholesale_revenue": 1_000_000_000},
        # Month 9-10 (Oct-Nov): Peak
        {"dtc_orders": 3000, "dtc_aov": 120000, "wholesale_revenue": 800_000_000},
        {"dtc_orders": 3500, "dtc_aov": 125000, "wholesale_revenue": 700_000_000},
    ]
    return monthly


def print_projection(projection):
    """Pretty-print a revenue projection."""
    print("\n" + "=" * 80)
    print("  월별 매출 프로젝션 (100억 목표)")
    print("=" * 80)
    print(f"{'월':>4} | {'DTC 매출':>16} | {'도매/B2B':>16} | {'월 합계':>16} | {'누적':>16}")
    print("-" * 80)
    for r in projection:
        print(
            f" {r['month']:>3} | "
            f"{format_krw(r['dtc_revenue']):>16} | "
            f"{format_krw(r['wholesale_revenue']):>16} | "
            f"{format_krw(r['total_revenue']):>16} | "
            f"{format_krw(r['cumulative_revenue']):>16}"
        )
    print("-" * 80)
    total = projection[-1]["cumulative_revenue"]
    target = 10_000_000_000
    pct = (total / target) * 100
    print(f"  10개월 누적: {format_krw(total)}")
    print(f"  목표 달성률: {pct:.1f}%")
    if total >= target:
        print("  ✓ 목표 달성!")
    else:
        gap = target - total
        print(f"  Gap: {format_krw(gap)}")
    print()


def print_margin_analysis(products):
    """Print margin analysis for all hero product candidates."""
    from k_wellness_agent.data.business_plan import HERO_PRODUCTS

    print("\n" + "=" * 80)
    print("  히어로 제품 마진 분석")
    print("=" * 80)

    for product in HERO_PRODUCTS:
        analysis = calculate_margin_table(product)
        rec = " ★ 추천" if product.get("recommended") else ""
        print(f"\n  ▶ {analysis['product']}{rec}")
        print(f"    원가(COGS): {format_krw(analysis['cogs'])}")
        print(f"    {'채널':<20} | {'판매가':>10} | {'마진':>10} | {'마진율':>8}")
        print(f"    {'-'*60}")
        for ch_name, ch_data in analysis["channels"].items():
            price = ch_data.get("selling_price", ch_data.get("net_after_fees", 0))
            margin = ch_data["margin"]
            margin_pct = ch_data["margin_pct"]
            print(f"    {ch_name:<20} | {format_krw(price):>10} | {format_krw(margin):>10} | {margin_pct:>6.1f}%")
    print()


def export_projection_json(projection, filename="projection.json"):
    """Export projection to JSON file."""
    os.makedirs(DATA_DIR, exist_ok=True)
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(projection, f, ensure_ascii=False, indent=2)
    print(f"  Exported to: {filepath}")
    return filepath


def run_financial_dashboard():
    """Run the full financial modeling dashboard."""
    from k_wellness_agent.data.business_plan import HERO_PRODUCTS, AOV_SCENARIOS, REVENUE_TARGET_KRW

    print("\n" + "=" * 80)
    print("  📊 재무 모델링 대시보드")
    print("=" * 80)

    # 1. Orders needed by AOV
    print("\n  [1] 목표 매출 달성에 필요한 주문 수 (AOV별)")
    print(f"  목표: {format_krw(REVENUE_TARGET_KRW)}")
    print()
    for scenario in AOV_SCENARIOS:
        orders = calculate_orders_needed(REVENUE_TARGET_KRW, scenario["aov_krw"])
        print(f"    {scenario['label']}: {orders:,}건 필요")

    # 2. Margin analysis
    print_margin_analysis(HERO_PRODUCTS)

    # 3. Revenue projection
    monthly = default_aggressive_projection()
    projection = revenue_projection(monthly)
    print_projection(projection)

    # 4. Export
    export_projection_json(projection)

    return projection
