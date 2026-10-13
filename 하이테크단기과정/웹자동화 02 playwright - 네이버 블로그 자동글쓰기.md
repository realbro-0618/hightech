# Playwright를 이용한 네이버 로그인 + ChatGPT 블로그 글 작성 자동화

> 대상: 코딩을 처음 배우는 수강생  
> 사용 언어: Python  
> 사용 도구: Playwright, Chrome, pyperclip  
> 수업 목표: 사람이 브라우저에서 하던 반복 작업을 Python으로 자동화하고, ChatGPT를 이용해 블로그 글 초안을 만드는 과정까지 연결해본다.

---

# 1. 이번 수업에서 만들어볼 것

이번 수업에서는 두 가지 자동화를 만들어봅니다.

첫 번째는 **네이버 로그인 자동화**입니다.

두 번째는 **ChatGPT에 블로그 글 작성을 요청하고, 생성된 답변을 복사하는 자동화**입니다.

전체 흐름은 다음과 같습니다.

```text
Python 실행
   ↓
Chrome 실행
   ↓
Playwright가 Chrome에 연결
   ↓
네이버 로그인 자동화
   ↓
ChatGPT 접속
   ↓
블로그 글 작성 요청
   ↓
ChatGPT 답변 생성
   ↓
답변 복사
   ↓
블로그 작성에 활용
```

이번 수업에서 중요한 것은 단순히 코드를 복사해서 실행하는 것이 아닙니다.

왜 `subprocess`를 사용하는지, 왜 Chrome의 디버깅 포트를 여는지, 왜 `pyperclip`으로 아이디와 비밀번호를 붙여넣는지, 왜 `persistent context`를 사용하는지까지 이해하는 것이 중요합니다.

---

# 2. 필요한 라이브러리 설치

터미널에서 다음 명령을 실행합니다.

```bash
pip install playwright
```

환경에 따라 위 명령이 안 된다면:

```bash
python -m pip install playwright
```

그다음 Playwright에서 사용할 브라우저를 설치합니다.

```bash
playwright install
```

이 명령이 안 된다면:

```bash
python -m playwright install
```

이번 수업에서는 클립보드 기능도 사용하기 때문에 `pyperclip`도 설치합니다.

```bash
pip install pyperclip
```

---

# 3. 이번 수업에서 일반 Chrome을 사용하는 이유

Playwright는 기본적으로 Playwright가 관리하는 Chromium 브라우저를 실행할 수 있습니다.

```python
browser = p.chromium.launch(
    headless=False
)
```

그런데 실제 자동화를 만들다 보면 다음과 같은 상황이 생깁니다.

```text
이미 로그인되어 있는 Chrome을 사용하고 싶다.

기존 쿠키를 유지하고 싶다.

브라우저 프로필을 계속 사용하고 싶다.

사람이 먼저 로그인하고,
그 다음 Python이 이어서 제어하게 하고 싶다.
```

이럴 때 사용할 수 있는 방법 중 하나가 **Chrome Remote Debugging Port**입니다.

이번 수업에서는 Chrome을 Python에서 직접 실행하면서 `9222`번 포트를 열고, Playwright가 그 Chrome 브라우저에 연결하도록 만들어봅니다.

---

# 4. Remote Debugging Port란?

Chrome은 외부 프로그램이 브라우저를 제어할 수 있도록 디버깅용 포트를 열 수 있습니다.

예를 들어 Chrome을 다음과 같이 실행할 수 있습니다.

```text
--remote-debugging-port=9222
```

그러면 구조는 다음과 같습니다.

```text
Python
   ↓
Chrome 실행
   ↓
Chrome이 9222 포트를 엶
   ↓
Playwright가 9222 포트에 접속
   ↓
이미 실행 중인 Chrome 제어
```

즉 Playwright가 Chrome을 새로 만드는 것이 아니라 **이미 실행된 Chrome에 접속해서 제어한다**고 이해하면 됩니다.

---

# 5. 네이버 로그인 자동화 전체 코드

아래 코드는 수업용으로 정리한 버전입니다.

```python
import subprocess
import time
import pyperclip

from playwright.sync_api import sync_playwright


user_id = "naver_id"
password = "naver_password"

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
user_data_dir = r"C:\chrome_debug_profile"


# 1. Chrome 실행
subprocess.Popen([
    chrome_path,
    "--remote-debugging-port=9222",
    f"--user-data-dir={user_data_dir}"
])


# 2. Chrome 실행 대기
time.sleep(2)


# 3. Playwright 실행
with sync_playwright() as p:

    browser = p.chromium.connect_over_cdp(
        "http://127.0.0.1:9222"
    )

    context = browser.contexts[0]

    pages = context.pages

    if len(pages) > 0:
        page = pages[0]
    else:
        page = context.new_page()


    # 4. 네이버 접속
    page.goto(
        "https://www.naver.com"
    )

    print(
        page.title()
    )


    # 5. 로그인 버튼 클릭
    page.get_by_role(
        "link",
        name="NAVER 로그인"
    ).click()


    # 6. 아이디 입력
    pyperclip.copy(
        user_id
    )

    page.get_by_role(
        "textbox",
        name="아이디"
    ).click()

    page.keyboard.press(
        "Control+V"
    )


    # 7. 비밀번호 입력
    pyperclip.copy(
        password
    )

    page.get_by_role(
        "textbox",
        name="비밀번호"
    ).click()

    page.keyboard.press(
        "Control+V"
    )


    # 8. Enter로 로그인
    page.get_by_role(
        "textbox",
        name="비밀번호"
    ).press(
        "Enter"
    )


    # 보안을 위해 클립보드 내용 제거
    pyperclip.copy("")


    input(
        "종료하려면 Enter"
    )
```

---

# 6. import는 왜 사용하는가?

코드 위쪽을 보면 다음과 같은 부분이 있습니다.

```python
import subprocess
import time
import pyperclip

from playwright.sync_api import sync_playwright
```

`import`는 다른 사람이 만들어놓은 기능이나 Python 기본 기능을 내 프로그램에서 가져오는 역할을 합니다.

---

## subprocess

```python
import subprocess
```

`subprocess`는 Python에서 다른 프로그램을 실행할 수 있게 해줍니다.

이번 수업에서는 Python이 직접 Chrome을 실행하기 위해 사용합니다.

즉:

```text
Python
   ↓
Chrome 실행
```

을 가능하게 해주는 기능입니다.

---

## time

```python
import time
```

`time`은 시간과 관련된 기능입니다.

이번 코드에서는:

```python
time.sleep(2)
```

를 사용합니다.

뜻은:

> 2초 동안 잠깐 기다려라.

입니다.

Chrome이 실행되자마자 바로 Playwright가 접속하면 아직 준비가 끝나지 않았을 수 있기 때문에 잠깐 기다립니다.

---

## pyperclip

```python
import pyperclip
```

`pyperclip`은 Windows 클립보드를 사용할 수 있게 해주는 라이브러리입니다.

예를 들어:

```python
pyperclip.copy("안녕하세요")
```

라고 하면 `"안녕하세요"`라는 문자열이 클립보드에 저장됩니다.

사람이 `Ctrl + C`를 한 것과 비슷합니다.

---

# 7. 아이디와 비밀번호를 변수에 저장

```python
user_id = "naver_id"
password = "naver_password"
```

Python에서 값을 저장할 때 변수를 사용합니다.

예를 들어:

```python
name = "홍길동"
```

이라고 하면 `name`이라는 이름으로 `"홍길동"`이라는 값을 저장한 것입니다.

이번 코드에서는 `user_id`, `password`라는 변수에 로그인 정보를 저장합니다.

---

# 8. 로그인 정보 입력 시 주의할 점

수업에서는 실제 네이버 비밀번호를 사용하지 않는 것을 권장합니다.

실제 프로그램에서 다음처럼 비밀번호를 코드에 직접 적어두면:

```python
password = "my_real_password"
```

파일이 다른 사람에게 전달되거나 GitHub에 올라갔을 때 비밀번호가 노출될 수 있습니다.

이번 수업에서는 Playwright 동작 원리를 배우기 위해 단순한 형태로 작성하지만, 실제 프로젝트에서는 환경변수나 별도의 보안 저장소를 사용하는 것이 좋습니다.

---

# 9. Chrome 경로 설정

```python
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
```

Python에게 Chrome 프로그램이 어디에 있는지 알려주는 부분입니다.

Windows에서는 보통 다음 위치에 설치됩니다.

```text
C:\Program Files\Google\Chrome\Application\chrome.exe
```

PC에 따라:

```text
C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
```

일 수도 있습니다.

---

# 10. 문자열 앞에 r을 붙이는 이유

```python
r"C:\Program Files\Google\Chrome\Application\chrome.exe"
```

Windows 경로에는 `\` 문자가 많이 사용됩니다.

Python에서는 `\`가 특별한 의미를 가지는 경우가 있기 때문에 Windows 경로는 `r"..."` 형태로 작성하면 편리합니다.

이것을 Raw String이라고 합니다.

---

# 11. user_data_dir은 무엇인가?

```python
user_data_dir = r"C:\chrome_debug_profile"
```

이 폴더는 Chrome의 사용자 데이터를 저장하는 폴더입니다.

예:

```text
쿠키
사이트 설정
로그인 상태
LocalStorage
일부 캐시 데이터
```

같은 폴더를 계속 사용하면 Chrome을 다시 실행해도 이전 상태를 일부 유지할 수 있습니다.

---

# 12. Python에서 Chrome 실행하기

```python
subprocess.Popen([
    chrome_path,
    "--remote-debugging-port=9222",
    f"--user-data-dir={user_data_dir}"
])
```

이 부분이 이번 코드에서 중요한 부분입니다.

- `chrome_path`: 실행할 Chrome 프로그램
- `--remote-debugging-port=9222`: Playwright가 연결할 포트
- `--user-data-dir=...`: Chrome 사용자 데이터 저장 위치

---

# 13. f-string이란?

```python
f"--user-data-dir={user_data_dir}"
```

앞에 `f`가 붙어 있습니다.

이것은 문자열 안에 변수를 쉽게 넣는 방법입니다.

예:

```python
name = "홍길동"

print(
    f"안녕하세요 {name}님"
)
```

결과:

```text
안녕하세요 홍길동님
```

---

# 14. Chrome 실행 후 잠깐 기다리는 이유

```python
time.sleep(2)
```

Python 프로그램은 매우 빠르게 실행됩니다.

Chrome을 실행하라는 명령 직후 바로 다음 줄을 실행하면:

```text
Chrome은 아직 준비 중
        +
Playwright는 이미 접속 시도
```

상황이 생길 수 있습니다.

그러면 `ECONNREFUSED` 같은 오류가 발생할 수 있습니다.

첫 수업에서는 개념 이해를 위해 단순하게 2초 기다리게 합니다.

---

# 15. Playwright 시작

```python
with sync_playwright() as p:
```

Playwright를 시작하는 부분입니다.

이번 수업에서는 비동기 방식이 아니라 동기 방식인 `sync_playwright`를 사용합니다.

코딩을 처음 배우는 학생에게는 이 방식이 더 이해하기 쉽습니다.

---

# 16. 이미 실행된 Chrome에 연결

```python
browser = p.chromium.connect_over_cdp(
    "http://127.0.0.1:9222"
)
```

여기서 중요한 함수는 `connect_over_cdp()`입니다.

뜻은:

> CDP를 이용해서 이미 실행 중인 Chromium 계열 브라우저에 연결한다.

입니다.

CDP는 Chrome DevTools Protocol의 약자입니다.

쉽게 생각하면 Chrome과 외부 프로그램이 대화하기 위한 통신 방법입니다.

---

# 17. 127.0.0.1은 무엇인가?

```text
127.0.0.1
```

은 현재 사용 중인 자기 자신의 컴퓨터를 의미합니다.

보통 `localhost`라고도 부릅니다.

따라서:

```text
http://127.0.0.1:9222
```

는 내 컴퓨터의 9222번 포트에 접속한다는 뜻입니다.

---

# 18. Browser / Context / Page 이해하기

Playwright에서는 다음 구조를 자주 사용합니다.

```text
Browser
   ↓
Context
   ↓
Page
```

- **Browser**: 전체 브라우저 프로그램
- **Context**: 하나의 사용자 환경
- **Page**: 브라우저 탭 하나

---

# 19. 현재 Chrome의 Context 가져오기

```python
context = browser.contexts[0]
```

`browser.contexts`에는 Chrome에서 사용 중인 Context들이 들어 있습니다.

`[0]`은 첫 번째 항목이라는 뜻입니다.

Python 리스트는 0부터 시작합니다.

---

# 20. 현재 열려 있는 탭 가져오기

```python
pages = context.pages
```

현재 Chrome에서 열려 있는 페이지들을 가져옵니다.

예:

```text
pages[0]
pages[1]
pages[2]
```

처럼 여러 탭이 있을 수 있습니다.

---

# 21. 페이지가 이미 열려 있는지 확인

```python
if len(pages) > 0:
    page = pages[0]
else:
    page = context.new_page()
```

뜻은:

```text
열려 있는 탭이 하나 이상 있으면
   ↓
첫 번째 탭 사용

열려 있는 탭이 없으면
   ↓
새로운 탭 생성
```

입니다.

---

# 22. 네이버 접속

```python
page.goto(
    "https://www.naver.com"
)
```

`goto()`는 웹사이트 주소로 이동하는 기능입니다.

사람이 주소창에 주소를 입력하고 Enter를 누르는 것과 비슷합니다.

---

# 23. Locator란?

웹 자동화에서 가장 중요한 개념 중 하나입니다.

사람은 화면을 보고 로그인 버튼을 바로 찾을 수 있지만, Python은 어떤 요소를 클릭해야 하는지 알려줘야 합니다.

그때 사용하는 것이 Locator입니다.

---

# 24. 네이버 로그인 버튼 찾기

```python
page.get_by_role(
    "link",
    name="NAVER 로그인"
).click()
```

이 코드를 사람의 말로 바꾸면:

> 현재 페이지에서 역할이 link이고 이름이 NAVER 로그인인 요소를 찾아 클릭해라.

입니다.

---

# 25. 왜 get_by_role()을 사용하는가?

웹페이지에는 다음과 같은 여러 요소가 있습니다.

```text
버튼
링크
입력창
이미지
메뉴
체크박스
```

`get_by_role()`은 요소의 역할을 이용해 찾습니다.

예:

```python
page.get_by_role(
    "button",
    name="확인"
)
```

사람이 화면을 이해하는 방식과 비슷해서 코드가 읽기 쉽습니다.

---

# 26. 왜 fill() 대신 클립보드를 사용할까?

보통 Playwright에서는 다음처럼 입력할 수 있습니다.

```python
page.get_by_role(
    "textbox",
    name="아이디"
).fill(
    user_id
)
```

그런데 이번 코드에서는:

```text
클립보드에 복사
        ↓
입력창 클릭
        ↓
Ctrl + V
```

방식을 사용합니다.

이렇게 하면 실제 사용자가 복사해서 붙여넣는 동작과 비슷하게 처리할 수 있습니다.

---

# 27. 아이디 입력 과정

```python
pyperclip.copy(
    user_id
)
```

아이디를 Windows 클립보드에 저장합니다.

그다음:

```python
page.get_by_role(
    "textbox",
    name="아이디"
).click()
```

으로 아이디 입력창을 클릭합니다.

마지막으로:

```python
page.keyboard.press(
    "Control+V"
)
```

를 실행하면 클립보드의 아이디가 입력됩니다.

---

# 28. 비밀번호도 같은 방식

```python
pyperclip.copy(
    password
)

page.get_by_role(
    "textbox",
    name="비밀번호"
).click()

page.keyboard.press(
    "Control+V"
)
```

순서는:

```text
비밀번호를 클립보드에 복사
        ↓
비밀번호 입력창 클릭
        ↓
Ctrl + V
```

입니다.

---

# 29. Enter로 로그인

```python
page.get_by_role(
    "textbox",
    name="비밀번호"
).press(
    "Enter"
)
```

비밀번호 입력창에서 Enter 키를 누릅니다.

---

# 30. 클립보드를 지우는 이유

```python
pyperclip.copy("")
```

비밀번호를 클립보드에 복사하면 Windows 클립보드에 그대로 남을 수 있습니다.

그래서 로그인 후 빈 문자열을 복사해서 클립보드를 지웁니다.

특히 `Win + V` 클립보드 기록 기능을 쓰는 경우 실제 비밀번호를 사용할 때는 주의해야 합니다.

---

# 31. 여기까지 자동화 흐름

```text
Python 실행
   ↓
Chrome 실행
   ↓
9222 포트 오픈
   ↓
Playwright 연결
   ↓
네이버 이동
   ↓
로그인 버튼 클릭
   ↓
아이디 붙여넣기
   ↓
비밀번호 붙여넣기
   ↓
Enter
   ↓
로그인
```

---

# 32. ChatGPT 자동화를 해보자

다음 단계는 ChatGPT를 Playwright로 제어하는 것입니다.

이번 실습에서는 다음 과정을 자동화합니다.

```text
ChatGPT 접속
   ↓
프롬프트 입력
   ↓
메시지 전송
   ↓
답변 생성 대기
   ↓
답변을 블로그 글 작성에 활용
```

---

# 33. ChatGPT 자동화 코드

아래 코드는 수업용으로 정리한 예제입니다.

```python
from playwright.sync_api import sync_playwright


PROMPT = """
춘천 폴리텍대학교 신입생 모집글을 블로그에 올리고 싶어.
학과는 AI융합과야.
프로그래밍을 전문적으로 배워.

블로그 제목과 본문을 작성해줘.
제목과 본문을 한 번에 복사할 수 있도록 작성해줘.
"""


with sync_playwright() as p:

    context = p.chromium.launch_persistent_context(
        user_data_dir=r"C:\playwright_profile",
        channel="chrome",
        headless=False
    )

    pages = context.pages

    if len(pages) > 0:
        page = pages[0]
    else:
        page = context.new_page()


    page.goto(
        "https://chatgpt.com/"
    )


    chat_box = page.get_by_role(
        "textbox",
        name="ChatGPT와 채팅"
    )

    chat_box.click()


    chat_box.fill(
        PROMPT
    )


    page.get_by_role(
        "button",
        name="메시지 보내기"
    ).click()


    page.wait_for_timeout(
        30000
    )


    input(
        "답변이 완성되었는지 확인 후 Enter"
    )


    context.close()
```

> ChatGPT 화면의 이름이나 버튼 구조는 서비스 업데이트에 따라 달라질 수 있습니다.  
> Locator가 맞지 않는 경우에는 Playwright Codegen을 실행해서 현재 화면의 Locator를 다시 확인합니다.

---


# 34. persistent context란?

ChatGPT 자동화에서 핵심은:

```python
launch_persistent_context()
```

입니다.

ChatGPT는 로그인이 필요합니다.

매번 이메일, 비밀번호, 인증 과정을 자동화하면 번거롭습니다.

그래서 한 번 로그인한 브라우저 상태를 저장해두고 다음 실행에서도 계속 사용하는 것이 편합니다.

---

# 35. persistent context 구조

```python
context = p.chromium.launch_persistent_context(
    user_data_dir=r"C:\playwright_profile",
    channel="chrome",
    headless=False
)
```

각 옵션의 의미는 다음과 같습니다.

- `user_data_dir`: 브라우저 프로필 저장 위치
- `channel="chrome"`: 실제 Google Chrome 사용
- `headless=False`: 브라우저 화면 표시

---

# 36. user_data_dir

```python
user_data_dir=r"C:\playwright_profile"
```

이 폴더에 브라우저 데이터가 저장됩니다.

예:

```text
쿠키
로그인 세션
사이트 설정
LocalStorage
```

첫 실행에서는 ChatGPT에 직접 로그인해야 할 수 있습니다.

그다음부터는 로그인 상태가 유지되는 경우가 많습니다.

---

# 37. channel="chrome"

```python
channel="chrome"
```

Playwright가 설치한 Chromium이 아니라 PC에 설치된 Google Chrome을 사용합니다.

---

# 38. headless=False

```python
headless=False
```

브라우저 화면을 실제로 보여줍니다.

초보자 수업에서는 자동화가 어떻게 움직이는지 볼 수 있어서 `False`로 사용하는 것이 좋습니다.

---

# 39. ChatGPT 입력창 찾기

```python
chat_box = page.get_by_role(
    "textbox",
    name="ChatGPT와 채팅"
)
```

여기서도 Locator를 사용합니다.

사람은 화면에서 입력창을 눈으로 찾지만 Playwright는:

```text
role = textbox
name = ChatGPT와 채팅
```

이라는 정보를 이용해 찾습니다.

---

# 40. 프롬프트를 변수에 넣는 이유

```python
PROMPT = """
...
"""
```

긴 프롬프트를 변수로 따로 빼두면 코드가 훨씬 읽기 쉬워집니다.

여러 줄 문자열은 `"""`를 사용하면 편리합니다.

---

# 41. ChatGPT에 메시지 보내기

```python
chat_box.fill(
    PROMPT
)
```

으로 입력하고:

```python
page.get_by_role(
    "button",
    name="메시지 보내기"
).click()
```

으로 전송합니다.

---


# 43. 실제 프로그램에서는 어떻게 개선할까?

실제로는 고정 시간을 기다리는 것보다:

```text
답변 생성이 끝났는지 확인
```

하는 것이 더 좋습니다.

예를 들어:

```text
중지 버튼이 사라졌는지
복사 버튼이 나타났는지
응답 영역이 만들어졌는지
```

같은 화면 상태를 확인하는 방식이 더 안정적입니다.

---

# 44. ChatGPT 복사 버튼 Locator

처음 코드에는 다음과 같은 코드가 있었습니다.

```python
page.get_by_role(
    "region",
    name="DIL content"
).get_by_label(
    "복사"
).click()
```

이 방식은 현재 화면 구조에 의존합니다.

ChatGPT처럼 자주 업데이트되는 서비스는 Locator가 달라질 수 있습니다.

따라서 수업에서는:

```text
1. Codegen 실행

2. 실제 복사 버튼 클릭

3. Codegen이 만든 Locator 확인

4. 그 코드를 프로그램에 적용
```

순서로 찾는 방법을 권장합니다.

---

# 45. Codegen으로 복사 버튼 찾기

터미널에서:

```bash
playwright codegen https://chatgpt.com
```

환경에 따라:

```bash
python -m playwright codegen https://chatgpt.com
```

을 사용할 수 있습니다.

그다음 직접 ChatGPT에서 답변의 복사 버튼을 클릭하면 Codegen이 현재 화면에 맞는 Locator를 만들어줍니다.

---

# 46. context.close()만 사용하는 이유

처음 코드에는:

```python
context.close()
browser.close()
```

가 있었습니다.

그런데 `launch_persistent_context()`를 사용한 코드에서는 별도의 `browser` 변수를 만들지 않았습니다.

그래서 `browser.close()`를 호출하면 오류가 발생할 수 있습니다.

이 경우에는:

```python
context.close()
```

만 사용하면 됩니다.

---

# 47. 네이버 방식과 ChatGPT 방식의 차이

이번 수업에서는 일부러 두 가지 방법을 배웁니다.

## 네이버

```text
Python이 Chrome 실행
        ↓
9222 포트 사용
        ↓
connect_over_cdp()
        ↓
이미 실행된 Chrome에 연결
```

## ChatGPT

```text
Playwright가 Chrome 실행
        ↓
launch_persistent_context()
        ↓
전용 프로필 유지
        ↓
로그인 상태 재사용
```

---

# 48. 왜 두 가지 방식을 모두 배우는가?

상황에 따라 알맞은 방법이 다르기 때문입니다.

이미 실행 중인 Chrome을 이어서 제어하고 싶다면:

```python
connect_over_cdp()
```

Playwright가 브라우저를 실행하면서 로그인 상태를 계속 유지하고 싶다면:

```python
launch_persistent_context()
```

가 편합니다.

둘 중 하나가 무조건 더 좋은 것이 아니라 **자동화하려는 상황에 맞게 선택하는 것**이 중요합니다.

---

# 49. 이번 수업 핵심 구조

## 네이버 로그인

```text
subprocess.Popen()
        ↓
Chrome 실행
        ↓
--remote-debugging-port=9222
        ↓
connect_over_cdp()
        ↓
Locator
        ↓
pyperclip
        ↓
Ctrl + V
        ↓
로그인
```

## ChatGPT

```text
launch_persistent_context()
        ↓
Chrome 프로필 유지
        ↓
ChatGPT 접속
        ↓
Locator
        ↓
fill()
        ↓
메시지 전송
        ↓
응답 기다리기
```

---

# 50. 실습 1 - Chrome 자동 실행 확인

네이버 로그인 코드를 실행합니다.

확인할 것:

```text
Chrome이 자동으로 실행되는가?
9222 포트로 실행되는가?
네이버 사이트가 열리는가?
```

---

# 51. 실습 2 - 네이버 로그인 버튼 클릭

다음 코드까지만 실행해봅니다.

```python
page.goto(
    "https://www.naver.com"
)

page.get_by_role(
    "link",
    name="NAVER 로그인"
).click()
```

확인할 것:

```text
네이버 접속
   ↓
로그인 화면 이동
```

---

# 52. 실습 3 - 아이디 붙여넣기

```python
pyperclip.copy(
    user_id
)

page.get_by_role(
    "textbox",
    name="아이디"
).click()

page.keyboard.press(
    "Control+V"
)
```

확인할 것:

```text
클립보드 복사
   ↓
입력창 클릭
   ↓
Ctrl + V
   ↓
아이디 입력
```

---

# 53. 실습 4 - ChatGPT 로그인 상태 유지

ChatGPT 코드를 처음 실행합니다.

```python
context = p.chromium.launch_persistent_context(
    user_data_dir=r"C:\playwright_profile",
    channel="chrome",
    headless=False
)
```

직접 ChatGPT에 로그인합니다.

프로그램을 종료하고 다시 실행했을 때 로그인 상태가 유지되는지 확인합니다.

---

# 54. 실습 5 - ChatGPT 프롬프트 변경

기본 프롬프트를 학생이 직접 바꿔봅니다.

예:

```text
춘천 여행지 소개
Python 초보자 공부법
AI융합과 수업 소개
대학생 취업 준비 방법
```

프롬프트가 달라지면 ChatGPT의 결과가 어떻게 달라지는지 확인합니다.

---

# 55. 다음 단계 - 네이버 블로그 글쓰기까지 연결

다음 단계에서는 다음 흐름으로 확장할 수 있습니다.

```text
ChatGPT에서 글 생성
        ↓
답변 복사
        ↓
네이버 블로그 접속
        ↓
글쓰기 버튼 클릭
        ↓
제목 입력
        ↓
본문 입력
        ↓
최종 확인
        ↓
발행
```

---

# 56. 블로그 자동 발행 시 주의할 점

실제 서비스 자동화에서는 다음을 확인해야 합니다.

```text
서비스 이용약관
자동화 정책
로그인 보안
CAPTCHA
비정상 로그인 탐지
자동 게시 제한
```

수업에서는 자동화 기술을 배우는 것이 목적이므로, 처음에는 **글쓰기 화면 이동 + 제목 입력 + 본문 입력** 정도까지 연습하고 실제 발행은 사람이 최종 확인하는 방식으로 진행하는 것이 좋습니다.

---

# 57. 이번 수업에서 꼭 기억할 6가지

## 1. subprocess

```python
subprocess.Popen()
```

Python에서 다른 프로그램을 실행합니다.

## 2. Remote Debugging Port

```text
--remote-debugging-port=9222
```

실행 중인 Chrome에 Playwright가 접속할 수 있게 합니다.

## 3. connect_over_cdp

```python
p.chromium.connect_over_cdp()
```

이미 실행 중인 Chrome에 Playwright가 연결합니다.

## 4. Locator

```python
page.get_by_role()
```

웹페이지에서 원하는 요소를 찾습니다.

## 5. pyperclip + Ctrl + V

```python
pyperclip.copy()

page.keyboard.press(
    "Control+V"
)
```

Windows 클립보드를 이용해 값을 붙여넣습니다.

## 6. persistent context

```python
launch_persistent_context()
```

로그인 상태와 쿠키 등을 유지할 수 있는 Chrome 프로필을 사용합니다.

---

# 58. 전체 흐름 다시 보기

```text
[네이버]

Python
 ↓
Chrome 실행
 ↓
9222 포트 오픈
 ↓
Playwright 연결
 ↓
네이버 접속
 ↓
로그인


[ChatGPT]

Python
 ↓
Persistent Chrome 실행
 ↓
로그인 상태 유지
 ↓
ChatGPT 접속
 ↓
프롬프트 입력
 ↓
글 생성


[다음 단계]

생성된 글
 ↓
네이버 블로그
 ↓
제목 입력
 ↓
본문 입력
 ↓
최종 확인
```

---

# 59. 강의 마무리

이번 수업에서 중요한 것은 단순히:

```python
click()
fill()
```

같은 명령어를 외우는 것이 아닙니다.

웹 자동화는 결국:

```text
사람이 하는 작업을 분석하고
        ↓
그 행동을 작은 단계로 나누고
        ↓
각 단계를 Python 코드로 바꾸고
        ↓
화면 상태를 확인하면서 다음 행동을 결정하는 것
```

입니다.

이번 네이버 로그인과 ChatGPT 자동화를 통해:

```text
브라우저 실행
로그인
Locator
클립보드
키보드 입력
Chrome 프로필
AI 서비스 연동
```

까지 한 번에 경험할 수 있습니다.

다음 수업에서는 여기서 한 단계 더 나아가 **ChatGPT가 작성한 글을 네이버 블로그 글쓰기 화면에 자동으로 입력하는 과정**까지 연결할 수 있습니다.
