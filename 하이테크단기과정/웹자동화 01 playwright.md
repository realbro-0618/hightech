# Playwright 웹 자동화 입문

> **대상:** Python을 처음 배우는 학생  
> **수업 방향:** 복잡한 웹 테스트 이론보다, 사람이 웹 브라우저에서 하는 행동을 Python으로 자동화하는 경험에 집중  
> **사용 언어:** Python  
> **사용 방식:** `sync_playwright`  
> **추천 수업 시간:** 약 4시간

---

# 0. 오늘 수업에서 배울 내용

오늘 수업에서는 다음 순서로 Playwright를 배웁니다.

1. **Playwright란 무엇인가?**
2. **Selenium과 무엇이 다른가?**
3. **Playwright 설치하기**
4. **Codegen으로 내가 한 행동을 코드로 기록하기**
5. **Codegen으로 만들어진 코드를 직접 실행해보기**
6. **Playwright의 기본 구조 이해하기**
7. **클릭, 입력, 키보드, 스크린샷 등 주요 기능 사용하기**
8. **웹페이지에서 원하는 요소를 찾는 방법 배우기**
9. **Locator와 Selector 이해하기**
10. **간단한 웹 자동화 프로그램 만들어보기**

---

# 1. 웹 자동화란?

웹 자동화(Web Automation)는 사람이 웹 브라우저에서 직접 하던 행동을 프로그램이 대신 수행하도록 만드는 것입니다.

예를 들어 사람이 네이버에서 검색을 한다면:

```text
Chrome 실행
   ↓
네이버 접속
   ↓
검색창 클릭
   ↓
"Playwright" 입력
   ↓
검색 버튼 클릭
   ↓
검색 결과 확인
```

웹 자동화를 사용하면 이 과정을 Python 프로그램이 대신 수행할 수 있습니다.

예를 들면 다음과 같은 형태입니다.

```python
page.goto("https://www.naver.com")

search = page.get_by_role("textbox")

search.fill("Playwright")

search.press("Enter")
```

> 실제 네이버의 Locator 이름은 사이트 구조가 변경되면 달라질 수 있습니다.  
> 수업에서는 **Codegen이 현재 사이트에서 만들어준 Locator를 사용하는 방법**을 먼저 배웁니다.

---

# 2. Playwright란?

Playwright는 웹 브라우저를 프로그램으로 제어할 수 있게 해주는 자동화 도구입니다.

Playwright를 사용하면 Python 코드로 다음과 같은 일을 할 수 있습니다.

- 웹사이트 접속
- 버튼 클릭
- 입력창에 글자 입력
- Enter 키 누르기
- 체크박스 선택
- 드롭다운 메뉴 선택
- 파일 업로드
- 파일 다운로드
- 새 창이나 새 탭 처리
- 팝업 처리
- 웹페이지의 글자 읽기
- 웹페이지 스크린샷 찍기
- 로그인 상태 저장
- 브라우저 동작 자동화
- 웹서비스 테스트

Playwright는 다음 브라우저 엔진을 지원합니다.

```text
Chromium
Firefox
WebKit
```

우리는 수업에서 주로 Chromium을 사용합니다.

---

# 3. Playwright를 사용하는 이유

Playwright의 장점 중 초보자가 체감하기 좋은 것은 다음과 같습니다.

## 3-1. Python 코드로 브라우저를 직접 조작할 수 있다

```python
page.goto("https://www.naver.com")
```

웹사이트에 접속할 수 있습니다.

```python
page.get_by_text("로그인").click()
```

웹페이지의 요소를 찾아 클릭할 수 있습니다.

---

## 3-2. Codegen 기능이 있다

사람이 브라우저에서 직접 행동하면 Playwright가 그 행동을 코드로 만들어줄 수 있습니다.

예:

```text
내가 검색창 클릭
        ↓
Playwright가 클릭 코드 생성

내가 "Playwright" 입력
        ↓
Playwright가 fill() 코드 생성

내가 검색 버튼 클릭
        ↓
Playwright가 click() 코드 생성
```

코딩을 처음 배우는 학생에게 매우 유용한 기능입니다.

---

## 3-3. Auto-Waiting 기능이 있다

웹사이트는 버튼이나 입력창이 즉시 나타나지 않는 경우가 많습니다.

Playwright는 클릭 등의 작업을 하기 전에 해당 요소가 실제로 클릭 가능한 상태인지 자동으로 확인하고 기다려줍니다.

따라서 단순히:

```python
page.get_by_role("button", name="확인").click()
```

이라고 작성해도 Playwright가 버튼이 사용할 수 있는 상태가 될 때까지 일정 시간 기다려줍니다.

---

# 4. Selenium이란?

Selenium 역시 대표적인 웹 브라우저 자동화 도구입니다.

Playwright가 등장하기 훨씬 전부터 사용되어 왔으며, 현재도 웹 테스트와 자동화 분야에서 널리 사용됩니다.

두 도구 모두 다음 작업을 할 수 있습니다.

```text
브라우저 실행
웹사이트 접속
버튼 클릭
글자 입력
데이터 읽기
자동 로그인
반복 작업 자동화
웹 테스트
```

---

# 5. Selenium과 Playwright의 차이

둘 중 하나가 무조건 좋다고 볼 수는 없습니다.

다만 입문 수업에서는 Playwright가 편리한 부분이 많습니다.

| 구분 | Selenium | Playwright |
|---|---|---|
| 브라우저 자동화 | 가능 | 가능 |
| Python 지원 | O | O |
| 오랜 사용 역사 | 매우 오래됨 | 비교적 최신 |
| Chromium | O | O |
| Firefox | O | O |
| WebKit | 환경에 따라 다름 | 공식 지원 |
| 자동 대기 기능 | 명시적 Wait를 사용하는 경우가 많음 | Auto-Waiting이 강력함 |
| 행동 녹화 | 도구/환경에 따라 사용 | Codegen 기본 제공 |
| 브라우저 세션 분리 | 가능 | BrowserContext 사용이 편리함 |
| 최신 웹 앱 대응 | 가능 | 현대적인 웹 앱 자동화를 고려해 설계 |
| 기존 자료/사례 | 매우 많음 | 빠르게 증가 중 |

> Selenium도 현재는 Selenium Manager 등 설치 편의 기능이 발전했습니다.  
> 따라서 단순히 "Selenium은 불편하고 Playwright는 편하다"라고 이해하면 안 됩니다.

이번 수업에서는 다음 이유로 Playwright를 사용합니다.

```text
Codegen을 사용하기 쉽다.
        +
Locator 문법이 읽기 쉽다.
        +
Auto-Waiting을 제공한다.
        +
초보자가 결과를 빠르게 확인하기 좋다.
```

---

# 6. Playwright 설치하기

VS Code의 터미널을 엽니다.

---

## 6-1. Playwright 설치

먼저 다음 명령을 입력합니다.

```bash
pip install playwright
```

정상적으로 설치되면 다음 단계로 넘어갑니다.

---

## 6-2. Playwright가 사용할 브라우저 설치

다음 명령을 입력합니다.

```bash
playwright install
```

Playwright에서 사용하는 브라우저가 설치됩니다.

---

## 6-3. `playwright install`이 안 된다면?

환경에 따라 `playwright` 명령을 찾지 못하는 경우가 있습니다.

그럴 때는 다음 명령을 사용합니다.

```bash
python -m playwright install
```

즉 다음 순서로 시도하면 됩니다.

```text
1차 시도

pip install playwright
playwright install
```

안 된다면:

```text
2차 시도

pip install playwright
python -m playwright install
```

---

## 6-4. `pip` 명령 자체가 안 된다면?

다음 명령을 사용할 수 있습니다.

```bash
python -m pip install playwright
```

따라서 설치 문제 발생 시 다음 명령들을 기억하면 됩니다.

```bash
pip install playwright
```

```bash
python -m pip install playwright
```

```bash
playwright install
```

```bash
python -m playwright install
```

---

# 7. 설치 확인하기

터미널에서 다음 명령을 입력해봅니다.

```bash
playwright --help
```

또는:

```bash
python -m playwright --help
```

도움말이 표시되면 Playwright 명령을 사용할 수 있는 상태입니다.

---

# 8. Codegen부터 사용해보기

코드를 직접 작성하기 전에 Playwright의 Codegen 기능부터 사용해봅니다.

Codegen은:

> **내가 브라우저에서 한 행동을 Playwright 코드로 기록해주는 기능**

입니다.

---

# 9. Codegen 실행하기

터미널에서 다음 명령을 실행합니다.

```bash
playwright codegen https://www.naver.com
```

명령어가 동작하지 않는 환경이라면 다음처럼 시도할 수 있습니다.

```bash
python -m playwright codegen https://www.naver.com
```

실행하면 보통 다음 두 개의 창을 확인할 수 있습니다.

```text
1. 실제 브라우저 창

2. Playwright Inspector
```

---

# 10. Codegen 첫 번째 실습 - 네이버 검색

Codegen으로 열린 브라우저에서 직접 다음 행동을 해봅니다.

```text
1. 네이버 접속

2. 검색창 클릭

3. Playwright 입력

4. 검색 실행

5. 검색 결과 페이지 확인
```

오른쪽 Playwright Inspector를 확인하면 내가 한 행동이 코드로 기록됩니다.

대략적으로 다음과 같은 종류의 코드가 생성됩니다.

```python
page.goto("https://www.naver.com/")

page.get_by_role("textbox").fill("Playwright")

page.get_by_role("textbox").press("Enter")
```

> **주의:** 위 코드는 개념 설명용 예시입니다.  
> 네이버 사이트의 HTML 구조가 변경되면 실제 Codegen에서 만들어지는 코드는 다를 수 있습니다.  
> 수업에서는 **자신의 컴퓨터에서 Codegen이 생성해준 코드를 그대로 사용**합니다.

---

# 11. Codegen을 사용하면 좋은 이유

초보자가 웹 자동화를 처음 만들 때 가장 어려운 문제는 다음입니다.

> "화면에 보이는 이 검색창을 코드에서는 어떻게 찾아야 하지?"

Codegen을 사용하면 Playwright가 해당 요소를 분석하여 Locator를 만들어줍니다.

예를 들어 내가 로그인 버튼을 클릭했다면:

```python
page.get_by_role(
    "button",
    name="로그인"
).click()
```

같은 코드를 만들어줄 수 있습니다.

따라서 처음에는:

```text
Codegen으로 행동 기록
        ↓
생성된 코드 확인
        ↓
코드를 복사
        ↓
직접 실행
        ↓
코드를 조금씩 수정
```

순서로 연습하면 좋습니다.

---

# 12. Codegen으로 생성한 코드 실행하기

Codegen에서 만들어진 코드를 복사합니다.

VS Code에서 예를 들어 다음 파일을 만듭니다.

```text
naver_test.py
```

복사한 Python 코드를 붙여넣습니다.

그리고 실행합니다.

```bash
python naver_test.py
```

내가 직접 브라우저에서 했던 행동을 Python이 그대로 다시 수행하면 성공입니다.

---

# 13. Codegen 실습 - 네이버 로그인 페이지

이번에는 익숙한 로그인 화면을 이용해봅니다.

Codegen을 실행합니다.

```bash
playwright codegen https://nid.naver.com/nidlogin.login
```

그리고 다음 행동을 기록해봅니다.

```text
1. 아이디 입력창 클릭
2. 연습용 문자열 입력
3. 비밀번호 입력창 클릭
4. 연습용 문자열 입력
5. 로그인 버튼까지 마우스로 이동
```

### 중요한 주의사항

수업에서는 실제 개인 비밀번호를 입력하지 않는 것을 추천합니다.

Codegen에 의해 다음처럼 값이 코드에 그대로 기록될 수 있기 때문입니다.

```python
page.get_by_label("비밀번호").fill("실제비밀번호")
```

이 파일을 GitHub 등에 올리면 비밀번호가 노출될 수 있습니다.

따라서 수업에서는:

```text
test_id
1234
```

같은 가짜 문자열을 사용하여 **입력 과정만 연습**합니다.

또한 실제 로그인 서비스에서는 CAPTCHA, 2단계 인증, 비정상 로그인 탐지 등이 발생할 수 있습니다.

---

# 14. Codegen 실습 - 블로그 글쓰기 생각해보기

사람이 블로그 글을 작성한다고 생각해봅시다.

작업 순서:

```text
로그인
  ↓
블로그 이동
  ↓
글쓰기 버튼 클릭
  ↓
제목 입력
  ↓
본문 입력
  ↓
사진 첨부
  ↓
발행 버튼 클릭
```

이 작업 역시 각각 Playwright 행동으로 나눌 수 있습니다.

```text
접속        → goto()

버튼 클릭   → click()

제목 입력   → fill()

본문 입력   → fill() 또는 키보드 입력

사진 첨부   → set_input_files()

발행 클릭   → click()
```

다만 네이버 블로그처럼 복잡한 웹 에디터는 다음 요소가 포함될 수 있습니다.

- iframe
- contenteditable
- 동적으로 생성되는 HTML
- 여러 개의 동일한 버튼
- 팝업
- 새 창
- 로그인 인증

따라서 처음부터 직접 Selector를 만들기보다 Codegen으로 동작을 기록하고 코드를 분석하는 방법이 좋습니다.

---

# 15. Playwright Python 기본 구조

Codegen을 사용해봤다면 이제 Playwright 코드의 기본 구조를 이해해봅니다.

```python
from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto(
        "https://www.naver.com"
    )

    input("종료하려면 Enter")

    browser.close()
```

---

# 16. 한 줄씩 이해하기

## Playwright 가져오기

```python
from playwright.sync_api import sync_playwright
```

Python에서 Playwright 기능을 사용하겠다는 의미입니다.

---

## Playwright 실행

```python
with sync_playwright() as p:
```

Playwright를 시작합니다.

---

## 브라우저 실행

```python
browser = p.chromium.launch(
    headless=False
)
```

Chromium 브라우저를 실행합니다.

`headless=False`는 브라우저 화면을 보여달라는 의미입니다.

---

## 새 페이지 만들기

```python
page = browser.new_page()
```

새로운 브라우저 탭을 만든다고 생각하면 됩니다.

---

## 웹사이트 이동

```python
page.goto(
    "https://www.naver.com"
)
```

주소창에 URL을 입력하여 웹사이트로 이동하는 것과 비슷합니다.

---

## 브라우저 종료

```python
browser.close()
```

브라우저를 종료합니다.

---

# 17. Browser / Context / Page

Playwright의 구조를 조금 더 정확하게 보면 다음과 같습니다.

```text
Playwright
    ↓
Browser
    ↓
BrowserContext
    ↓
Page
```

---

## Browser

브라우저 프로그램입니다.

```python
browser = p.chromium.launch(
    headless=False
)
```

---

## BrowserContext

독립된 브라우저 사용 환경이라고 생각하면 됩니다.

```python
context = browser.new_context()
```

서로 다른 Context는 쿠키나 로그인 상태 등을 분리해서 사용할 수 있습니다.

쉽게 생각하면:

```text
브라우저 안의 독립된 사용자 공간
```

입니다.

---

## Page

브라우저의 하나의 탭입니다.

```python
page = context.new_page()
```

전체 구조:

```python
from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    context = browser.new_context()

    page = context.new_page()

    page.goto(
        "https://www.naver.com"
    )

    input()

    browser.close()
```

---

# 18. 주요 기능 1 - 웹사이트 이동

```python
page.goto(
    "https://www.naver.com"
)
```

현재 URL 확인:

```python
print(page.url)
```

페이지 제목 확인:

```python
print(page.title())
```

---

# 19. 주요 기능 2 - 클릭

```python
page.get_by_text(
    "로그인"
).click()
```

핵심은:

```text
요소를 먼저 찾고
        ↓
click()
```

입니다.

---

# 20. 주요 기능 3 - 글자 입력

```python
search = page.get_by_role("textbox")

search.fill("Playwright")
```

`fill()`은 입력창에 값을 넣습니다.

기존 값이 있다면 보통 기존 내용을 지우고 새 값을 입력합니다.

---

# 21. 주요 기능 4 - 키보드 입력

Enter:

```python
search.press("Enter")
```

Tab:

```python
search.press("Tab")
```

Escape:

```python
search.press("Escape")
```

단축키도 사용할 수 있습니다.

```python
page.keyboard.press("Control+A")
```

---

# 22. 주요 기능 5 - 천천히 실행하기

자동화가 너무 빨라서 학생이 무슨 일이 일어나는지 보기 어려울 수 있습니다.

브라우저 실행 시 `slow_mo`를 사용할 수 있습니다.

```python
browser = p.chromium.launch(
    headless=False,
    slow_mo=1000
)
```

`1000`은 동작 사이에 약 1000ms 정도 느리게 실행하도록 하는 값입니다.

수업 시연에서 매우 유용합니다.

---

# 23. 주요 기능 6 - 스크린샷

현재 화면 저장:

```python
page.screenshot(
    path="naver.png"
)
```

전체 웹페이지 저장:

```python
page.screenshot(
    path="naver_full.png",
    full_page=True
)
```

---

# 24. 주요 기능 7 - 글자 가져오기

화면의 텍스트를 Python으로 가져올 수 있습니다.

```python
text = page.get_by_text(
    "어떤 글자"
).text_content()

print(text)
```

자동화에서는:

```text
웹페이지에서 정보 읽기
        ↓
Python 변수에 저장
        ↓
조건문이나 반복문에서 사용
```

하는 식으로 활용합니다.

---

# 25. 주요 기능 8 - 보이는지 확인

```python
login = page.get_by_text("로그인")

if login.is_visible():

    print("로그인 버튼이 있습니다.")
```

`if`문과 결합하면 자동화가 훨씬 강력해집니다.

---

# 26. 주요 기능 9 - 체크박스

HTML:

```html
<input type="checkbox" id="agree">
```

체크:

```python
page.locator("#agree").check()
```

체크 해제:

```python
page.locator("#agree").uncheck()
```

---

# 27. 주요 기능 10 - 드롭다운 선택

HTML:

```html
<select id="city">

    <option value="seoul">서울</option>

    <option value="chuncheon">춘천</option>

</select>
```

Playwright:

```python
page.locator("#city").select_option(
    "chuncheon"
)
```

---

# 28. 주요 기능 11 - 마우스 올리기

```python
page.get_by_text(
    "메뉴"
).hover()
```

마우스를 올렸을 때 서브메뉴가 나타나는 사이트에 사용할 수 있습니다.

---

# 29. 주요 기능 12 - 파일 업로드

웹페이지:

```html
<input type="file" id="upload">
```

Playwright:

```python
page.locator(
    "#upload"
).set_input_files(
    "photo.jpg"
)
```

예를 들어 블로그에 사진을 첨부하는 자동화를 만들 때 활용할 수 있습니다.

---

# 30. 주요 기능 13 - 뒤로가기 / 새로고침

뒤로가기:

```python
page.go_back()
```

새로고침:

```python
page.reload()
```

---

# 31. 주요 기능 14 - 여러 요소 반복하기

웹페이지에 같은 종류의 항목이 여러 개 있다고 생각해봅시다.

```html
<div class="item">사과</div>
<div class="item">바나나</div>
<div class="item">수박</div>
```

Playwright:

```python
items = page.locator(".item")
```

몇 개인지 확인:

```python
print(items.count())
```

하나씩 출력:

```python
for i in range(items.count()):

    item = items.nth(i)

    print(
        item.text_content()
    )
```

결과:

```text
사과
바나나
수박
```

---

# 32. 웹 자동화에서 가장 중요한 것 - 요소 찾기

Playwright 명령 자체는 어렵지 않습니다.

```python
.click()
.fill()
.press()
```

진짜 어려운 것은:

> **"내가 클릭하고 싶은 버튼을 Playwright에게 어떻게 알려줄 것인가?"**

입니다.

그래서 웹 자동화에서 가장 중요한 개념 중 하나가 **Locator**입니다.

---

# 33. Locator란?

Locator는 웹페이지에서 원하는 HTML 요소를 찾는 방법입니다.

예를 들어 화면에 다음 버튼이 있다고 생각해봅시다.

```html
<button>로그인</button>
```

Playwright:

```python
login_button = page.get_by_role(
    "button",
    name="로그인"
)
```

여기서 `login_button`은 실제 버튼 그 자체라기보다:

> **"이 조건에 맞는 요소를 찾아라"**

라는 정보를 가진 Locator라고 생각하면 됩니다.

이후:

```python
login_button.click()
```

하면 Playwright가 현재 페이지에서 조건에 맞는 버튼을 찾아 클릭합니다.

---

# 34. Locator와 Selector의 차이

초보자가 가장 많이 헷갈리는 개념입니다.

## Locator

Playwright에서 요소를 찾고 조작하기 위한 객체입니다.

예:

```python
button = page.get_by_role(
    "button",
    name="로그인"
)
```

또는:

```python
button = page.locator(
    "#login"
)
```

둘 다 결과는 Locator입니다.

---

## Selector

웹페이지에서 어떤 요소를 찾을지 표현하는 **검색 규칙**입니다.

예:

```text
#login
```

```text
.login-button
```

```text
input[name="id"]
```

```text
//button
```

이런 문자열을 Selector라고 생각하면 됩니다.

Selector는 보통:

```python
page.locator(
    "SELECTOR"
)
```

안에서 사용합니다.

예:

```python
page.locator(
    "#login"
)
```

---

# 35. 웹 요소를 찾기 위해 HTML 조금 이해하기

다음 HTML을 봅시다.

```html
<input
    id="user-id"
    class="login-input"
    name="id"
    placeholder="아이디"
>
```

하나의 입력창에도 여러 정보가 있습니다.

```text
태그        input

id          user-id

class       login-input

name        id

placeholder 아이디
```

Playwright는 이 정보들을 이용해서 요소를 찾을 수 있습니다.

---

# 36. 방법 1 - get_by_role()

Playwright에서 가장 권장되는 Locator 중 하나입니다.

HTML:

```html
<button>로그인</button>
```

Playwright:

```python
page.get_by_role(
    "button",
    name="로그인"
).click()
```

링크:

```html
<a href="/write">글쓰기</a>
```

```python
page.get_by_role(
    "link",
    name="글쓰기"
).click()
```

장점:

```text
사람이 화면을 이해하는 방식과 비슷하다.
코드가 읽기 쉽다.
HTML 구조가 조금 바뀌어도 비교적 유지하기 좋다.
```

---

# 37. 방법 2 - get_by_text()

화면에 보이는 글자로 찾습니다.

```python
page.get_by_text(
    "로그인"
)
```

클릭:

```python
page.get_by_text(
    "로그인"
).click()
```

화면에 동일한 글자가 여러 개 있다면 문제가 생길 수 있습니다.

예:

```text
로그인
로그인
로그인
```

이런 경우 다른 Locator를 사용하거나 범위를 좁혀야 합니다.

---

# 38. 방법 3 - get_by_label()

HTML:

```html
<label for="user-id">아이디</label>

<input id="user-id">
```

Playwright:

```python
page.get_by_label(
    "아이디"
).fill(
    "student01"
)
```

로그인이나 회원가입 Form에서 매우 유용합니다.

---

# 39. 방법 4 - get_by_placeholder()

HTML:

```html
<input
    placeholder="아이디를 입력하세요"
>
```

Playwright:

```python
page.get_by_placeholder(
    "아이디를 입력하세요"
).fill(
    "student01"
)
```

입력창을 찾을 때 이해하기 쉽습니다.

---

# 40. 방법 5 - get_by_alt_text()

이미지:

```html
<img
    src="logo.png"
    alt="네이버 로고"
>
```

Playwright:

```python
page.get_by_alt_text(
    "네이버 로고"
)
```

---

# 41. 방법 6 - get_by_title()

HTML:

```html
<button title="새로고침">
    ↻
</button>
```

Playwright:

```python
page.get_by_title(
    "새로고침"
).click()
```

---

# 42. 방법 7 - get_by_test_id()

개발자가 HTML에 테스트용 ID를 만들어놓은 경우입니다.

HTML:

```html
<button data-testid="login-button">
    로그인
</button>
```

Playwright:

```python
page.get_by_test_id(
    "login-button"
).click()
```

직접 만든 웹서비스를 테스트할 때 매우 안정적인 방법입니다.

---

# 43. 방법 8 - CSS Selector

`page.locator()`를 사용하여 CSS Selector로 요소를 찾을 수 있습니다.

---

## id로 찾기

HTML:

```html
<button id="login">
    로그인
</button>
```

Playwright:

```python
page.locator(
    "#login"
).click()
```

기억:

```text
# = id
```

---

# 44. class로 찾기

HTML:

```html
<button class="login-button">
    로그인
</button>
```

Playwright:

```python
page.locator(
    ".login-button"
).click()
```

기억:

```text
. = class
```

---

# 45. 태그로 찾기

HTML:

```html
button
```

Playwright:

```python
page.locator(
    "button"
)
```

하지만 화면에 버튼이 여러 개 있을 가능성이 높아서 단독 사용은 주의해야 합니다.

---

# 46. 속성으로 찾기

HTML:

```html
<input
    name="id"
>
```

Playwright:

```python
page.locator(
    'input[name="id"]'
)
```

placeholder를 이용할 수도 있습니다.

```python
page.locator(
    'input[placeholder="아이디"]'
)
```

---

# 47. 여러 조건 결합하기

예:

```html
<input
    class="login-input"
    name="id"
>
```

Playwright:

```python
page.locator(
    'input.login-input[name="id"]'
)
```

조건을 구체적으로 만들수록 원하는 요소 하나를 정확하게 찾을 수 있습니다.

하지만 너무 복잡하게 만들면 웹사이트가 조금만 변경되어도 코드가 깨질 수 있습니다.

---

# 48. XPath

Playwright는 XPath도 사용할 수 있습니다.

예:

```python
page.locator(
    "//button"
)
```

텍스트 조건:

```python
page.locator(
    '//button[text()="로그인"]'
)
```

하지만 초보 단계에서는 XPath를 가장 먼저 사용하는 것을 추천하지 않습니다.

특히 다음처럼 너무 긴 XPath는 좋지 않습니다.

```python
page.locator(
    '//*[@id="wrap"]/div[2]/div[3]/div/div[1]/button'
)
```

HTML 구조가 조금만 바뀌어도 동작하지 않을 가능성이 높습니다.

---

# 49. Locator 추천 순서

처음에는 다음 순서로 생각하면 좋습니다.

```text
1. get_by_role()

2. get_by_label()

3. get_by_placeholder()

4. get_by_text()

5. get_by_test_id()

6. 짧고 명확한 CSS Selector

7. XPath
```

무조건 이 순서가 정답은 아니지만 초보자가 안정적인 자동화 코드를 만들기 좋은 방향입니다.

---

# 50. Codegen이 Locator를 찾는 데 도움이 되는 이유

Codegen에서 브라우저의 어떤 버튼을 클릭하면 Playwright가 해당 요소를 분석합니다.

예를 들어:

```python
page.get_by_role(
    "button",
    name="로그인"
).click()
```

같이 만들어줍니다.

따라서:

```text
Codegen 사용
   ↓
생성된 Locator 확인
   ↓
왜 get_by_role()을 사용했는지 분석
   ↓
직접 Locator 수정
```

순서로 학습하면 Locator를 훨씬 쉽게 이해할 수 있습니다.

---

# 51. 동일한 요소가 여러 개 검색되는 경우

예:

```python
page.get_by_text(
    "확인"
).click()
```

그런데 화면에 `확인`이 3개 있다면 Playwright가 정확히 하나를 선택하지 못할 수 있습니다.

이때는 Locator를 더 구체적으로 만듭니다.

예:

```python
page.get_by_role(
    "button",
    name="확인"
).click()
```

그래도 여러 개라면 범위를 좁힐 수 있습니다.

```python
buttons = page.get_by_role(
    "button",
    name="확인"
)

print(buttons.count())
```

특정 번째 요소:

```python
buttons.nth(0).click()
```

하지만 가능하면 `nth()`에 의존하기보다 의미 있는 Locator를 만드는 것이 좋습니다.

---

# 52. Locator 안에서 다시 찾기

HTML:

```html
<div class="login-box">

    <button>확인</button>

</div>

<div class="popup">

    <button>확인</button>

</div>
```

전체 페이지에서 `확인`을 찾으면 2개입니다.

먼저 로그인 영역을 찾습니다.

```python
login_box = page.locator(
    ".login-box"
)
```

그 안에서 버튼을 찾습니다.

```python
login_box.get_by_role(
    "button",
    name="확인"
).click()
```

이렇게 검색 범위를 좁힐 수 있습니다.

---

# 53. filter() 사용하기

상품 목록처럼 비슷한 HTML이 여러 개 있을 때 유용합니다.

예:

```python
product = page.get_by_role(
    "listitem"
).filter(
    has_text="노트북"
)
```

그 안에서 버튼을 찾습니다.

```python
product.get_by_role(
    "button",
    name="구매"
).click()
```

---

# 54. 개발자 도구(F12)로 요소 확인하기

Codegen만 사용하는 것이 아니라 브라우저 개발자 도구를 사용해서 직접 HTML을 확인할 수도 있습니다.

Chrome에서:

```text
F12
```

또는:

```text
마우스 오른쪽 클릭
        ↓
검사
```

를 선택합니다.

Elements 화면에서 HTML을 확인합니다.

예:

```html
<input
    id="user-id"
    class="login-input"
    placeholder="아이디"
>
```

이 정보를 보고:

```python
page.locator("#user-id")
```

또는:

```python
page.get_by_placeholder("아이디")
```

같은 Locator를 만들 수 있습니다.

---

# 55. Auto-Waiting 다시 이해하기

Playwright는 클릭할 요소가 준비될 때까지 자동으로 확인합니다.

예:

```python
page.get_by_role(
    "button",
    name="로그인"
).click()
```

Playwright는 단순히 HTML에 버튼이 존재하는지만 보는 것이 아니라 클릭 작업을 하기 전에 필요한 상태들을 확인합니다.

따라서 초보자가 다음처럼 무조건 기다리는 코드를 많이 넣을 필요가 줄어듭니다.

```python
import time

time.sleep(5)
```

---

# 56. 특정 요소를 기다리기

필요한 경우 직접 기다릴 수도 있습니다.

```python
button = page.get_by_role(
    "button",
    name="확인"
)

button.wait_for(
    state="visible"
)

button.click()
```

사용 가능한 상태:

```text
visible
hidden
attached
detached
```

---

# 57. 새 창 / 새 탭 처리

어떤 버튼을 클릭했을 때 새 탭이 열릴 수 있습니다.

기본 개념:

```text
Page 1
네이버

Page 2
새로운 사이트
```

Playwright는 여러 Page를 관리할 수 있습니다.

예:

```python
with page.expect_popup() as popup_info:

    page.get_by_text(
        "새 창 열기"
    ).click()

new_page = popup_info.value

print(new_page.url)
```

---

# 58. 팝업(Dialog) 처리

JavaScript의 `alert()` 같은 팝업이 나타날 수 있습니다.

예:

```python
page.once(
    "dialog",
    lambda dialog: dialog.accept()
)
```

그 다음 팝업을 발생시키는 버튼을 클릭합니다.

```python
page.get_by_text(
    "삭제"
).click()
```

---

# 59. iframe

일부 웹사이트의 특정 영역은 iframe 안에 들어 있습니다.

HTML 개념:

```html
<iframe>
    내부 웹페이지
</iframe>
```

이 경우 일반 Page에서 바로 찾지 못할 수 있습니다.

예:

```python
frame = page.frame_locator(
    "iframe"
)
```

iframe 안의 버튼:

```python
frame.get_by_role(
    "button",
    name="확인"
).click()
```

블로그 에디터, 결제창, 외부 위젯 등에서 iframe을 만날 수 있습니다.

---

# 60. 자동화 프로그램을 만드는 사고방식

웹 자동화 코드를 바로 작성하지 말고 사람이 하는 행동부터 정리합니다.

예를 들어 블로그 글쓰기:

```text
1. 사이트 접속

2. 로그인 여부 확인

3. 블로그 메뉴 이동

4. 글쓰기 버튼 찾기

5. 글쓰기 버튼 클릭

6. 제목 입력창 찾기

7. 제목 입력

8. 본문 입력 영역 찾기

9. 본문 입력

10. 사진 추가

11. 발행 버튼 찾기

12. 발행
```

그 다음 각 작업을 Playwright 기능으로 변경합니다.

```text
사이트 접속
→ goto()

화면 확인
→ is_visible()

버튼 찾기
→ Locator

버튼 클릭
→ click()

입력
→ fill()

사진 첨부
→ set_input_files()
```

---

# 61. 자동화와 조건문

Python의 `if`문과 연결합니다.

예:

```python
login_button = page.get_by_text(
    "로그인"
)

if login_button.is_visible():

    print(
        "현재 로그인되어 있지 않습니다."
    )
```

자동화 프로그램은 단순히 정해진 순서만 실행하는 것이 아니라 화면의 상태를 확인하고 행동을 바꾸게 할 수 있습니다.

---

# 62. 자동화와 반복문

여러 항목을 반복해서 처리할 수도 있습니다.

```python
items = page.locator(
    ".item"
)

for i in range(
    items.count()
):

    item = items.nth(i)

    print(
        item.text_content()
    )
```

즉 Playwright를 배우면서 Python의:

```text
변수
함수
조건문
반복문
```

을 실제 프로그램에 적용할 수 있습니다.

---

# 63. 첫 번째 종합 예제 - 네이버 검색 자동화

아래 예제의 Locator는 개념 설명용입니다.

실제 수업에서는 Codegen이 생성한 Locator로 교체합니다.

```python
from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    page = browser.new_page()

    # 네이버 접속
    page.goto(
        "https://www.naver.com"
    )

    # 검색창 찾기
    search = page.get_by_role(
        "textbox"
    )

    # 검색어 입력
    search.fill(
        "Playwright"
    )

    # Enter
    search.press(
        "Enter"
    )

    # 현재 URL 확인
    print(
        page.url
    )

    # 스크린샷
    page.screenshot(
        path="search_result.png"
    )

    input(
        "종료하려면 Enter"
    )

    browser.close()
```

### 수업 포인트

이 코드에는 지금까지 배운 내용이 들어 있습니다.

```text
브라우저 실행
goto()
Locator
fill()
press()
URL 확인
screenshot()
```

---

# 64. 두 번째 종합 예제 - 로그인 자동화 구조

실제 특정 사이트에 종속되지 않은 로그인 자동화의 기본 구조입니다.

```python
from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto(
        "로그인 페이지 주소"
    )

    page.get_by_label(
        "아이디"
    ).fill(
        "student01"
    )

    page.get_by_label(
        "비밀번호"
    ).fill(
        "1234"
    )

    page.get_by_role(
        "button",
        name="로그인"
    ).click()

    input()

    browser.close()
```

실제 네이버 등의 사이트에서는 Codegen을 사용하여 현재 HTML 구조에 맞는 Locator로 바꾸면 됩니다.

---

# 65. 세 번째 종합 예제 - 글쓰기 자동화의 구조

```python
page.goto(
    "글쓰기 페이지 주소"
)

page.get_by_placeholder(
    "제목"
).fill(
    "Playwright 자동화 테스트"
)

page.get_by_placeholder(
    "내용"
).fill(
    "Playwright를 이용해서 자동으로 작성한 글입니다."
)

page.get_by_role(
    "button",
    name="발행"
).click()
```

실제 네이버 블로그는 에디터 구조가 더 복잡할 수 있기 때문에 위 코드는 **자동화 흐름을 이해하기 위한 예제**입니다.

실제 작업에서는:

```text
Codegen
+
F12 개발자 도구
+
Locator 분석
```

을 함께 사용합니다.

---

# 66. 처음 자동화를 만들 때 추천 순서

학생들은 다음 순서를 기억하면 됩니다.

```text
1. 사람이 직접 사이트를 사용해본다.

        ↓

2. 행동 순서를 적는다.

        ↓

3. Codegen으로 행동을 기록한다.

        ↓

4. 만들어진 코드를 실행해본다.

        ↓

5. 생성된 Locator를 분석한다.

        ↓

6. 불필요한 코드를 정리한다.

        ↓

7. 조건문과 반복문을 추가한다.

        ↓

8. 자동화 프로그램으로 완성한다.
```

---

# 67. 자주 발생하는 오류

## 67-1. 요소를 찾지 못함

예:

```text
TimeoutError
```

가능한 원인:

```text
Locator가 잘못됨

요소가 아직 화면에 없음

iframe 안에 있음

새로운 탭에 있음

사이트 HTML이 변경됨
```

---

## 67-2. 같은 요소가 여러 개 있음

예:

```python
page.get_by_text(
    "확인"
)
```

화면에 `확인`이 여러 개 있는 경우입니다.

해결:

```text
get_by_role() 사용

부모 요소부터 찾기

filter() 사용

CSS Selector를 더 구체적으로 작성
```

---

## 67-3. 자동화가 너무 빠름

수업 중에는:

```python
browser = p.chromium.launch(
    headless=False,
    slow_mo=1000
)
```

을 사용하면 동작을 쉽게 관찰할 수 있습니다.

---

## 67-4. 사이트가 변경됨

웹 자동화의 중요한 특징입니다.

```text
오늘 잘 되던 코드가

사이트 HTML 변경 후

동작하지 않을 수도 있다.
```

그래서 너무 긴 CSS Selector나 XPath보다 의미 기반 Locator를 우선적으로 사용하는 것이 좋습니다.

---

# 68. 웹 자동화 시 주의할 점

Playwright로 기술적으로 할 수 있다고 해서 모든 자동화가 허용되는 것은 아닙니다.

사이트에 따라:

- 이용약관
- 자동화 정책
- 로그인 보안
- 개인정보
- CAPTCHA
- 2단계 인증
- 요청 횟수 제한

등이 있을 수 있습니다.

따라서 실제 서비스 자동화 전에 해당 서비스의 정책을 확인해야 합니다.

또한 다음 정보는 코드에 직접 넣지 않는 것이 좋습니다.

```text
실제 비밀번호
API KEY
개인정보
인증 토큰
```

---

# 69. 오늘 배운 주요 기능 요약

| 하고 싶은 일 | Playwright |
|---|---|
| 웹사이트 접속 | `page.goto()` |
| 현재 주소 | `page.url` |
| 페이지 제목 | `page.title()` |
| 버튼 클릭 | `.click()` |
| 값 입력 | `.fill()` |
| 키 입력 | `.press()` |
| 텍스트 읽기 | `.text_content()` |
| 보이는지 확인 | `.is_visible()` |
| 체크박스 | `.check()` |
| 체크 해제 | `.uncheck()` |
| 메뉴 선택 | `.select_option()` |
| 마우스 올리기 | `.hover()` |
| 파일 업로드 | `.set_input_files()` |
| 스크린샷 | `page.screenshot()` |
| 뒤로가기 | `page.go_back()` |
| 새로고침 | `page.reload()` |
| 기다리기 | `.wait_for()` |
| 행동 기록 | `playwright codegen` |

---

# 70. Locator 요약

| 찾는 방법 | 예제 |
|---|---|
| 역할 | `get_by_role()` |
| 화면 글자 | `get_by_text()` |
| Label | `get_by_label()` |
| Placeholder | `get_by_placeholder()` |
| 이미지 alt | `get_by_alt_text()` |
| title 속성 | `get_by_title()` |
| test id | `get_by_test_id()` |
| CSS Selector | `locator()` |
| XPath | `locator("//...")` |

---

# 71. CSS Selector 핵심 요약

HTML:

```html
<input
    id="user-id"
    class="login-input"
    name="id"
>
```

## id

```python
page.locator(
    "#user-id"
)
```

## class

```python
page.locator(
    ".login-input"
)
```

## 태그

```python
page.locator(
    "input"
)
```

## 속성

```python
page.locator(
    'input[name="id"]'
)
```

기억:

```text
# = id

. = class

[ ] = 속성
```

---

# 72. 수업 실습 과제

## 실습 1

Codegen을 이용하여 네이버에 접속합니다.

```bash
playwright codegen https://www.naver.com
```

검색창에:

```text
Playwright
```

를 입력하고 검색합니다.

Codegen에서 만들어진 코드를 확인합니다.

---

## 실습 2

Codegen에서 만들어진 코드를 Python 파일로 저장하고 실행합니다.

```bash
python naver_search.py
```

내가 직접 했던 행동이 자동으로 반복되는지 확인합니다.

---

## 실습 3

검색어를 다른 값으로 변경합니다.

예:

```text
Python
```

```text
AI
```

```text
춘천 맛집
```

---

## 실습 4

검색 결과 화면을 자동으로 스크린샷 저장합니다.

```python
page.screenshot(
    path="result.png"
)
```

---

## 실습 5

현재 URL과 페이지 제목을 출력합니다.

```python
print(
    page.url
)

print(
    page.title()
)
```

---

## 실습 6

Codegen으로 네이버 로그인 화면의 입력창과 로그인 버튼이 어떤 Locator로 만들어지는지 확인합니다.

> 실제 비밀번호를 입력하지 않습니다.

---

## 실습 7

F12 개발자 도구를 이용하여 웹페이지의:

```text
id

class

placeholder

name
```

을 하나씩 찾아봅니다.

그리고 직접 `page.locator()` 코드를 만들어봅니다.

---

# 73. 4시간 강의 구성 추천

## 1교시 - Playwright 소개와 설치

```text
웹 자동화란?

Playwright란?

Selenium과 차이

설치

Playwright 실행 확인
```

### 목표

> Playwright가 무엇인지 이해하고 실행 환경을 만든다.

---

## 2교시 - Codegen 체험

```text
Codegen 실행

네이버 검색 자동화

사용자 행동 기록

생성된 코드 확인

생성 코드 복사

Python으로 다시 실행
```

### 목표

> "내 행동이 Python 코드가 된다"는 것을 직접 경험한다.

---

## 3교시 - Playwright 주요 기능

```text
goto()

click()

fill()

press()

text_content()

is_visible()

screenshot()

check()

select_option()

hover()

set_input_files()
```

### 목표

> Codegen 없이도 기본적인 브라우저 행동을 코드로 이해한다.

---

## 4교시 - Locator와 Selector

```text
HTML 요소 구조

Locator란?

get_by_role()

get_by_text()

get_by_label()

get_by_placeholder()

CSS Selector

id

class

속성

XPath

F12 개발자 도구

Codegen으로 Locator 찾기
```

### 목표

> 원하는 웹 요소를 직접 찾고 조작할 수 있다.

---

# 74. 오늘 수업의 핵심

Playwright 자동화는 결국 다음 과정입니다.

```text
웹사이트 접속

        ↓

원하는 요소 찾기

        ↓

행동하기

        ↓

결과 확인

        ↓

조건에 따라 다음 행동
```

코드로 보면:

```text
goto()

   ↓

Locator

   ↓

click()
fill()
press()

   ↓

is_visible()
text_content()
```

입니다.

---

# 75. 가장 먼저 기억해야 하는 6가지

## 사이트 이동

```python
page.goto()
```

## 요소 찾기

```python
page.get_by_role()
```

## 클릭

```python
.click()
```

## 입력

```python
.fill()
```

## 화면 상태 확인

```python
.is_visible()
```

## 막히면 Codegen

```bash
playwright codegen
```

---

# 76. 마무리

Playwright를 처음 배울 때 모든 Locator와 명령어를 외울 필요는 없습니다.

처음에는 다음 순서만 기억하면 됩니다.

```text
직접 해본다.
    ↓
Codegen으로 기록한다.
    ↓
코드를 실행한다.
    ↓
Locator를 이해한다.
    ↓
코드를 수정한다.
    ↓
조건문과 반복문을 넣는다.
```

처음에는 Codegen이 만든 코드를 따라하면서 시작하고, 익숙해진 뒤 직접 Locator와 자동화 로직을 작성하는 방향으로 발전하면 됩니다.

---

# 참고 자료

- Playwright Python 공식 문서: https://playwright.dev/python/
- Playwright Python 설치: https://playwright.dev/python/docs/library
- Playwright Codegen: https://playwright.dev/python/docs/codegen-intro
- Playwright Locator: https://playwright.dev/python/docs/locators
- Playwright Auto-Waiting: https://playwright.dev/python/docs/actionability
- Selenium 공식 문서: https://www.selenium.dev/documentation/
