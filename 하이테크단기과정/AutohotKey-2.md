# AutoHotkey 키보드 입력과 클립보드 자동화

## 1. 오늘 배울 내용

지난 시간에는 AutoHotkey의 `SendText`를 이용해서 키보드 입력을 자동화했습니다.

```ahk
F3::
{
    SendText "Hello AutoHotkey"
}
```

메모장이나 일반 입력창에서는 이것만으로도 충분히 자동 입력이 가능합니다.

하지만 실제 웹사이트에서는 이야기가 조금 다릅니다.

로그인, 회원가입, 결제 등 중요한 기능을 제공하는 웹사이트는 자동화 프로그램이나 비정상적인 입력을 탐지하기 위해 여러 가지 보안 기능을 사용할 수 있습니다.

따라서 오늘은 두 가지 입력 방법을 비교해봅니다.

```text
방법 1
AutoHotkey → SendText → 입력창

방법 2
AutoHotkey → Clipboard → Ctrl + V → 입력창
```

중요한 점은 **클립보드 방식이 보안 기능을 우회하는 기술이라는 뜻이 아니라, Windows에서 문자를 입력하는 서로 다른 방법을 학습하는 것**입니다.

---

# 2. 오늘 만들 프로그램

단축키를 다음과 같이 구성합니다.

| 단축키 | 기능 |
|---|---|
| F2 | Chrome 실행 및 실습 페이지 접속 |
| F3 | 아이디를 `SendText`로 입력 |
| F4 | 비밀번호를 `SendText`로 입력 |
| F5 | 아이디를 Clipboard로 붙여넣기 |
| F6 | 비밀번호를 Clipboard로 붙여넣기 |
| ESC | AutoHotkey 종료 |

실습용 계정은 다음과 같이 사용합니다.

```text
ID : student01
PW : class1234
```

실제 사용하는 아이디와 비밀번호는 수업 코드에 넣지 않습니다.

---

# 3. AutoHotkey 기본 코드 만들기

먼저 다음 파일을 만듭니다.

```text
login_macro.ahk
```

그리고 다음 코드를 작성합니다.

```ahk
#Requires AutoHotkey v2.0

demoId := "student01"
demoPw := "class1234"

Esc::
{
    ExitApp
}
```

---

# 4. F2를 누르면 Chrome 실행하기

먼저 Chrome이 실행되고 있는지 확인해봅니다.

AutoHotkey에서는 다음과 같이 프로그램의 실행 여부를 확인할 수 있습니다.

```ahk
WinExist("ahk_exe chrome.exe")
```

Chrome이 있다면 기존 Chrome을 활성화합니다.

```ahk
WinActivate "ahk_exe chrome.exe"
```

Chrome이 없다면 실행합니다.

```ahk
Run "chrome.exe"
```

따라서 다음과 같이 만들 수 있습니다.

```ahk
F2::
{
    if WinExist("ahk_exe chrome.exe")
    {
        WinActivate "ahk_exe chrome.exe"
    }
    else
    {
        Run "chrome.exe"
    }
}
```

### 동작 순서

```text
F2
 ↓
Chrome이 실행 중인가?
 ↓
YES → 기존 Chrome 활성화
NO  → Chrome 실행
```

---

# 5. Chrome 주소창으로 이동하기

Chrome에서

```text
Ctrl + L
```

을 누르면 주소창으로 이동할 수 있습니다.

AutoHotkey에서는:

```ahk
Send "^l"
```

입니다.

따라서:

```ahk
F2::
{
    if WinExist("ahk_exe chrome.exe")
    {
        WinActivate "ahk_exe chrome.exe"
    }
    else
    {
        Run "chrome.exe"
        Sleep 1000
    }

    Send "^l"
}
```

---

# 6. 실습 페이지 주소 입력하기

실습 페이지의 주소가 다음이라고 가정해봅시다.

```text
file:///C:/AHK/login_demo.html
```

주소창에 입력하고 Enter를 누릅니다.

```ahk
SendText "file:///C:/AHK/login_demo.html"
Send "{Enter}"
```

전체 코드는 다음과 같습니다.

```ahk
F2::
{
    if WinExist("ahk_exe chrome.exe")
    {
        WinActivate "ahk_exe chrome.exe"
    }
    else
    {
        Run "chrome.exe"
        Sleep 1000
    }

    Sleep 300

    Send "^l"
    SendText "file:///C:/AHK/login_demo.html"
    Send "{Enter}"
}
```

---

# 7. F3으로 아이디 입력하기

이번에는 로그인 페이지의 아이디 입력창을 마우스로 클릭합니다.

그리고 F3을 누릅니다.

```ahk
F3::
{
    SendText "student01"
}
```

변수를 사용하면:

```ahk
demoId := "student01"

F3::
{
    SendText demoId
}
```

---

# 8. F4로 비밀번호 입력하기

비밀번호 입력창을 마우스로 선택하고 F4를 누릅니다.

```ahk
F4::
{
    SendText demoPw
}
```

현재까지 코드는 다음과 같습니다.

```ahk
#Requires AutoHotkey v2.0

demoId := "student01"
demoPw := "class1234"


F2::
{
    if WinExist("ahk_exe chrome.exe")
    {
        WinActivate "ahk_exe chrome.exe"
    }
    else
    {
        Run "chrome.exe"
        Sleep 1000
    }

    Sleep 300

    Send "^l"
    SendText "file:///C:/AHK/login_demo.html"
    Send "{Enter}"
}


F3::
{
    SendText demoId
}


F4::
{
    SendText demoPw
}


Esc::
{
    ExitApp
}
```

---

# 9. 여기서 확인할 것

아이디 입력창 클릭 후:

```text
F3
```

비밀번호 입력창 클릭 후:

```text
F4
```

를 누릅니다.

실습 페이지에서는 매우 빠른 자동 입력을 감지하도록 만들어 두었기 때문에 로그인 버튼을 누르면 다음과 같은 메시지를 보여주도록 합니다.

```text
자동 입력이 의심됩니다.

추가 인증이 필요합니다.
```

여기서 학생들에게 질문합니다.

> 사람이 키보드로 입력한 것과 프로그램이 입력한 것은 항상 같은 입력일까?

---

# 10. Windows Clipboard

이번에는 다른 방법을 사용해봅니다.

Windows에는 **Clipboard**라는 임시 저장 공간이 있습니다.

우리가 일반적으로 사용하는:

```text
Ctrl + C
Ctrl + V
```

도 Clipboard를 이용합니다.

AutoHotkey에서는 Clipboard를 다음 변수로 사용할 수 있습니다.

```ahk
A_Clipboard
```

예:

```ahk
A_Clipboard := "Hello"
```

이 코드를 실행하면 Windows Clipboard에

```text
Hello
```

가 들어갑니다.

이 상태에서:

```text
Ctrl + V
```

를 누르면 Hello가 붙여넣어집니다.

---

# 11. AutoHotkey에서 Ctrl + V

AutoHotkey에서 Ctrl은:

```text
^
```

기호를 사용합니다.

따라서:

```ahk
Send "^v"
```

는 실제로

```text
Ctrl + V
```

를 누르는 것과 같습니다.

---

# 12. F5로 아이디 붙여넣기

이번에는 아이디를 Clipboard에 저장합니다.

```ahk
F5::
{
    A_Clipboard := demoId

    Send "^v"
}
```

조금 더 안정적으로 만들면:

```ahk
F5::
{
    A_Clipboard := demoId

    ClipWait 1

    Send "^v"
}
```

`ClipWait`는 Clipboard에 데이터가 준비될 때까지 기다립니다.

---

# 13. F6으로 비밀번호 붙여넣기

비밀번호도 동일합니다.

```ahk
F6::
{
    A_Clipboard := demoPw

    ClipWait 1

    Send "^v"
}
```

---

# 14. 최종 AutoHotkey 코드

```ahk
#Requires AutoHotkey v2.0


; =====================================
; 실습용 계정
; =====================================

demoId := "student01"
demoPw := "class1234"


; =====================================
; F2 : Chrome 실행 + 실습 페이지 이동
; =====================================

F2::
{
    if WinExist("ahk_exe chrome.exe")
    {
        WinActivate "ahk_exe chrome.exe"
    }
    else
    {
        Run "chrome.exe"

        Sleep 1000
    }

    Sleep 300

    Send "^l"

    SendText "file:///C:/AHK/login_demo.html"

    Send "{Enter}"
}


; =====================================
; F3 : SendText로 ID 입력
; =====================================

F3::
{
    SendText demoId
}


; =====================================
; F4 : SendText로 Password 입력
; =====================================

F4::
{
    SendText demoPw
}


; =====================================
; F5 : Clipboard로 ID 입력
; =====================================

F5::
{
    A_Clipboard := demoId

    ClipWait 1

    Send "^v"
}


; =====================================
; F6 : Clipboard로 Password 입력
; =====================================

F6::
{
    A_Clipboard := demoPw

    ClipWait 1

    Send "^v"
}


; =====================================
; ESC : 프로그램 종료
; =====================================

Esc::
{
    ExitApp
}
```

---

# 15. 두 방법 비교

## SendText 방식

```ahk
SendText "student01"
```

동작 과정:

```text
AutoHotkey
    ↓
키 입력 생성
    ↓
입력창
```

장점:

- 코드가 매우 간단하다.
- Clipboard를 변경하지 않는다.
- 일반적인 프로그램 자동화에 편리하다.

---

## Clipboard 방식

```ahk
A_Clipboard := "student01"

ClipWait 1

Send "^v"
```

동작 과정:

```text
AutoHotkey
    ↓
Windows Clipboard
    ↓
Ctrl + V
    ↓
입력창
```

장점:

- 긴 문자열 입력이 편리하다.
- 한글이나 특수문자가 포함된 문자열 입력에 유용하다.
- 프로그램에 따라 `SendText`보다 안정적으로 동작하는 경우가 있다.

---

# 16. Clipboard 사용 시 주의사항

다음 코드를 실행하면:

```ahk
A_Clipboard := "class1234"
```

Windows Clipboard에 비밀번호가 남습니다.

사용자가 이후:

```text
Ctrl + V
```

를 누르면 비밀번호가 그대로 붙여넣어질 수 있습니다.

따라서 실제 프로그램에서는 민감한 정보를 Clipboard에 오래 남겨두지 않는 것이 좋습니다.

예를 들어 실습이 끝난 다음 Clipboard를 비울 수 있습니다.

```ahk
A_Clipboard := ""
```

---

# 17. 기존 Clipboard 보존하기

사용자가 기존에 복사해 놓은 내용이 있다고 생각해봅시다.

AutoHotkey가 Clipboard를 덮어쓰면 기존 내용이 사라집니다.

따라서 기존 Clipboard를 저장할 수도 있습니다.

```ahk
oldClipboard := ClipboardAll()

A_Clipboard := "student01"

ClipWait 1

Send "^v"

Sleep 300

A_Clipboard := oldClipboard
```

동작 과정:

```text
기존 Clipboard 저장
        ↓
새로운 문자열 저장
        ↓
Ctrl + V
        ↓
기존 Clipboard 복원
```

---

# 18. 오늘의 핵심

지난 시간:

```ahk
SendText "Hello"
```

오늘:

```ahk
A_Clipboard := "Hello"

Send "^v"
```

두 방법 모두 결과적으로는 화면에 글자가 입력되지만 **입력 과정은 서로 다릅니다.**

자동화 프로그램을 만들 때 중요한 것은 단순히:

> 마우스를 클릭하고 글자를 입력하는 것

만이 아닙니다.

상황에 따라:

```text
SendText
Clipboard
ControlSend
ControlSetText
ImageSearch
ControlClick
```

등 여러 방법 중 적절한 방법을 선택해야 합니다.

---

# 실습 문제 1

F7을 누르면 다음 문장을 Clipboard로 입력하도록 만들어보세요.

```text
한국폴리텍대학 AutoHotkey 수업입니다.
```

정답:

```ahk
F7::
{
    A_Clipboard := "한국폴리텍대학 AutoHotkey 수업입니다."

    ClipWait 1

    Send "^v"
}
```

---

# 실습 문제 2

F8을 누르면 다음 세 줄을 한번에 붙여넣어보세요.

```text
이름 : 홍길동
학번 : 20260001
학과 : AI소프트웨어과
```

힌트:

AutoHotkey에서 줄바꿈은:

```ahk
`n
```

입니다.

정답:

```ahk
F8::
{
    A_Clipboard :=
        "이름 : 홍길동`n"
        . "학번 : 20260001`n"
        . "학과 : AI소프트웨어과"

    ClipWait 1

    Send "^v"
}
```

---

# 다음 시간 연결

이번 시간에는:

```text
키보드 자동 입력
        ↓
Clipboard
        ↓
붙여넣기
```

를 배웠습니다.

다음에는 프로그램이 단순히 정해진 행동만 하는 것이 아니라 화면 상태를 판단하도록 만들어봅니다.

예:

```text
버튼이 있는가?
        ↓
YES → 버튼 클릭
NO  → 기다리기

특정 이미지가 있는가?
        ↓
YES → 다음 작업
NO  → 오류 처리
```

이를 이용하면 단순 매크로에서 한 단계 발전한 **상태를 판단하는 자동화 프로그램**을 만들 수 있습니다.
