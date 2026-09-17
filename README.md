# 202609_NOLOGINMAIN — U+유모바일 nologinMain 페이지 개편

비로그인 메인 페이지(nologinMain)의 **개선목표 정의 · 요구사항 정의 · 동작 프로토타입**을 만드는 프로젝트.
2026-09-17 초기화 상태로 셋팅. 내용은 자료 분석과 함께 채운다.

## 폴더 구조

```
202609_NOLOGINMAIN/
├── README.md                      이 문서
├── docs/
│   ├── 00_Baseline.md             공통 기준 — 단일 진실 원천 (C/O/D · 근거 등급 · 표준 문구)
│   ├── 01_개선목표_정의서.md       왜 개편하는가 — 현황 · 페인포인트(P) · 원칙(G) · 목표 지표(M)
│   └── 02_요구사항_정의서.md       무엇을 만드는가 — 영역별 확정 사항(C) · 데이터 규칙 · 예외(EX)
├── index.html                     통합 리포트 (3탭: 01 프로토타입 · 02 개선목표 · 03 요구사항 정의서) — GitHub Pages 루트
├── .nojekyll                      Pages 빌드 우회
├── font/PretendardVariable.woff2  페이지 공통 폰트 (index.html @font-face, 상대경로)
└── assets/
    ├── captures/                  AS-IS 화면 캡처 (리포트에는 base64 임베딩)
    └── data/                      분석 자료 (Clarity 추출 · 시트 · 전달 문서)
```

## 이전 프로젝트(PLANLIST_20260901_V1.0)에서 가져온 것 / 뺀 것

| 가져온 것 | 뺀 것 |
|---|---|
| 리포트 크롬 CSS (`r-*` 접두사) · 디자인 토큰 · 탭 골격(제목 → 역할 한 문장 → KPI) | 02 화면설계 · 03 기능정의 · 05 테스트 케이스 · 06 변경 이력 탭 |
| Baseline ID 체계 (C / O / D / P / G / EX) 와 근거 등급 태그 | 요금제 선택 화면의 수치 · 문구 · 확정 사항 66건 전부 |
| ID 칩 호버 상세(`.cid.has-tip`) · 확정 카운터 자동 집계 | PC 700px 프레임 · 769px 브레이크포인트 (가입신청서 팝업 전용) |
| 모바일 기기 프레임 394×940 (`.phone`) · 자유 조작 / 시나리오 시뮬레이터 뷰 전환 | 프로토타입 화면 내부 CSS·JS (요금제 카드 · 필터 · 비교 시트) |

## 진행 순서

1. `assets/data/`, `assets/captures/` 에 자료를 넣는다 (Clarity 추출 · 실제 화면 캡처 · 요구사항 시트)
2. 실제 nologinMain을 끝까지 걸어보고 URL · 상태 변화를 기록한다 → `01_개선목표_정의서.md` 1장
3. 페인포인트(P) · 원칙(G) · 목표 지표(M) 확정 → `01_개선목표_정의서.md` 2~3장 → 리포트 02 탭 반영
4. 영역 구분 → 확정 사항(C) · 미확정(O) · 협의(D) → `00_Baseline.md` 먼저, `02_요구사항_정의서.md` 본문, 리포트 03 탭
5. 프로토타입 화면 구현 (`index.html` PROTO 블록) · 시나리오 시뮬레이터 정의
6. 외부 적대적 리뷰 → `git push` → GitHub Pages 반영 확인 (`?v=n` 캐시 우회)

## 문장 규칙 (모든 리포트 · 문서 공통)

- 명사형 종결. 간결한 문장. 난해한 표현 · 장황한 풀어쓰기 금지
- 중복 표현 · 불필요한 내용 제외
- 예: "선택 후 확정까지 화면 이동이 필요 없도록 설계했습니다" → "선택→확정 화면 이동 없음"

## 운영 규칙 (요약)

- 변경은 **Baseline 먼저** → 문서 본문 → 리포트 → 버전·카운터 일치 확인
- 근거 열은 `[관측] [데이터] [추론] [합의]` 중 하나로 비워두지 않는다
- 리포트 크롬은 `r-` 접두사, 프로토타입 CSS는 접두사 없음 — 서로 손대지 않는다
- 외부 CDN · localStorage 금지. 캡처는 base64 임베딩
- JS 검증: `node -e "const s=require('fs').readFileSync('index.html','utf8');const i=s.lastIndexOf('<script>')+8,j=s.lastIndexOf('</script>');try{new Function(s.slice(i,j));console.log('JS OK')}catch(e){console.log('ERR',e.message)}"`

## 저장소 · 배포

- 저장소: https://github.com/jiwonida-dotcom/nologinmain (이 폴더가 저장소 루트)
- 배포 URL: https://jiwonida-dotcom.github.io/nologinmain/ — Settings → Pages → `main / (root)` 설정 후 반영
- **Public 저장소면 실제 서비스 URL 구조 · 분석 수치가 외부에 노출된다.** 수치를 넣기 전에 공개 범위를 확인한다

## 참조

- 이전 프로젝트 배포본: https://jiwonida-dotcom.github.io/PLANLIST_20260901_V1.0/
- 적용 skill: `requirement-to-prototype`(산출물 체계) · `observed-ux-improvement`(근거 등급 · 검증 공정)
