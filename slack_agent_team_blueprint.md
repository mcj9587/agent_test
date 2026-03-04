# Slack 스레드 기반 멀티 에이전트 팀 운영 설계도 (v1)

이 문서는 **"Slack에서 6개 역할 에이전트가 스레드로 협업"** 하는 시스템을 바로 구현할 수 있게, 이벤트/상태/UX/가드레일을 한 장짜리 운영 설계로 정리한 문서다.

## 1) 목표와 범위

- 목표: 채널에서 태스크를 시작하고, 하나의 스레드에서 `captain → pm → designer → fe → be → qa` 흐름을 자동화한다.
- v1 범위:
  - Slack App 1개 (역할은 메시지 prefix로 구분)
  - `/agent start`로 스레드 생성
  - 스레드 내 진행은 버튼 기반(`Status`, `Ship 요청`, `QA 승인/거절`)
  - JSON only 산출물 강제
  - QA 게이트 통과 전 ship 금지

---

## 2) 핵심 UX (사용자 관점)

### 2.1 채널에서 시작

1. 사용자가 채널에서 `/agent start <요청>` 실행
2. 봇이 채널에 Task 생성 메시지 게시
3. 해당 메시지의 `ts`를 `thread_ts`로 사용해 스레드 작업방 고정
4. 봇이 스레드 첫 메시지에 상태 보드 + 버튼 3개 첨부
   - `Status`
   - `Ship 요청`
   - `QA 승인/거절`

> 주의: 슬래시 커맨드는 스레드 내부 호출 제약이 있으므로, 스레드 내 조작은 인터랙션(버튼)으로 통일한다.

### 2.2 스레드 내부 진행

- Captain: 요구사항 분해 + 작업 순서/담당 배정
- PM: 산출물 정의/우선순위/완료 조건
- Designer: UX 카피/플로우/컴포넌트 가이드
- FE: 구현 계획/리스크/PR 요약
- BE: API/스키마/에러 처리 계획
- QA: 테스트 관점/통과 여부(`pass|fail`) + 코멘트

각 메시지는 아래 JSON 규격으로만 게시:

```json
{
  "task_id": "TASK-001",
  "agent": "qa",
  "status": "pass",
  "summary": "핵심 결과 요약",
  "artifacts": ["PR#12", "test-report-url"],
  "next_action": "ship 승인 가능"
}
```

---

## 3) 이벤트/핸들러 설계

### 3.1 Slack 수신 이벤트

- `command(/agent start)`
  - 즉시 ack (3초 이내)
  - Task 생성 + 채널 메시지 + thread_ts 저장
  - 비동기 큐에 `captain kickoff` 작업 enqueue

- `app_mention` (선택)
  - 스레드 내 멘션 시 현재 단계 재실행/요약

- `block_actions` (버튼 클릭)
  - `status_btn`: 현재 단계/최근 산출물 요약 출력
  - `ship_btn`: QA `pass`일 때만 ship 진행
  - `qa_gate_btn`: QA 상태 전환(pass/fail)

### 3.2 내부 워커 잡 타입

- `run_agent_step(task_id, agent_name)`
- `retry_json_format(task_id, agent_name)`
- `post_status_snapshot(task_id)`
- `ship_task(task_id)`

---

## 4) 상태 저장 스키마 (최소)

### 4.1 `tasks`

- `task_id` (PK)
- `channel_id`
- `thread_ts`
- `title`
- `status` (`created|in_progress|qa_pending|qa_failed|qa_passed|shipped`)
- `current_agent`
- `created_at`, `updated_at`

### 4.2 `agent_outputs`

- `id` (PK)
- `task_id` (FK)
- `agent_name`
- `payload_json` (TEXT/JSON)
- `slack_message_ts`
- `created_at`

### 4.3 `qa_gate`

- `task_id` (PK/FK)
- `qa_status` (`pending|pass|fail`)
- `qa_note`
- `reviewed_by`
- `reviewed_at`

### 4.4 `event_dedup`

- `event_key` (PK)  
  예: `event_id` 또는 `channel_id:ts:action_id`
- `first_seen_at`

---

## 5) 라우팅 규칙 (에이전트 체인)

기본 체인:

1. `captain`
2. `pm`
3. `designer`
4. `fe`
5. `be`
6. `qa`

전이 규칙:

- 각 단계 성공 + JSON 유효성 통과 시 다음 에이전트 enqueue
- JSON 파싱 실패 시 같은 에이전트에 `JSON만 재출력` 1~2회 재시도
- QA 결과가 `fail`이면 `qa_failed`로 종료(또는 captain으로 롤백 옵션)
- QA 결과가 `pass`이면 `qa_passed`로 전이 후 `Ship 요청` 가능

---

## 6) 가드레일 (운영 필수)

1. **3초 ack 보장**
   - Slack 수신 직후 ack
   - LLM 호출/외부 API는 전부 비동기 워커

2. **중복 처리 방지**
   - 이벤트 수신 시 `event_dedup` 선조회
   - 있으면 즉시 skip

3. **JSON only 강제**
   - 시스템 프롬프트에 JSON 스키마 고정
   - 파싱 실패 시 자동 재시도

4. **QA gate 강제**
   - `ship_btn` 클릭 시 `qa_gate.qa_status == pass` 검증
   - 아니면 ship 거절 + 사유 안내

---

## 7) Ship/배포 연동 (선택)

- v1: Slack 내부 상태만 `shipped` 처리
- v1.5+: GitHub 보호 브랜치 + required check 연동
  - 체크명 예: `qa-approved`
  - QA pass 시 성공 상태 업로드

---

## 8) 구현 순서 (현실적인 5단계)

1. Slack Bolt 앱 기동 + Socket Mode 연결 확인
2. `/agent start`로 task/thread 생성 + DB 저장
3. captain~qa 체인 워커 연결 + JSON 검증
4. 스레드 버튼(`Status/Ship/QA`) 액션 연결
5. QA gate 강제 + ship 조건 검증

---

## 9) 운영 체크리스트

- [ ] `/agent start` 요청 후 1초 내 확인 메시지가 온다
- [ ] thread_ts가 DB에 저장된다
- [ ] 각 에이전트 메시지가 JSON 파싱 가능하다
- [ ] 동일 이벤트 재전송 시 중복 실행되지 않는다
- [ ] QA fail 상태에서 ship이 차단된다
- [ ] QA pass 상태에서만 ship이 허용된다

이 체크리스트가 통과되면, v1 운영 가능한 수준이다.
