# 계정 이관 안내서 — nologinMain 개편 (2026-09-18)

이전 계정 `jiwonida@gmail.com` 의 Cowork 프로젝트 「유모바일 nologinmain 페이지 개편」을 다른 계정으로 이관하기 위한 패키지.
**새 계정의 첫 세션은 이 문서 → `docs/00_Baseline.md` → `handover/claude_project/04_프로토타입_구현_메모.md` 순으로 읽고 착수한다.**

## 1. 무엇이 어디에 있는가

| 구분 | 이관 방법 | 위치 |
|---|---|---|
| 저장소 · 산출물 (문서 · index.html · 자산) | 계정 무관 — 로컬 폴더 + GitHub | `D:\ClaudeProject\202609_NOLOGINMAIN` = https://github.com/jiwonida-dotcom/nologinmain (main) |
| Claude Project 문서 5건 (셋팅 현황 · AS-IS 관측 · 개편안 분석 · 작성 규칙 · 구현 메모) | 파일로 보존 → 새 Project 에 다시 업로드 | `handover/claude_project/` |
| Project 설명(시스템 지시) | 아래 §3 원문 | 이 문서 |
| 커스텀 skill 3건 | SKILL.md 보존 → 새 계정에 다시 등록 | `handover/skills/` |
| 커넥터 (Figma · Microsoft Clarity · Chrome 확장 · 로컬 폴더) | 새 계정에서 다시 연결 | §2 체크리스트 |
| 대화 이력 · 프로젝트 메모리 | **이관 불가** — 필요한 결정은 문서에 이미 기록됨 | — |

## 2. 새 계정 셋업 체크리스트

1. GitHub — 저장소 `jiwonida-dotcom/nologinmain` 접근 권한 확인. 새 계정으로 push 할 PC 에 Git Credential Manager 로그인. (저장소 소유자를 바꿀 경우 `push.cmd` · README · Baseline 의 URL 갱신)
2. Cowork 새 Project 생성 — 이름 `유모바일 nologinmain 페이지 개편`, 설명은 §3 원문 그대로
3. Project 문서 업로드 — `handover/claude_project/00~04*.md` 5건
4. Skill 등록 — `handover/skills/*/SKILL.md` 3건을 새 계정 skill 로 등록 (`requirement-to-prototype` · `observed-ux-improvement` 필수, `clarity-ux-report` 는 O-08 데이터 수령 후 사용)
5. 커넥터 연결 — Figma (`2026.09-Nologin-Main` 파일 접근), Microsoft Clarity (O-08), Claude in Chrome 확장 (Figma 자산 캡처 · 실서비스 워크스루에 사용했음)
6. 데스크톱 앱에서 폴더 연결 — `D:\ClaudeProject\202609_NOLOGINMAIN`
7. 첫 세션 착수 문구 예: 「`handover/HANDOVER.md` 읽고 `docs/00_Baseline.md` 기준으로 현황 요약 후 대기」

## 3. Project 설명 원문 (그대로 복사)

```
당신은 nologinMain 개편의 요구사항 정의 및 설계를 담당하는 UI/UX 전문가 입니다.
개편 목표와 요구사항을 정의하고 프로토타입을 생성합니다.
```

## 4. 현재 상태 (2026-09-18 기준, 최신 커밋 `15d1f46`)

- 작업 트리 클린, origin/main 과 동기 (push 완료 상태)
- 배포: GitHub Pages `main / (root)` → https://jiwonida-dotcom.github.io/nologinmain/ (반영 확인은 `?v=n` 캐시 우회)
- `index.html` 3탭 리포트 (01 프로토타입 · 02 개선목표 · 03 요구사항 정의서). 약 930KB, 이미지 · 폰트 임베딩
- 프로토타입 구현 범위: **홈 탭** 완료(배너 · 로그인 블록 · 타임딜 · 요금제 카드 · 휴대폰 카드 · 결합 · 고객센터 · 푸터, 가로 플리킹) · **요금제 탭** 완료(타이틀 · 필터바 · 리스트형 PlaneCard 5장 · 유형 필터 · 초기화). **휴대폰 · 유픽폰 탭 미구현**
- 기기 프레임: 모바일 446×940 단일 (Figma 510 프레임 zoom .87). 폰트 하한 14px, Pretendard 통일
- Baseline v0.4: 확정 C 5건 · 미확정 O 9건(해소 2 · 부분 해소 1) · 협의 D 0건 · 표준 문구 전부 미확정
- `Claude outputs/` 폴더: 리포트 버전 스냅샷(index_v3 · v4 등). 참고용, 정본은 루트 `index.html`

## 5. 미확정 · 열린 항목 (새 계정에서 이어갈 것)

| ID | 항목 | 상태 |
|---|---|---|
| O-02 | 데이터량 5단계 선택 — 제거 / 요금제 탭 이동, `nologPpnSearchBann` 랜딩 폐기 여부 | 미확정 |
| O-03 | 타임딜 타이머 · 참여 인원 · 이벤트 코드 — 실데이터 / 운영자 입력, 백오피스 범위 | 미확정 |
| O-04 | 배너 6장 자동 회전 여부 (G-07 범위) | 미확정 |
| O-05 | 로그인 블록 배치 이유 · 위치 의도 | 미확정 |
| O-06 | 홈 탭 4 — 휴대폰(40007051:18419) · 유픽폰(40007051:19201) 탭 미구현 | 부분 해소 |
| O-08 | Clarity · GA 데이터 제공 시점 → P 우선순위 · M 현재값 | 미확정 |
| O-09 | 요금제 탭 필터 · 정렬 바텀시트 Figma 미정의 | 미확정 |
| — | 개편안 분석 초안(G-01~07)은 전부 [추론] — 사용자 확인 후 승격 | 확인 대기 |
| — | 터치 타깃 44px 미달 다수(Figma 수치 유지) — 확대 여부 | 미결 |
| — | 이전 프로젝트 이관 기준(터치 타깃 · 상태 표현 · 포커스) [추론] 재확인 | 재확인 |

## 6. 다음 단계 (README 진행 순서 기준)

1. O-02~O-09 확인 답변 수령 → Baseline 갱신 → 02_요구사항 → 리포트 03 탭
2. 휴대폰 · 유픽폰 탭 구현 (Figma 프레임 확인됨)
3. `assets/data/` 에 Clarity · GA 자료 투입 → 01_개선목표 P · M 확정 → 리포트 02 탭
4. 외부 적대적 리뷰 → push → Pages 반영 확인

## 7. 운영 규칙 요약 (상세는 README · Baseline · 03_작성_규칙)

- 변경은 **Baseline 먼저** → 문서 본문 → 리포트 → 버전 · 카운터 일치
- 근거 열 `[관측] [데이터] [추론] [합의]` 필수. 임의 의사결정 금지, 확정 전 사용자 확인
- 문장: 명사형 종결 · 간결 · 중복 금지
- CSS 접두사: 리포트 `r-` · 프로토타입 `np-` · 프레임 `.phone` — 서로 손대지 않음
- 외부 CDN · localStorage 금지. 이미지 base64 임베딩. 폰트 `font/PretendardVariable.woff2` 상대경로
- JS 검증: `node -e "const s=require('fs').readFileSync('index.html','utf8');const i=s.lastIndexOf('<script>')+8,j=s.lastIndexOf('</script>');try{new Function(s.slice(i,j));console.log('JS OK')}catch(e){console.log('ERR',e.message)}"`
- 커밋 · push: 세션은 로컬 커밋까지, push 는 사용자가 `push.cmd` 실행 (인자 없으면 메시지 자동 생성)
- Public 저장소 — 실서비스 URL · 분석 수치 노출 주의. 수치 투입 전 공개 범위 확인
