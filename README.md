# K-Wellness Agent Bot

Korean Wellness / K-Beauty / K-Food 사업 실행을 위한 인터랙티브 CLI 에이전트 봇.

**목표: 2026년 100억 KRW 매출 + 50억 KRW 자산**

## Quick Start

```bash
# 프로젝트 루트에서 실행
python -m k_wellness_agent
```

## Features

| 기능 | 커맨드 | 설명 |
|------|--------|------|
| **대시보드** | `dashboard` | 전체 사업 현황 요약 |
| **3트랙 전략** | `strategy` | 유통/브랜드/미디어 전략 |
| **재무 모델링** | `finance` | 매출 프로젝션, 마진 분석, 채널 믹스 |
| **로드맵** | `roadmap` | 10개월 로드맵 (4 Phase) |
| **태스크 관리** | `week1` / `done <id>` | Week-1 체크리스트 + 커스텀 태스크 |
| **템플릿** | `templates` | 라인시트, 피치 스크립트, 이메일, 브랜드 스토리 |
| **컴플라이언스** | `compliance` / `scan <text>` | FDA/FTC/MoCRA 가이드 + 문구 스캔 |
| **콘텐츠 플래너** | `calendar` / `brief <day>` | 30일 콘텐츠 캘린더 + 스크립트 브리프 |
| **KPI 트래킹** | `kpi` / `kpi log` | 주간 KPI 기록 + 트렌드 분석 |

## Usage Examples

```
K-Wellness> status              # 현재 Phase, 채널 믹스, Week-1 진행률
K-Wellness> finance             # 재무 대시보드 (마진표 + 10개월 프로젝션)
K-Wellness> done 1              # Week-1 태스크 #1 완료 처리
K-Wellness> scan This cures acne  # 마케팅 문구 FDA 리스크 스캔
K-Wellness> brief 5             # Day 5 콘텐츠 스크립트 브리프
K-Wellness> templates           # 라인시트/피치/이메일 등 전체 템플릿 생성
K-Wellness> kpi log 1 revenue=50000000 orders=100  # 주간 KPI 기록
```

## Architecture

```
k_wellness_agent/
  app.py                  # Main CLI (interactive REPL)
  __main__.py             # python -m entry point
  data/
    business_plan.py      # Core business data (strategy, roadmap, KPIs, etc.)
  modules/
    financial_model.py    # Revenue projection, margin analysis
    roadmap_tracker.py    # Roadmap phases, week-1 checklist, custom tasks
    templates.py          # Line sheet, pitch script, email, brand story
    compliance.py         # FDA/FTC/MoCRA compliance checker
    content_planner.py    # 30-day content calendar, briefs
    kpi_dashboard.py      # KPI framework, weekly logging, trends
  exports/                # Generated files (templates, reports, KPI data)
```

## Strategy Summary

**3-Track Revenue Model:**
1. **Track 1 (Volume):** 검증된 K-브랜드 총판/유통 → 70억 도매/B2B
2. **Track 2 (Brand):** 하우스 브랜드 히어로 제품 → 30억 DTC (구독/번들)
3. **Track 3 (Media):** 퍼블릭 피겨/인플루언서 엔진 → CAC 절감

**Recommended Hero Product:** 이너뷰티 스틱/파우더 (highest margin + subscription fit)

## Requirements

- Python 3.8+
- No external dependencies (stdlib only)
