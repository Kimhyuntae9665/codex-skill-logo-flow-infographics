# 복사해서 쓰는 Logo Flow 예제

이 스킬은 기술 사이의 관계를 **로고와 화살표로 설명하는 SVG·PNG**를 만듭니다. 데이터베이스를 설치하거나 API를 연결하는 스킬은 아닙니다. 그림에 로고가 있다는 사실만으로 해당 기술을 실제 프로젝트에 썼다고 판단하지 않습니다.

흰 카드 안에는 검증한 **독립 심볼만**, 카드 바로 아래에는 **정확한 기술 이름**을 둡니다. 역할 설명과 분기 의미는 그림 밖의 설명에 적습니다. “카드 안의 글자를 빼줘”라고 요청해도 카드 아래 이름은 유지합니다.

[설치와 기본 사용법](../README.md) · [입력 형식](../references/input-contract.md) · [내보내기 검수](../references/export-checks.md)

## 먼저 확인할 세 가지

1. **무엇을 그릴지:** 연결 방향과 분기·합류 의미를 적습니다. 설계안인지, 사용자에게 받은 흐름인지, 코드를 확인한 결과인지 구분합니다.
2. **어떤 로고를 쓸지:** 승인한 로컬 파일을 주거나 “공식 로고를 찾아 사용해줘”라고 요청합니다. 공식 독립 심볼을 우선하며, 모델 제품명과 로고 브랜드명을 혼동하지 않습니다.
3. **어떤 파일이 필요한지:** 편집용 SVG, 공유용 PNG, 출처 기록용 manifest를 요청합니다. PNG 변환에는 이미 사용 가능한 렌더러가 필요합니다.

아래 프롬프트는 Codex에 그대로 붙여 넣어 사용할 수 있습니다. “첨부한” 자료를 사용하는 예제는 그 자료를 먼저 함께 제공하세요. 공개 로고를 찾으라는 예제는 필요한 공개 브랜드 파일의 다운로드를 포함합니다. 다운로드 출처와 사용 조건은 결과 manifest에 남깁니다.

## 다운로드해서 살펴보는 갤러리

아래 여섯 갤러리는 공식 프로젝트 원본 또는 고정 리비전의 Simple Icons에서 확보한 실제 심볼로 **배치와 연결 형태**를 보여주는 제안 예제입니다. 자산 출처와 공식 원본 대신 라이브러리 변형을 선택한 이유는 [출처 기록](../examples/assets/SOURCES.md)과 각 manifest에서 확인할 수 있습니다. 실제 로고를 썼더라도 서비스나 CI/CD를 구현·실행했다는 증거는 아닙니다.

별도의 [기존 스타일 샘플 SVG](../preview/example.svg)와 [PNG](../preview/example.png)는 Alpha·Beta·Gamma·Delta라는 가상 이름과 직접 만든 도형을 사용합니다. 이 파일은 배치 확인용이며, 그 도형을 Python·Qwen·Qdrant 등의 실제 로고처럼 사용하지 마세요. [스타일 샘플 manifest](../preview/example.manifest.json)에서도 원본 예제 자산임을 구분합니다.

각 폴더의 `graph.json`은 노드·화살표·좌표를 담고, `output.svg`는 편집 가능한 결과, `output.png`는 이미지 결과, `output.manifest.json`은 상태와 자산 출처 기록입니다. 아래 링크에서 파일을 열어 저장하거나 저장소를 내려받아 사용할 수 있습니다.

| 예제 | 읽는 방법 | 입력과 결과 |
| --- | --- | --- |
| 01 · 직선 | 한 단계의 결과가 다음 단계로 전달됩니다. | [graph.json](../examples/01-linear/graph.json) · [SVG](../examples/01-linear/output.svg) · [PNG](../examples/01-linear/output.png) · [manifest](../examples/01-linear/output.manifest.json) |
| 02 · 분기 | 하나의 출발점에서 여러 목적지로 나갑니다. | [graph.json](../examples/02-fan-out/graph.json) · [SVG](../examples/02-fan-out/output.svg) · [PNG](../examples/02-fan-out/output.png) · [manifest](../examples/02-fan-out/output.manifest.json) |
| 03 · 합류 | 여러 출발점이 하나의 목적지로 모입니다. | [graph.json](../examples/03-fan-in/graph.json) · [SVG](../examples/03-fan-in/output.svg) · [PNG](../examples/03-fan-in/output.png) · [manifest](../examples/03-fan-in/output.manifest.json) |
| 04 · 다이아몬드 | 분기한 두 경로가 뒤에서 다시 합쳐집니다. | [graph.json](../examples/04-diamond/graph.json) · [SVG](../examples/04-diamond/output.svg) · [PNG](../examples/04-diamond/output.png) · [manifest](../examples/04-diamond/output.manifest.json) |
| 05 · 병렬 경로 | 연결되지 않은 두 흐름을 나란히 비교합니다. | [graph.json](../examples/05-parallel/graph.json) · [SVG](../examples/05-parallel/output.svg) · [PNG](../examples/05-parallel/output.png) · [manifest](../examples/05-parallel/output.manifest.json) |
| 06 · CI/CD 형태 | 검사 경로를 분기하고 다음 단계로 모으는 배치를 보여줍니다. | [graph.json](../examples/06-ci-cd/graph.json) · [SVG](../examples/06-ci-cd/output.svg) · [PNG](../examples/06-ci-cd/output.png) · [manifest](../examples/06-ci-cd/output.manifest.json) |

저장소 루트에서 모든 예제를 SVG로 다시 만들려면 다음과 같이 실행합니다. Python 3.9 이상이 필요하며 출력은 원본 갤러리와 분리한 `output/gallery/`에 저장합니다.

```powershell
python -X utf8 scripts/render_examples.py --output output/gallery
```

PNG도 필요하다면 이미 설치한 렌더러를 명시합니다. 아래 두 명령 중 사용 가능한 렌더러에 맞는 하나를 실행하세요. CairoSVG에는 해당 Python 환경의 설치가 필요하고, Inkscape는 PATH에서 찾을 수 있어야 합니다. 이 명령은 패키지나 렌더러를 설치하지 않습니다.

```powershell
python -X utf8 scripts/render_examples.py --output output/gallery --png-renderer cairosvg
```

```powershell
python -X utf8 scripts/render_examples.py --output output/gallery --png-renderer inkscape
```

직선 예제 하나만 기존 helper로 다시 만들 수도 있습니다. 아래 PNG 변환 명령에는 이미 설치된 Inkscape가 필요합니다.

```powershell
python -X utf8 scripts/render_logo_flow.py examples/01-linear/graph.json --svg work/linear/output.svg --png work/linear/output.png
```

Inkscape가 없다면 같은 helper로 SVG만 만들 수 있습니다.

```powershell
python -X utf8 scripts/render_logo_flow.py examples/01-linear/graph.json --svg work/linear/output.svg
```

## 12가지 요청 예제

### 1. 직선: 수집 → 저장 → 조회

한 줄짜리 관계를 처음 만들 때 쓰기 좋습니다. 아래 흐름은 제안이며 실제 연동을 주장하지 않습니다.

```text
$logo-flow-infographics
Python → SQLite → Streamlit 순서의 왼쪽에서 오른쪽으로 읽는 설계 그림을 만들어줘.
Python으로 데이터를 준비하고 SQLite에 저장한 뒤 Streamlit에서 조회하는 제안이야. 실행한 시스템으로 표현하지 마.
각 기술의 공식 독립 심볼을 찾아 사용해줘. 흰 카드 안에는 심볼만, 카드 바로 아래에는 Python, SQLite, Streamlit 이름을 넣어줘.
어두운 점 배경과 얇은 곡선 화살표로 그리고, 단계 설명은 그림 밖에 적어줘.
SVG·PNG와 출처 및 해시를 담은 manifest를 저장하고 실제 이미지를 열어 확인해줘.
```

### 2. 분기: 하나의 처리기에서 두 저장소로

여기서 화살표는 데이터를 보내는 관계를 뜻합니다. 동시 실행이나 처리 속도까지 뜻하지 않습니다.

```text
$logo-flow-infographics
Python에서 PostgreSQL과 Redis로 각각 화살표가 나가는 분기 설계안을 그려줘.
PostgreSQL은 영구 저장, Redis는 캐시 용도의 제안이야. 두 목적지 사이의 화살표는 없어.
공식 독립 심볼을 찾아 쓰고 카드 아래 이름을 각각 정확하게 표시해줘.
Python은 왼쪽 가운데, PostgreSQL은 오른쪽 위, Redis는 오른쪽 아래에 배치해줘.
분기가 두 저장소로의 데이터 전달이라는 설명과 proposed 상태를 그림 밖 및 manifest에 남겨줘. SVG·PNG를 내보내고 화살표가 라벨을 가리지 않는지 확인해줘.
```

### 3. 합류: 두 입력 경로에서 하나의 저장소로

입력 두 개를 보여주되, 입력 경로 사이에 존재하지 않는 연결을 추가하지 않습니다.

```text
$logo-flow-infographics
FastAPI → PostgreSQL, Streamlit → PostgreSQL 두 연결이 하나의 저장소로 모이는 제안 그림을 만들어줘.
FastAPI는 API 입력 경로, Streamlit은 관리 화면 입력 경로라는 설계 가정이야. 둘 사이의 연결은 그리지 마.
FastAPI와 Streamlit은 왼쪽 위아래, PostgreSQL은 오른쪽 가운데에 배치해줘.
공식 독립 심볼을 찾아 흰 카드 안에 넣고 이름은 카드 아래에 유지해줘. 역할 설명은 그림 밖에 둬.
합류가 두 입력 경로의 저장을 뜻한다는 설명, 제안 상태, 자산 출처를 남기고 SVG·PNG를 검수해줘.
```

### 4. 다이아몬드: 분기 후 다시 합류

마름모 모양의 배치와 조건 분기 기호는 다릅니다. 아래 예제에는 예/아니오 판단 조건이 없습니다.

```text
$logo-flow-infographics
FastAPI에서 Redis와 PostgreSQL로 분기한 다음, 두 저장소에서 Python으로 합류하는 다이아몬드 형태의 설계 그림을 만들어줘.
연결은 FastAPI→Redis, FastAPI→PostgreSQL, Redis→Python, PostgreSQL→Python 네 개뿐이야.
Python은 두 저장소 결과를 받아 정리하는 처리기의 제안이야. 두 경로가 반드시 동시에 실행되거나 성공해야 한다는 의미를 추가하지 마.
공식 독립 심볼을 찾아 쓰고 각 카드 아래 기술 이름을 넣어줘. 분기와 합류의 의미는 그림 밖에서 설명해줘.
SVG·PNG·manifest를 저장하고 곡선 화살표가 교차하거나 카드 아래 이름을 가리지 않는지 확인해줘.
```

### 5. 병렬: 독립된 두 경로 비교

서로 연결되지 않은 흐름은 화살표로 이어 붙이지 않습니다.

```text
$logo-flow-infographics
위쪽에는 Python → SQLite, 아래쪽에는 JavaScript → PostgreSQL을 나란히 그려줘.
두 경로는 비교용 제안이며 서로 독립적이야. 위아래를 연결하는 화살표와 성능 수치는 추가하지 마.
실제 공식 독립 심볼을 찾아 사용하고, 각 카드 아래에 정확한 기술 이름을 넣어줘.
두 행의 카드 크기와 간격을 맞추고, 비교용 제안이라는 설명은 그림 밖에 둬.
SVG·PNG와 manifest를 저장하고 두 행 모두 로고 비율·이름·연결 방향을 확인해줘.
```

### 6. 데이터 검색: RAG 구성 제안

모델 이름은 로고 브랜드와 구분합니다. 공통 계열 심볼을 재사용했다면 그 사실을 기록합니다.

```text
$logo-flow-infographics
Python → Qwen3 Embedding → Qdrant → Qwen3 순서의 검색 기반 답변 구성 제안을 그려줘.
Python은 질문을 준비하고, Qwen3 Embedding은 질문 벡터를 만들고, Qdrant는 관련 문서를 검색하고, Qwen3는 검색 문서를 참고해 답변한다는 설계야. 문서 적재 경로는 이번 그림에서 제외해줘.
실제 구현이나 검색 품질 측정 결과로 표현하지 마. 각 기술의 공식 독립 심볼을 찾아 사용해줘.
Qwen 계열의 공통 심볼만 확인되면 검증된 심볼을 두 카드에 재사용하고, 아래 이름은 Qwen3 Embedding과 Qwen3로 구분해줘. 이 재사용도 manifest에 적어줘.
흰 카드 안은 심볼만 유지하고 역할은 그림 밖에 설명해줘. SVG·PNG·manifest를 내보내고 모델 이름과 로고 출처를 대조해줘.
```

### 7. 코드 확인: 실제 근거에서 흐름 추출

이 경우에는 사용자의 설명만으로 `implemented`라고 표시하지 않습니다. 코드가 보여주는 범위와 실행 확인 여부를 별도로 남깁니다.

```text
$logo-flow-infographics
현재 열린 저장소의 README, 의존성 파일, 진입점과 데이터 처리 코드를 확인해서 기술 흐름 그림을 만들어줘.
실제로 확인한 호출·데이터 전달 관계만 화살표로 넣고, 패키지 목록에 있다는 이유만으로 연결하지 마. 파일 경로와 확인한 커밋을 근거 기록에 남겨줘.
구현 코드에서 확인한 부분과 제안·미확인 부분을 분리하고 실행 여부도 설명해줘. 근거가 부족한 노드나 연결은 임의로 채우지 마.
확인된 기술의 공식 독립 심볼을 찾아 사용해줘. 카드 안은 심볼만, 아래는 정확한 기술 이름으로 구성해줘.
역할과 근거는 그림 밖에 적고 SVG·PNG·manifest를 저장해줘. 출력 이미지와 확인한 코드의 노드·연결을 대조해줘.
```

### 8. 제공한 자산: 다운로드 없이 그리기

로컬 파일과 이름·출처 정보를 함께 제공하면 자산 선택을 재현하기 쉽습니다.

```text
$logo-flow-infographics
첨부한 로컬 로고 파일과 자산 목록만 사용해서 Python → Qdrant → Streamlit 제안 그림을 만들어줘.
자산 목록의 이름·출처·사용 조건과 파일의 SHA-256을 manifest에 기록해줘. 새 다운로드나 설치는 하지 마.
파일이 실제 기술의 독립 심볼인지 확인하고, 전체 워드마크이거나 이름과 맞지 않는 파일이면 조용히 대체하지 말고 해당 제한을 알려줘.
승인한 PNG 자산이 있다면 SVG 전용 helper에 억지로 넣지 말고 이미 사용 가능한 다른 렌더러로 원본을 보존해줘.
카드 안은 심볼만, 이름은 카드 아래에 넣어 SVG·PNG를 만들고 실제 픽셀을 확인해줘.
```

### 9. 라벨만 수정: 기존 배치와 연결 보존

전체 재배치 없이 카드 내부의 잘못된 글자를 바로잡는 요청입니다.

```text
$logo-flow-infographics
첨부한 기존 SVG의 노드 위치·카드 크기·연결·화살표 방향·전체 구성을 유지해줘.
카드 안에는 실제 독립 심볼만 남기고, 기술 이름은 각 카드 바로 아래에 넣어줘. 이미 카드 아래에 있는 이름은 지우지 마.
심볼에 글자가 결합된 워드마크가 들어 있으면 글자를 덮거나 로고를 다시 그리지 마. 공식 독립 심볼을 찾아 사용하고 교체 출처를 기록해줘.
Ollama 로고를 Llama로 표기하는 식의 이름 오류도 자산 출처와 대조해 바로잡아줘.
수정 SVG·PNG·manifest를 저장하고 원본과 노드 위치·연결 수·외부 이름을 비교해줘.
```

### 10. 공식 심볼 없음: 텍스트 카드로 대체

가짜 브랜드 로고를 만드는 것보다 기술 이름을 그대로 읽을 수 있는 카드가 낫습니다. 이 대체는 SVG 자산을 요구하는 기본 helper가 지원하지 않으므로 다른 렌더러가 필요합니다.

```text
$logo-flow-infographics
첨부한 기술 목록과 흐름을 그림으로 만들어줘. 각 기술의 공식 독립 심볼을 먼저 찾아 확인해줘.
사용할 수 있는 심볼을 확인하지 못한 기술은 그 사실을 기록하고 해당 노드를 텍스트 이름 카드로 표현해줘. 가상의 브랜드 로고나 일반 데이터베이스 아이콘을 대신 만들지 마.
이 텍스트 대체는 로고 전용 카드 규칙의 예외로 표시하고, 이미 사용 가능한 다른 SVG 렌더러를 사용해줘. helper의 자산 검증을 우회하지 마.
확인된 심볼 카드에는 이미지 안의 글자 없이 카드 아래 이름을 유지해줘. 기존 흐름과 연결 방향은 보존해줘.
SVG·가능한 경우 PNG·manifest를 저장하고, 심볼 확인 제한과 텍스트 대체 노드를 결과 설명에 적어줘.
```

### 11. 다른 컴퓨터에서도 열리는 PNG

SVG가 브라우저에 보인다고 PNG 변환까지 성공한 것은 아닙니다. 외부 이미지 링크와 크기 지정도 확인합니다.

```text
$logo-flow-infographics
첨부한 SVG를 다른 컴퓨터에서도 확인할 수 있는 PNG로 내보내고 편집 가능한 SVG도 함께 보존해줘.
노드와 연결, 검증된 로고의 비율·색·모양, 카드 아래 기술 이름은 유지해줘.
승인된 로컬 자산을 SVG에 포함해 외부 파일 경로에 의존하지 않게 하고, viewBox 비율을 유지하면서 이미지 크기를 명시해줘. 출처와 원본 및 변환 자산 해시를 manifest에 남겨줘.
이미 사용 가능한 렌더러로 변환한 뒤 PNG 자체를 열어서 누락된 로고·잘린 이름·화살표 끝을 확인해줘.
PNG 도구가 없으면 설치하지 말고 SVG를 보존한 뒤 PNG를 만들지 못한 이유를 알려줘.
```

### 12. 가로로 긴 로고·세로로 긴 로고

카드 크기는 같게 두되 로고의 종횡비를 보존합니다. 빈 공간을 채우려고 늘이거나 중요한 부분을 자르지 않습니다.

```text
$logo-flow-infographics
첨부한 가로로 긴 독립 심볼과 세로로 긴 독립 심볼을 사용해, 첨부한 흐름대로 같은 크기의 흰 카드에 배치해줘.
각 자산의 viewBox와 원본 비율을 보존하고 카드 안에 맞춰 축소해줘. 늘이기·찌그러뜨리기·잘라내기·로고 다시 그리기는 하지 마.
가로로 긴 파일이 글자를 포함한 전체 워드마크라면 심볼 자산으로 취급하지 말고 제한을 알려줘. 제공한 자산 외에는 다운로드하지 마.
각 카드 아래에 자산 목록의 정확한 기술 이름을 넣고, 긴 이름이 겹치면 캔버스 간격을 넓히거나 이미 사용 가능한 다른 렌더러를 선택해줘. 연결은 바꾸지 마.
SVG·PNG·manifest를 저장하고 전체 보기와 확대 보기에서 비율·여백·이름·화살표를 확인해줘.
```

## 내 로고 파일을 준비하는 방법

공식 브랜드 페이지 또는 프로젝트 공식 저장소에서 **글자와 분리된 심볼**을 선택합니다. 다운로드 URL, 파일 버전이나 커밋, 확인한 사용 조건을 기록하세요. 공식 심볼이 없다면 전체 워드마크의 글자를 지우거나 비슷한 도형을 만들지 않습니다. 사용할 수 있는 자산이 없다는 사실과 대체 방법을 남깁니다.

helper를 직접 쓸 때에는 manifest와 로고 파일을 같은 폴더 아래에 모읍니다. manifest의 `path`는 해당 manifest 위치를 기준으로 해석되며, 그 폴더 밖을 가리킬 수 없습니다. 각 자산에는 다음 값이 필요합니다.

| 필드 | 넣을 내용 |
| --- | --- |
| `name` | 카드 아래에 표시할 정확한 기술 이름. helper에서는 24자 이내입니다. |
| `path` | manifest 폴더 안에 있는 승인한 로컬 SVG의 상대 경로. |
| `sha256` | 실제 로고 파일의 SHA-256 소문자 값. |
| `source` | 공식 파일 URL 또는 제공 자산의 출처·버전·커밋. 공통 계열 심볼 재사용도 기록합니다. |
| `license_note` | 확인한 라이선스·상표 사용 조건과 확인되지 않은 범위. |

PowerShell에서는 작업 폴더의 로고 파일을 대상으로 다음처럼 해시를 확인할 수 있습니다. 아래 `assets/python.svg`는 사용자가 그 위치에 저장한 파일입니다.

```powershell
(Get-FileHash -LiteralPath .\assets\python.svg -Algorithm SHA256).Hash.ToLowerInvariant()
```

다음 명령은 `assets/` 아래 SVG들의 경로와 해시를 한 번에 보여줍니다. 파일을 수정하거나 전송하지 않습니다.

```powershell
Get-ChildItem -LiteralPath .\assets -Filter *.svg -File | ForEach-Object {
    [PSCustomObject]@{
        File = $_.Name
        SHA256 = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    }
}
```

해시가 맞는다는 사실은 파일이 기록과 같다는 뜻입니다. 로고 정체성·사용 허락·실제 시스템의 연결까지 증명하지 않습니다. 자산 파일을 교체했다면 해시를 다시 계산하고 출처 기록도 함께 확인하세요.

## 어떤 렌더러를 선택할까?

기본 Python helper는 로컬 SVG, 짧은 기술 이름, 왼쪽에서 오른쪽으로 진행하는 연결에 적합합니다. 100px 카드 안에 최대 64px 크기로 로고를 맞추고 이름을 아래에 표시합니다. 라벨 공간을 위해 카드 아래에 최소 28px 여백을 확보하세요.

순환·역방향 연결, 매우 긴 이름, 복잡한 교차 경로, 텍스트 대체 카드, PNG·GIF 자산은 이미 사용 가능한 다른 렌더러나 편집기를 선택합니다. 도구 제약 때문에 노드나 화살표를 지우거나 실제 흐름을 바꾸지 않습니다. 필요한 도구가 없으면 편집 가능한 원본을 보존하고 제한을 설명합니다.

## 결과를 받을 때 확인할 것

- 각 심볼 카드에는 검증된 로고 이미지의 심볼만 있고, 카드 바로 아래에 정확한 이름이 있는가?
- 전체 워드마크·가상 도형·다른 제품의 로고를 실제 기술의 심볼처럼 쓰지 않았는가?
- 분기·합류·독립 경로가 요청한 관계와 일치하고, 실제 구현과 제안 상태가 구분되는가?
- SVG와 PNG를 실제로 열었을 때 로고·이름·화살표가 누락되거나 잘리지 않는가?
- manifest에 상태·근거·자산 출처·해시·사용 조건과 확인 제한이 남았는가?

포트폴리오 수정 요청이라면 완성한 그림을 해당 문서에 반영하고 최종 페이지도 다시 확인합니다. 이미지 파일 하나를 내보낸 것만으로 문서 수정이 끝난 것은 아닙니다.
