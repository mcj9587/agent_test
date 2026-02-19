"""
Core business plan data for K-Wellness Agent.
Contains all strategic data, roadmap phases, positioning, and compliance info.
"""

# ============================================================
# GOAL BREAKDOWN
# ============================================================
REVENUE_TARGET_KRW = 10_000_000_000  # 100억 원
ASSET_TARGET_KRW = 5_000_000_000     # 50억 원

CHANNEL_MIX = {
    "wholesale_retail_b2b": {
        "label": "도매/리테일/B2B",
        "target_krw": 7_000_000_000,
        "description": "총판/유통 + 리테일 발주",
        "margin_pct": 0.15,
    },
    "dtc": {
        "label": "DTC (아마존+자사몰+틱톡샵)",
        "target_krw": 3_000_000_000,
        "description": "고마진/구독/번들",
        "margin_pct": 0.45,
    },
}

AOV_SCENARIOS = [
    {"aov_krw": 75_000, "label": "7.5만원 AOV"},
    {"aov_krw": 150_000, "label": "15만원 AOV"},
    {"aov_krw": 300_000, "label": "30만원 AOV (프리미엄 번들)"},
]

# ============================================================
# 3-TRACK STRATEGY
# ============================================================
THREE_TRACKS = {
    "track1_volume": {
        "name": "빠른 매출(볼륨) — 검증된 K-브랜드 총판/유통",
        "description": "이미 잘 팔리는 한국 브랜드를 미국/해외 독점 또는 준독점 유통으로 가져옴",
        "pros": "리드타임 짧고, 리테일/도매로 매출 볼륨이 빨리 뜸",
        "cons": "마진은 낮을 수 있음(규모로 승부)",
        "priority": "HIGH",
    },
    "track2_brand": {
        "name": "고마진/자산(브랜드) — 시그니처 하우스 브랜드 런칭",
        "description": "유통 현금흐름 + 하우스 브랜드 1개(히어로 제품 1개)로 마진+IP+밸류",
        "pros": "마진/IP/밸류 확보, 구독모델 가능",
        "cons": "시간 필요, 초기 투자 필요",
        "priority": "HIGH",
    },
    "track3_media": {
        "name": "영향력(미디어) — 퍼블릭 피겨/인플루언서 엔진",
        "description": "창업자 스토리 + 루틴 콘텐츠 + 사회적 증거로 트래픽 비용 절감",
        "pros": "CAC 절감, 바이어/파트너십 문 열림",
        "cons": "일관된 콘텐츠 생산 필요",
        "priority": "MEDIUM",
    },
}

# ============================================================
# POSITIONING (한국인 장점 5가지)
# ============================================================
POSITIONING_ADVANTAGES = [
    {
        "id": 1,
        "title": "K-Beauty의 글로벌 신뢰",
        "detail": "한국 = 스킨케어 강국 인식 + 수요 상승",
        "action": "모든 마케팅에 'Korean skincare heritage' 메시지 포함",
    },
    {
        "id": 2,
        "title": "K-Food의 글로벌 트렌드",
        "detail": "발효/저당/기능성 식문화 → 'Gut-Skin Axis' 스토리 연결",
        "action": "제품 스토리에 발효/장건강 과학적 근거 반영",
    },
    {
        "id": 3,
        "title": "빨리빨리 실행력",
        "detail": "빠른 제품 개선/리뉴얼 → 미국에서 'agile brand'로 어필",
        "action": "제품 개선 주기를 마케팅 포인트로 활용",
    },
    {
        "id": 4,
        "title": "K-루틴 문화",
        "detail": "루틴(습관)을 상품화하기 쉬움 → 번들/구독/챌린지로 전환",
        "action": "모든 제품을 '루틴 키트' 형태로 번들링",
    },
    {
        "id": 5,
        "title": "창업자 서사",
        "detail": "한국에서 길러진 기준/철학 + 개인 경험을 권위(authority)로 전환",
        "action": "Founder Story 1-pager 작성 및 모든 채널에 일관 활용",
    },
]

# ============================================================
# HERO PRODUCT CANDIDATES
# ============================================================
HERO_PRODUCTS = [
    {
        "id": 1,
        "name": "이너뷰티 스틱/파우더",
        "description": "콜라겐/프로바이오틱/피부보습 성분 조합",
        "pros": "배송/보관/마진/확장성 유리, 구독모델 최적",
        "cons": "건기식 컴플라이언스 필요(DSHEA)",
        "recommended": True,
        "est_cogs_krw": 5_000,
        "est_retail_krw": 45_000,
        "est_wholesale_krw": 22_000,
    },
    {
        "id": 2,
        "name": "기능성 RTD(음료)",
        "description": "기능성 음료(콜라겐/프로바이오틱 등)",
        "pros": "트렌드 크고 충동구매 가능",
        "cons": "물류/마진/리스크 큼, 무게/부피 이슈",
        "recommended": False,
        "est_cogs_krw": 3_000,
        "est_retail_krw": 5_000,
        "est_wholesale_krw": 2_800,
    },
    {
        "id": 3,
        "name": "스킨케어 히어로(장벽/진정)",
        "description": "피부장벽/진정 중심 K-뷰티 스킨케어",
        "pros": "K-뷰티 강점, 높은 인지도",
        "cons": "경쟁 치열, 브랜드력이 중요",
        "recommended": False,
        "est_cogs_krw": 8_000,
        "est_retail_krw": 55_000,
        "est_wholesale_krw": 27_000,
    },
]

# ============================================================
# ROADMAP PHASES
# ============================================================
ROADMAP = [
    {
        "phase": 1,
        "name": "매출 기반 + 히어로 결정",
        "period": "0~30일 (2~3월)",
        "months": "2026-02 ~ 2026-03",
        "goals": [
            "유통 가능한 K-브랜드 3개 선정 → 공급 조건/MOQ/마진표 확보",
            "히어로 제품 1개 확정 → 원가/마진/패키징/라벨 문구 초안",
            "영어 콘텐츠 채널 오픈(YouTube Shorts/TikTok/IG 중 1개 메인)",
        ],
        "deliverables": [
            "제품 라인시트(wholesale line sheet)",
            "성분/원산지/인증/테스트 자료",
            "MSRP, 도매가, 케이스팩, MOQ, 리드타임 표",
            "브랜드 스토리 1페이지",
        ],
    },
    {
        "phase": 2,
        "name": "첫 대형 거래/PO + DTC 프리런칭",
        "period": "31~90일 (4~5월)",
        "months": "2026-04 ~ 2026-05",
        "goals": [
            "해외 리테일/도매 PO 3건 확보 (건당 2~5억 규모)",
            "아마존/자사몰 동시 준비",
            "프리런칭 대기자 3,000명 모집",
        ],
        "deliverables": [
            "PO 계약서 3건",
            "아마존 리스팅 완료",
            "'K-Glow 루틴 체크리스트' 리드마그넷",
            "'7-Day K-Glow Reset' 챌린지 페이지",
        ],
    },
    {
        "phase": 3,
        "name": "매출 가속 구간",
        "period": "4~6개월 (6~8월)",
        "months": "2026-06 ~ 2026-08",
        "goals": [
            "거래처 확대 (같은 SKU를 더 많이 파는 방식)",
            "UGC 100개 확보",
            "번들/구독 도입",
        ],
        "deliverables": [
            "거래처 10개+",
            "UGC 영상 100개",
            "스타터 킷 / Results Bundle / 구독 상품 런칭",
        ],
    },
    {
        "phase": 4,
        "name": "리테일 확장 + 밸류(자산) 트랙",
        "period": "7~10개월 (9~12월)",
        "months": "2026-09 ~ 2026-12",
        "goals": [
            "PO 기반 운영자금(인벤토리 파이낸싱/팩토링) 확보",
            "전략적 투자/유통 파트너 투자 검토",
            "지분 가치(자산) 키우기",
        ],
        "deliverables": [
            "파이낸싱 계약",
            "투자유치 IR 자료",
            "연간 매출 100억 달성 검증",
        ],
    },
]

# ============================================================
# WEEK-1 CHECKLIST (이번 주 해야 할 10가지)
# ============================================================
WEEK1_CHECKLIST = [
    {"id": 1, "task": "카테고리 하나로 좁히기: 이너뷰티 스틱 vs 스킨케어 히어로 vs 기능성 음료", "status": "pending"},
    {"id": 2, "task": "유통 후보 K-브랜드 20개 리스트업 → 10개 컨택 → 3개 미팅", "status": "pending"},
    {"id": 3, "task": "히어로 제품 원가/마진표 (원가, 물류, 수수료, 광고비 가정 포함)", "status": "pending"},
    {"id": 4, "task": "미국 판매 문구에서 금지/위험 표현 체크 (질병/치료 뉘앙스 제거)", "status": "pending"},
    {"id": 5, "task": "영어 계정 오픈 + 프로필 한 줄 (포지셔닝) 확정", "status": "pending"},
    {"id": 6, "task": "'7-Day K-Glow Reset' 랜딩페이지 (대기자 모집)", "status": "pending"},
    {"id": 7, "task": "UGC 20명 시딩 계획 (미국/한국 혼합)", "status": "pending"},
    {"id": 8, "task": "아마존/자사몰 중 한 채널 먼저 오픈", "status": "pending"},
    {"id": 9, "task": "도매 라인시트/샘플키트 구성", "status": "pending"},
    {"id": 10, "task": "주간 KPI 세팅: 리드/미팅/PO/콘텐츠 수/리뷰 수", "status": "pending"},
]

# ============================================================
# OFFER STRUCTURE
# ============================================================
OFFER_TIERS = [
    {
        "name": "Starter Kit",
        "description": "초기 진입 (1개월 분량)",
        "pricing_strategy": "낮은 진입 장벽, 체험 유도",
        "suggested_price_range_usd": "29~49",
    },
    {
        "name": "Results Bundle",
        "description": "2개월치, 체감 강화",
        "pricing_strategy": "단품 대비 15~20% 할인, AOV 상승",
        "suggested_price_range_usd": "59~89",
    },
    {
        "name": "Subscription",
        "description": "최저가 + 혜택 (매월 자동배송)",
        "pricing_strategy": "최저 단가, LTV 극대화, 이탈률 관리",
        "suggested_price_range_usd": "24~39/month",
    },
]

PRICE_AMPLIFIERS = [
    "측정 가능한 약속: '7일 루틴 완성', '30일 리셋'",
    "리스크 제거: 14일 만족 보장 / 첫 구매 환불",
    "사회적 증거: UGC/리뷰/전문가 코멘트",
    "희소성: 첫 생산 5,000개 한정 / 베타 멤버",
    "번들링: 단품보다 번들이 훨씬 잘 팔림",
]

# ============================================================
# COMPLIANCE
# ============================================================
COMPLIANCE_RULES = {
    "dietary_supplement": {
        "title": "이너뷰티/건기식 (Dietary Supplement)",
        "rules": [
            "질병 치료/예방/진단 표현 절대 금지 (Drug claim 리스크)",
            "구조/기능(structure/function) 표현만 사용: 'supports...', 'helps maintain...'",
            "DSHEA 디스클레이머 필수: 'This statement has not been evaluated by the FDA...'",
            "제조시설 GMP 준수",
            "라벨에 Supplement Facts 패널 필수",
        ],
        "banned_words": [
            "치료", "cure", "치료하다", "treat", "prevents", "예방",
            "진단", "diagnose", "질병", "disease", "암", "cancer",
            "당뇨", "diabetes", "고혈압", "hypertension",
            "reduces risk of", "fights", "kills", "eliminates",
            "anti-aging (의약품 맥락)", "heals", "restores",
        ],
        "safe_words": [
            "supports", "helps maintain", "promotes",
            "contributes to", "as part of a healthy lifestyle",
            "supports skin health", "supports gut health",
            "helps with occasional...", "supports healthy...",
        ],
        "reference": "https://www.fda.gov/food/information-industry-dietary-supplements",
    },
    "cosmetics_mocra": {
        "title": "화장품 (MoCRA)",
        "rules": [
            "시설 등록(Facility Registration) 필수",
            "제품 리스팅(Product Listing) 필수",
            "중대한 이상사례(Serious Adverse Event) 보고 의무",
            "향료/색소 알레르겐 라벨링",
            "GMP(Good Manufacturing Practice) 준수",
        ],
        "reference": "https://www.fda.gov/cosmetics/registration-listing-cosmetic-product-facilities-and-products",
    },
    "ftc_influencer": {
        "title": "인플루언서 광고/협찬 (FTC)",
        "rules": [
            "협찬/제휴/무료 제공 등 이해관계 명확히 공개",
            "#ad, #sponsored 등 눈에 띄는 위치에 표시",
            "플랫폼 내장 기능만으로 불충분할 수 있음",
            "허위/과장 후기 금지",
        ],
        "reference": "https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers",
    },
}

# ============================================================
# CONTENT PLAN (30-DAY)
# ============================================================
CONTENT_TOPICS_30DAY = [
    {"day": 1, "topic": "한국에서 다들 하는데 미국엔 없는 루틴 1가지", "pillar": "K-루틴 교육"},
    {"day": 2, "topic": "K-Beauty가 '피부 장벽'에 집착하는 이유", "pillar": "K-루틴 교육"},
    {"day": 3, "topic": "내가 미국에서 이 제품을 파는 이유(개인 경험 30초)", "pillar": "Build in public"},
    {"day": 4, "topic": "발효 식문화가 피부/컨디션 루틴에 들어오는 방식", "pillar": "K-루틴 교육"},
    {"day": 5, "topic": "7일 챌린지: 아침 루틴 2분 버전", "pillar": "K-루틴 교육"},
    {"day": 6, "topic": "OEM 공장에서 첫 샘플 받은 날 (비하인드)", "pillar": "Build in public"},
    {"day": 7, "topic": "고객 후기: 7일 챌린지 참가자 before/after", "pillar": "Proof"},
    {"day": 8, "topic": "한국 엄마들이 꼭 챙기는 아침 식단 루틴", "pillar": "K-루틴 교육"},
    {"day": 9, "topic": "아마존 리스팅 준비 과정 공개", "pillar": "Build in public"},
    {"day": 10, "topic": "Gut-Skin Axis: 장 건강이 피부에 미치는 영향 (과학)", "pillar": "K-루틴 교육"},
    {"day": 11, "topic": "패키지 디자인 A vs B — 어떤 게 나은가요?", "pillar": "Build in public"},
    {"day": 12, "topic": "콜라겐 스틱 vs 콜라겐 음료 — 뭐가 나은지 비교", "pillar": "K-루틴 교육"},
    {"day": 13, "topic": "DM으로 온 고객 질문에 답하기 (Q&A)", "pillar": "Proof"},
    {"day": 14, "topic": "한국 편의점 건강음료 Top 5 (미국에 왜 없을까)", "pillar": "K-루틴 교육"},
    {"day": 15, "topic": "첫 도매 바이어 미팅 후기", "pillar": "Build in public"},
    {"day": 16, "topic": "프로바이오틱이 피부에 좋은 이유 (3가지)", "pillar": "K-루틴 교육"},
    {"day": 17, "topic": "UGC 리뷰 모음: 실제 사용자들의 반응", "pillar": "Proof"},
    {"day": 18, "topic": "한국식 '스킨케어 루틴' 미국 버전으로 간소화하기", "pillar": "K-루틴 교육"},
    {"day": 19, "topic": "이번 달 매출 공개 (빌드 인 퍼블릭)", "pillar": "Build in public"},
    {"day": 20, "topic": "김치/된장/발효식품이 피부에 미치는 영향", "pillar": "K-루틴 교육"},
    {"day": 21, "topic": "30일 리셋 챌린지 중간 점검", "pillar": "Proof"},
    {"day": 22, "topic": "한국 vs 미국: 뷰티 루틴 차이점 TOP 3", "pillar": "K-루틴 교육"},
    {"day": 23, "topic": "첫 아마존 주문이 들어온 순간", "pillar": "Build in public"},
    {"day": 24, "topic": "피부 장벽 강화 식단 (한국식 + 미국식 재료)", "pillar": "K-루틴 교육"},
    {"day": 25, "topic": "인플루언서 시딩 결과: 20명에게 보내고 나서", "pillar": "Build in public"},
    {"day": 26, "topic": "이너뷰티 제품 고르는 기준 (성분표 읽는 법)", "pillar": "K-루틴 교육"},
    {"day": 27, "topic": "고객 전/후 사진 모음 (허가 받은 것만)", "pillar": "Proof"},
    {"day": 28, "topic": "왜 '구독 모델'인지 — 루틴은 꾸준해야 효과", "pillar": "K-루틴 교육"},
    {"day": 29, "topic": "이번 달 실수/교훈 3가지", "pillar": "Build in public"},
    {"day": 30, "topic": "30일 리셋 챌린지 최종 결과 & 다음 달 예고", "pillar": "Proof"},
]

# ============================================================
# FOUNDER STORY TEMPLATE
# ============================================================
FOUNDER_STORY_TEMPLATE = {
    "sections": [
        {"label": "예전의 나", "prompt": "(건강/피부/체력/멘탈/체중/커리어)에서 어떤 문제가 있었나요?", "example": "I struggled with..."},
        {"label": "전환점", "prompt": "무엇이 계기가 됐나요?", "example": "Everything changed when..."},
        {"label": "실험", "prompt": "어떤 루틴을 어떻게 바꿨나요? (한국식 장점 포함)", "example": "I started incorporating Korean..."},
        {"label": "결과", "prompt": "수치/체감/습관 변화는?", "example": "Within X weeks/months..."},
        {"label": "미션", "prompt": "이걸 미국에서 누구에게 어떤 방식으로 전달할 건가요?", "example": "Now I'm on a mission to help..."},
    ],
}

# ============================================================
# KPI METRICS
# ============================================================
KPI_CATEGORIES = {
    "sales": {
        "label": "매출/주문",
        "metrics": [
            {"name": "월매출 (KRW)", "target_monthly": "Phase별 상이", "unit": "원"},
            {"name": "주문 건수", "target_monthly": "-", "unit": "건"},
            {"name": "AOV (평균주문가)", "target_monthly": "75,000~150,000", "unit": "원"},
            {"name": "구독자 수", "target_monthly": "MoM 30%+", "unit": "명"},
        ],
    },
    "wholesale": {
        "label": "도매/B2B",
        "metrics": [
            {"name": "바이어 미팅 수", "target_monthly": "10+", "unit": "건"},
            {"name": "PO(구매주문서) 건수", "target_monthly": "2+", "unit": "건"},
            {"name": "PO 총액", "target_monthly": "Phase별 상이", "unit": "원"},
            {"name": "거래처 수", "target_monthly": "누적 관리", "unit": "개"},
        ],
    },
    "marketing": {
        "label": "마케팅/콘텐츠",
        "metrics": [
            {"name": "콘텐츠 발행 수", "target_monthly": "20+", "unit": "개"},
            {"name": "UGC 수", "target_monthly": "Phase별 상이", "unit": "개"},
            {"name": "이메일 리스트 크기", "target_monthly": "MoM 50%+", "unit": "명"},
            {"name": "SNS 팔로워", "target_monthly": "MoM 30%+", "unit": "명"},
        ],
    },
    "financial": {
        "label": "재무",
        "metrics": [
            {"name": "매출총이익률", "target_monthly": "40%+", "unit": "%"},
            {"name": "CAC (고객획득비용)", "target_monthly": "감소 추세", "unit": "원"},
            {"name": "LTV (고객생애가치)", "target_monthly": "증가 추세", "unit": "원"},
            {"name": "현금흐름", "target_monthly": "양(+)", "unit": "원"},
        ],
    },
}
