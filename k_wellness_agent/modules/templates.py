"""
Templates Module
- Wholesale line sheet generator
- Buyer pitch script
- Email templates (buyer outreach, influencer, etc.)
- Brand story 1-pager
- Founder story builder
"""

import os
from datetime import datetime

from k_wellness_agent.data.business_plan import (
    HERO_PRODUCTS,
    FOUNDER_STORY_TEMPLATE,
    OFFER_TIERS,
)

EXPORT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "exports")


def _ensure_export_dir():
    os.makedirs(EXPORT_DIR, exist_ok=True)


def generate_line_sheet(brand_name="K-Glow", contact_email="info@kglow.com"):
    """Generate a wholesale line sheet template."""
    _ensure_export_dir()

    hero = next((p for p in HERO_PRODUCTS if p.get("recommended")), HERO_PRODUCTS[0])

    content = f"""{'='*70}
                    WHOLESALE LINE SHEET
{'='*70}

Brand: {brand_name}
Contact: {contact_email}
Date: {datetime.now().strftime('%Y-%m-%d')}
Origin: South Korea

{'─'*70}
BRAND STORY
{'─'*70}
{brand_name} brings the Korean wellness philosophy to America.
We combine K-Beauty skin science with K-Food gut health wisdom
to deliver a simple "K-Glow" routine that busy women love.

Our hero product leverages the Gut-Skin Axis — the scientifically-
backed connection between gut health and radiant skin.

{'─'*70}
PRODUCT CATALOG
{'─'*70}

HERO PRODUCT: {hero['name']}
  Description:  {hero['description']}
  MSRP:         ${hero['est_retail_krw'] / 1350:.2f} USD (approx.)
  Wholesale:    ${hero['est_wholesale_krw'] / 1350:.2f} USD (approx.)
  Case Pack:    24 units
  MOQ:          48 units (2 cases)
  Lead Time:    2-3 weeks (domestic), 4-6 weeks (international)
  Shelf Life:   24 months
  Origin:       South Korea (GMP certified facility)

OFFER TIERS (DTC Reference):
"""
    for tier in OFFER_TIERS:
        content += f"""
  {tier['name']}
    {tier['description']}
    Suggested Retail: ${tier['suggested_price_range_usd']} USD
"""

    content += f"""
{'─'*70}
CERTIFICATIONS & COMPLIANCE
{'─'*70}
  * GMP Certified Manufacturing
  * FDA Facility Registration (pending/active)
  * MoCRA Compliant (for cosmetics)
  * DSHEA Compliant (for dietary supplements)
  * Product Liability Insurance: $2M

{'─'*70}
TERMS
{'─'*70}
  Payment:      Net 30 (with approved credit)
  Shipping:     FOB [warehouse location]
  Returns:      Defective product only, within 30 days
  Exclusivity:  Available for qualified partners (territory-based)

{'─'*70}
CONTACT
{'─'*70}
  {brand_name}
  Email: {contact_email}
  Website: www.{brand_name.lower().replace(' ', '')}.com

{'='*70}
"""
    filepath = os.path.join(EXPORT_DIR, "wholesale_line_sheet.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  >> Line sheet generated: {filepath}")
    return filepath


def generate_buyer_pitch_script():
    """Generate a buyer pitch script for wholesale meetings."""
    _ensure_export_dir()

    content = """======================================================================
               BUYER PITCH SCRIPT
======================================================================

TARGET: Retail buyers (H-Mart, indie beauty stores, online retailers)
DURATION: 5-7 minutes

----------------------------------------------------------------------
OPENING (30 seconds)
----------------------------------------------------------------------

"Hi [Buyer Name], thank you for taking the time to meet.

I'm [Your Name], founder of [Brand]. We're a Korean wellness brand
that's tapping into something your customers are already searching for
-- the connection between gut health and glowing skin, what scientists
call the Gut-Skin Axis."

----------------------------------------------------------------------
THE PROBLEM (45 seconds)
----------------------------------------------------------------------

"Your beauty-conscious customers are spending hundreds on skincare,
but most still struggle with dull skin, breakouts, and inflammation.

Here's what Korean women have known for generations: real glow starts
from the inside. That's why Korea's inner beauty market is already
$X billion -- and American consumers are just catching on."

----------------------------------------------------------------------
THE SOLUTION (60 seconds)
----------------------------------------------------------------------

"We created [Product Name] -- a daily [stick/powder/drink] that
combines:
  * [Key Ingredient 1] for skin hydration
  * [Key Ingredient 2] for gut health
  * [Key Ingredient 3] for antioxidant support

It's a 2-minute addition to any morning routine. No complicated steps.
Made in Korea at a GMP-certified facility."

----------------------------------------------------------------------
MARKET PROOF (60 seconds)
----------------------------------------------------------------------

"Here's why this is the right time:
  * K-Beauty exports to the US hit an all-time high in 2025
  * The inner beauty supplement market is growing at XX% CAGR
  * Our pre-launch waitlist already has [X,XXX] signups
  * [X] influencers are already posting about us organically

[Show 2-3 UGC screenshots or review highlights]"

----------------------------------------------------------------------
THE ASK (45 seconds)
----------------------------------------------------------------------

"We're looking for [X] retail partners for our US launch.

Here's what we offer:
  * Wholesale price: $XX per unit (MSRP $XX, XX% margin for you)
  * MOQ: Just [XX] units to start
  * Free POP display + sampling support for first order
  * Co-marketing support (social media features, in-store events)

We'd love to start with a test order of [XX] units. Can we set that up?"

----------------------------------------------------------------------
OBJECTION HANDLING
----------------------------------------------------------------------

"Already carry K-Beauty brands"
  -> "Great! That means your customers are already primed. We complement
     topical K-Beauty with the inner beauty angle -- it's an upsell."

"Not sure about supplements"
  -> "Totally understand. That's why we offer a starter program:
     low MOQ, free returns on first order if it doesn't move in 60 days."

"Need to think about it"
  -> "Of course. Can I send you a sample kit this week? I'll include our
     sell sheet with the margin breakdown so you have everything you need."

======================================================================
"""
    filepath = os.path.join(EXPORT_DIR, "buyer_pitch_script.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  >> Buyer pitch script generated: {filepath}")
    return filepath


def generate_email_templates():
    """Generate email templates for buyer outreach and influencer seeding."""
    _ensure_export_dir()

    content = """======================================================================
                    EMAIL TEMPLATES
======================================================================

--- TEMPLATE 1: BUYER COLD OUTREACH ---

Subject: Korean Inner Beauty Brand -- Exclusive US Distribution Opportunity

Hi [Buyer Name],

I'm [Your Name], founder of [Brand Name]. We're a Korean wellness
brand launching in the US market with a product your customers are
going to love.

Our hero product, [Product Name], is a daily [format] that supports
skin health from the inside out -- combining Korean beauty science
with gut health innovation (the "Gut-Skin Axis").

Quick highlights:
  * Made in Korea (GMP certified)
  * [Key metric: waitlist size / influencer interest / market data]
  * Wholesale margin: XX%+
  * Low MOQ to start: XX units

K-Beauty exports to the US hit record highs in 2025, and inner
beauty is the next wave. We'd love to be on your shelves.

Could I send you a sample kit? Happy to jump on a quick call this
week to walk through our line sheet.

Best,
[Your Name]
[Brand] | [Website] | [Phone]


--- TEMPLATE 2: BUYER FOLLOW-UP ---

Subject: Following up -- [Brand] sample kit

Hi [Buyer Name],

Just following up on my email from [X days ago]. I'd love to get
a sample of [Product Name] in your hands -- I think you'll see why
our pre-launch customers are already reordering.

Quick update since my last email:
  * [New social proof: reviews, press mention, sales milestone]

Would [Day] or [Day] work for a 10-minute call? I can also just
ship a sample kit directly -- what's the best address?

Best,
[Your Name]


--- TEMPLATE 3: INFLUENCER SEEDING OUTREACH ---

Subject: Gift for you -- Korean glow routine

Hi [Influencer Name],

I love your content on [specific post/topic]. Your approach to
[skincare/wellness/routine] really resonates with our brand philosophy.

I'm [Your Name], founder of [Brand]. We're bringing the Korean
"Gut-Skin Axis" routine to the US -- the idea that real glow
starts from the inside.

I'd love to send you our [Product Name] -- no strings attached.
If you love it and want to share, amazing. If not, no pressure at all.

Can I send a kit to your PR address?

Best,
[Your Name]
[Brand] | @[handle]


--- TEMPLATE 4: INFLUENCER COLLABORATION PROPOSAL ---

Subject: Collaboration opportunity -- [Brand] x [Influencer Name]

Hi [Influencer Name / Manager],

Following up on the sample I sent -- hope you're enjoying it!

We're launching our "7-Day K-Glow Reset" challenge and would love
for you to be one of our founding ambassadors.

What we're thinking:
  * [X] posts/stories over 7 days documenting your routine
  * Unique discount code for your audience ([XX]% off)
  * Commission: [X]% on all sales through your code
  * [Optional: flat fee of $XXX]

Our brand is all about real results + authentic routines, which is
exactly what your audience loves.

Interested? Happy to hop on a call or DM to discuss details.

Best,
[Your Name]


--- TEMPLATE 5: PR/MEDIA PITCH ---

Subject: Story pitch: The next wave of K-Beauty is what you eat

Hi [Editor/Journalist Name],

Quick pitch for [Publication]:

The K-Beauty boom transformed American skincare routines. Now,
Korean brands are bringing the next evolution: "inner beauty"
-- supplements and functional foods designed to support skin
health from the gut.

[Brand Name] is at the forefront, founded by [Your Name], who
grew up in Korea surrounded by the philosophy that beauty starts
with what you put IN your body, not just ON it.

Key angles:
  * The Gut-Skin Axis: the science behind K-inner beauty
  * K-Beauty exports to US at all-time highs
  * Founder story: Korean wellness meets American market
  * The "2-Minute K-Glow Routine" trend

Happy to provide product samples, founder interview, or expert
sources. What works best?

Best,
[Your Name]
[Brand] | [Website]

======================================================================
"""
    filepath = os.path.join(EXPORT_DIR, "email_templates.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  >> Email templates generated: {filepath}")
    return filepath


def generate_brand_story_1pager(
    founder_name="Chaejung Maeng",
    brand_name="K-Glow",
    mission="",
    story_sections=None,
):
    """Generate a brand story 1-pager."""
    _ensure_export_dir()

    sections = story_sections or {}
    past = sections.get("past", "[Your past experience here]")
    turning_point = sections.get("turning_point", "[Your turning point here]")
    experiment = sections.get("experiment", "[Your routine changes here]")
    result = sections.get("result", "[Your results here]")
    mission_text = mission or sections.get("mission", "[Your mission here]")

    content = f"""======================================================================
                    BRAND STORY -- {brand_name}
                    Founded by {founder_name}
======================================================================

THE ORIGIN
----------
{past}

THE TURNING POINT
-----------------
{turning_point}

THE DISCOVERY
-------------
{experiment}

THE RESULT
----------
{result}

THE MISSION
-----------
{mission_text}

======================================================================

ONE-LINER:
"I help busy women get 'K-Glow' through a simple 2-minute routine:
skin barrier + gut-friendly inner beauty."

BRAND PROMISE:
{brand_name} combines generations of Korean beauty wisdom with
modern gut-health science to deliver visible results in a routine
that takes less time than brewing your morning coffee.

CORE VALUES:
  1. Inside-Out Beauty (Gut-Skin Axis)
  2. Simplicity (2-minute routine)
  3. Korean Heritage, Global Standard
  4. Transparency (clean ingredients, honest marketing)
  5. Community (build in public, grow together)

======================================================================
"""
    filepath = os.path.join(EXPORT_DIR, "brand_story_1pager.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  >> Brand story 1-pager generated: {filepath}")
    return filepath


def generate_founder_story_worksheet():
    """Generate interactive founder story worksheet."""
    _ensure_export_dir()

    template = FOUNDER_STORY_TEMPLATE
    content = """======================================================================
              FOUNDER STORY WORKSHEET
======================================================================

Answer these 5 questions to build a unified story for all channels:
content, landing pages, IR materials, and buyer pitches.

"""
    for i, section in enumerate(template["sections"], 1):
        content += f"""
--- {i}. {section['label']} ---

Question: {section['prompt']}
English example: "{section['example']}"

Your answer:
-> _______________________________________________________________
   _______________________________________________________________
   _______________________________________________________________

"""

    content += """
======================================================================

After filling this out, use 'story set' command to input each section
and auto-generate your brand story 1-pager.

======================================================================
"""
    filepath = os.path.join(EXPORT_DIR, "founder_story_worksheet.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  >> Founder story worksheet generated: {filepath}")
    return filepath


def generate_all_templates():
    """Generate all templates at once."""
    print("\n" + "=" * 80)
    print("  Template Generation")
    print("=" * 80 + "\n")

    generate_line_sheet()
    generate_buyer_pitch_script()
    generate_email_templates()
    generate_brand_story_1pager()
    generate_founder_story_worksheet()

    print(f"\n  All templates saved to: {EXPORT_DIR}/")
