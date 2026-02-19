"""
Compliance Checker Module
- FDA dietary supplement claim checker
- MoCRA cosmetics compliance checklist
- FTC influencer disclosure checker
- Marketing copy scanner for banned words
"""

from k_wellness_agent.data.business_plan import COMPLIANCE_RULES


def check_marketing_copy(text):
    """
    Scan marketing copy for banned/risky words (dietary supplement context).
    Returns a report of flagged terms and suggested alternatives.
    """
    text_lower = text.lower()
    rules = COMPLIANCE_RULES["dietary_supplement"]
    banned = rules["banned_words"]
    safe = rules["safe_words"]

    flagged = []
    for word in banned:
        if word.lower() in text_lower:
            flagged.append(word)

    print("\n" + "=" * 80)
    print("  Marketing Copy Compliance Scan")
    print("=" * 80)
    print(f"\n  Scanned: \"{text[:80]}{'...' if len(text) > 80 else ''}\"")

    if flagged:
        print(f"\n  WARNING: {len(flagged)} risky term(s) found!")
        print()
        for word in flagged:
            print(f"    X \"{word}\" -- may be classified as a Drug Claim")
        print(f"\n  -----------------------------------------------")
        print(f"  Safe alternatives (Structure/Function Claims):")
        for s in safe:
            print(f"    OK \"{s}\"")
    else:
        print(f"\n  PASS: No risky terms found!")

    print(f"\n  Note: Always include DSHEA disclaimer:")
    print(f"    \"These statements have not been evaluated by the Food and Drug Administration.")
    print(f"     This product is not intended to diagnose, treat, cure, or prevent any disease.\"")
    print()

    return {
        "flagged": flagged,
        "is_safe": len(flagged) == 0,
        "safe_alternatives": safe,
    }


def print_compliance_overview():
    """Display full compliance overview for all categories."""
    print("\n" + "=" * 80)
    print("  Compliance Guide (US Market)")
    print("=" * 80)

    for key, rules in COMPLIANCE_RULES.items():
        print(f"\n  --- {rules['title']} ---")

        print(f"\n  Required:")
        for r in rules["rules"]:
            print(f"    * {r}")

        if "banned_words" in rules:
            print(f"\n  WARNING - Banned/Risky terms:")
            words = rules["banned_words"]
            for i in range(0, len(words), 4):
                row = words[i:i+4]
                print(f"    X {', '.join(row)}")

        if "safe_words" in rules:
            print(f"\n  Safe terms:")
            for w in rules["safe_words"]:
                print(f"    OK {w}")

        print(f"\n  Reference: {rules['reference']}")

    print("\n" + "=" * 80)


def print_supplement_checklist():
    """Display dietary supplement launch compliance checklist."""
    print("\n" + "=" * 80)
    print("  Dietary Supplement Launch Compliance Checklist")
    print("=" * 80)

    items = [
        ("Manufacturing", [
            "GMP certified facility",
            "Raw material Identity Testing complete",
            "Stability Test complete",
            "Heavy metal / microbial testing passed",
            "COA (Certificate of Analysis) on file",
        ]),
        ("Labeling", [
            "Supplement Facts panel included",
            "Full ingredient list (Other Ingredients) displayed",
            "Serving Size / Servings Per Container specified",
            "DSHEA disclaimer text included",
            "Manufacturer/distributor contact info displayed",
            "Net quantity displayed",
            "Drug Claim language removed (verified)",
        ]),
        ("Registration", [
            "FDA Facility Registration complete",
            "Structure/Function Claim notification filed (if applicable, within 30 days)",
            "New Dietary Ingredient notification (NDI, if applicable)",
            "Product Liability Insurance obtained",
        ]),
        ("Marketing", [
            "Website/ad copy cleared of Drug Claims",
            "Customer testimonials reviewed for disease mentions",
            "Influencer guidelines provided",
            "FTC disclosure requirements met",
        ]),
    ]

    for category, checks in items:
        print(f"\n  [{category}]")
        for check in checks:
            print(f"    [ ] {check}")

    print("\n" + "=" * 80)


def print_cosmetics_checklist():
    """Display MoCRA cosmetics compliance checklist."""
    print("\n" + "=" * 80)
    print("  Cosmetics (MoCRA) Compliance Checklist")
    print("=" * 80)

    items = [
        ("Facility & Registration", [
            "Manufacturing facility FDA registered",
            "Product Listing submitted",
            "Registration info renewal scheduled",
        ]),
        ("Safety & Testing", [
            "Product safety substantiation on file",
            "Fragrance/color allergen identification complete",
            "Serious Adverse Event reporting system established",
            "15 business-day FDA reporting process in place",
        ]),
        ("Labeling", [
            "Full ingredient list (INCI nomenclature)",
            "Net quantity displayed",
            "Manufacturer/distributor info displayed",
            "Usage warnings (if applicable)",
            "Fragrance allergen disclosure (if applicable)",
        ]),
        ("GMP", [
            "Good Manufacturing Practice compliance",
            "Manufacturing records maintained",
            "Quality control system operational",
        ]),
    ]

    for category, checks in items:
        print(f"\n  [{category}]")
        for check in checks:
            print(f"    [ ] {check}")

    print("\n" + "=" * 80)
