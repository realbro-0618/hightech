# AutoHotkey 기초 자동화

## 1. 학습 목표

이번 시간에는 AutoHotkey를 이용하여 Windows에서 반복적으로 수행하는 작업을 자동화하는 방법을 학습한다.

이번 수업을 통해 다음 기능을 사용할 수 있다.

- AutoHotkey 설치 및 `.ahk` 파일 실행
- 단축키(Hotkey) 만들기
- 키보드 자동 입력
- 마우스 이동 및 클릭
- 프로그램 실행
- 특정 프로그램 창 찾기
- 프로그램 창 활성화
- Window Spy를 이용한 프로그램 정보 확인

---

# 2. AutoHotkey란?

AutoHotkey는 Windows 환경에서 키보드와 마우스 작업을 자동화할 수 있는 프로그램이다.

사람이 반복적으로 수행하는 다음과 같은 작업을 코드로 작성할 수 있다.

```text
프로그램 실행
    ↓
특정 위치 클릭
    ↓
문자 입력
    ↓
Enter
    ↓
다른 프로그램으로 이동
```

단순한 단축키부터 반복 업무 자동화 프로그램까지 만들 수 있다.

---

# 3. AutoHotkey 설치

AutoHotkey 공식 홈페이지에서 **AutoHotkey v2**를 설치한다.

이번 수업에서는 모든 코드를 **AutoHotkey v2 문법**으로 작성한다.

인터넷에는 AutoHotkey v1 예제도 많이 존재하므로 코드 검색 시 버전을 확인해야 한다.

작성하는 `.ahk` 파일의 첫 번째 줄에는 다음 코드를 추가한다.

```ahk
#Requires AutoHotkey v2.0
```

이 코드는 현재 스크립트가 AutoHotkey v2 이상에서 실행되어야 한다는 것을 의미한다.

---

# 4. 첫 번째 AutoHotkey 프로그램

새로운 파일을 만든 후 다음과 같이 저장한다.

```text
hello.ahk
```

파일 내용:

```ahk
#Requires AutoHotkey v2.0

MsgBox "Hello AutoHotkey!"
```

`hello.ahk` 파일을 더블클릭하여 실행한다.

다음과 같은 메시지 창이 나타나면 정상적으로 실행된 것이다.

```text
Hello AutoHotkey!
```

## MsgBox

`MsgBox`는 화면에 메시지 창을 출력하는 명령이다.

```ahk
MsgBox "안녕하세요"
```

Python의 다음 코드와 비슷한 역할을 한다.

```python
print("안녕하세요")
```

---

# 5. 주석 사용하기

코드에 설명을 작성할 때는 `;`를 사용한다.

```ahk
; AutoHotkey 첫 번째 프로그램

MsgBox "안녕하세요"
```

`;` 뒤에 작성한 내용은 프로그램 실행에 영향을 주지 않는다.

주석을 적절하게 사용하면 코드의 목적과 동작을 쉽게 이해할 수 있다.

---

# 6. Hotkey

AutoHotkey의 가장 중요한 기능 중 하나가 **Hotkey**이다.

Hotkey는 특정 키를 눌렀을 때 원하는 코드를 실행하도록 만드는 기능이다.

예를 들어 F1을 눌렀을 때 메시지를 출력해보자.

```ahk
F1::
{
    MsgBox "F1을 눌렀습니다."
}
```

스크립트를 실행한 상태에서 `F1`을 누르면 메시지 창이 나타난다.

## 기본 구조

```ahk
단축키::
{
    실행할 코드
}
```

예:

```ahk
F2::
{
    MsgBox "F2 실행"
}
```

---

# 7. 여러 키를 조합한 단축키

AutoHotkey에서는 특수문자를 이용하여 Ctrl, Alt, Shift 등의 키를 표현한다.

| 기호 | 키 |
|---|---|
| `^` | Ctrl |
| `!` | Alt |
| `+` | Shift |
| `#` | Windows |
| `F1` | F1 |
| `Esc` | ESC |

## Ctrl + 1

```ahk
^1::
{
    MsgBox "Ctrl + 1"
}
```

## Ctrl + Alt + A

```ahk
^!a::
{
    MsgBox "Ctrl + Alt + A"
}
```

## Windows + A

```ahk
#a::
{
    MsgBox "Windows + A"
}
```

기호를 조합하면 다양한 단축키를 만들 수 있다.

---

# 8. 프로그램 종료 단축키

자동화 실습에서는 프로그램을 즉시 종료할 수 있는 키를 만들어 두는 것이 좋다.

```ahk
Esc::
{
    ExitApp
}
```

이제 `ESC` 키를 누르면 실행 중인 AutoHotkey 스크립트가 종료된다.

특히 반복 클릭이나 반복 입력을 실습할 때 반드시 준비해 두는 것을 권장한다.

---

# 9. 키보드 자동 입력

AutoHotkey에서는 `SendText`를 이용하여 문자열을 자동으로 입력할 수 있다.

```ahk
F1::
{
    SendText "안녕하세요. AutoHotkey입니다."
}
```

실습 방법:

1. AutoHotkey 스크립트를 실행한다.
2. 메모장을 실행한다.
3. 메모장 입력 영역을 클릭한다.
4. `F1`을 누른다.

다음 문자열이 자동으로 입력된다.

```text
안녕하세요. AutoHotkey입니다.
```

---

# 10. 특수키 입력

문자가 아닌 Enter, Tab, Delete 등의 키는 `Send`를 사용한다.

## Enter

```ahk
Send "{Enter}"
```

## Tab

```ahk
Send "{Tab}"
```

## ESC

```ahk
Send "{Esc}"
```

## Delete

```ahk
Send "{Delete}"
```

예를 들어 두 줄의 문장을 자동으로 입력하려면 다음과 같이 작성할 수 있다.

```ahk
F1::
{
    SendText "첫 번째 줄"
    Send "{Enter}"
    SendText "두 번째 줄"
}
```

실행 결과:

```text
첫 번째 줄
두 번째 줄
```

---

# 11. Ctrl 키 조합 보내기

AutoHotkey에서도 우리가 일반적으로 사용하는 단축키를 실행할 수 있다.

## Ctrl + C

```ahk
Send "^c"
```

## Ctrl + V

```ahk
Send "^v"
```

## Ctrl + A

```ahk
Send "^a"
```

예:

```ahk
F1::
{
    Send "^a"
    Send "^c"
}
```

F1을 누르면 다음 동작이 실행된다.

```text
Ctrl + A
   ↓
전체 선택

Ctrl + C
   ↓
복사
```

---

# 12. Sleep

자동화 프로그램에서는 작업과 작업 사이에 일정 시간 기다려야 하는 경우가 많다.

이때 사용하는 명령이 `Sleep`이다.

```ahk
Sleep 1000
```

단위는 **밀리초(ms)** 이다.

| 값 | 시간 |
|---:|---:|
| 100 | 0.1초 |
| 500 | 0.5초 |
| 1000 | 1초 |
| 2000 | 2초 |

예:

```ahk
F1::
{
    SendText "안녕하세요"

    Sleep 1000

    Send "{Enter}"

    Sleep 1000

    SendText "두 번째 줄입니다."
}
```

자동화 프로그램에서는 프로그램이 실행되거나 화면이 변경되는 데 시간이 필요할 수 있으므로 적절한 대기 시간을 주어야 한다.

---

# 13. 프로그램 실행하기

`Run`을 사용하면 AutoHotkey에서 다른 프로그램을 실행할 수 있다.

## 메모장

```ahk
Run "notepad.exe"
```

## 계산기

```ahk
Run "calc.exe"
```

예:

```ahk
F1::
{
    Run "notepad.exe"

    Sleep 1000

    SendText "AutoHotkey 자동 입력 테스트"
}
```

실행 과정:

```text
F1
 ↓
메모장 실행
 ↓
1초 대기
 ↓
문자 자동 입력
```

---

# 14. 마우스 이동

`MouseMove`를 사용하면 원하는 좌표로 마우스를 이동할 수 있다.

```ahk
MouseMove 500, 300
```

의미:

```text
X = 500
Y = 300
```

화면 좌측 상단을 기준으로 마우스를 이동하려면 좌표 기준을 `Screen`으로 설정한다.

```ahk
CoordMode "Mouse", "Screen"
```

전체 코드:

```ahk
#Requires AutoHotkey v2.0

CoordMode "Mouse", "Screen"

F1::
{
    MouseMove 500, 300
}
```

---

# 15. 화면 좌표 이해하기

화면의 좌측 상단은 다음 좌표를 가진다.

```text
(0, 0)
```

오른쪽으로 이동할수록 X 값이 증가하고 아래쪽으로 이동할수록 Y 값이 증가한다.

```text
(0, 0)
  ┌──────────────────────→ X
  │
  │
  │
  │
  ↓
  Y
```

예를 들어:

```text
MouseMove 500, 300
```

은 화면 왼쪽에서 500픽셀, 위쪽에서 300픽셀 떨어진 위치로 마우스를 이동한다.

---

# 16. 마우스 클릭

현재 마우스 위치를 클릭하려면 다음과 같이 작성한다.

```ahk
Click
```

특정 좌표를 클릭할 수도 있다.

```ahk
Click 500, 300
```

## 오른쪽 클릭

```ahk
Click 500, 300, "Right"
```

## 더블 클릭

```ahk
Click 500, 300, 2
```

---

# 17. 가장 간단한 마우스 매크로

다음 동작을 자동으로 수행해보자.

```text
(500, 300) 클릭
       ↓
1초 대기
       ↓
(700, 500) 클릭
```

코드:

```ahk
#Requires AutoHotkey v2.0

CoordMode "Mouse", "Screen"

F1::
{
    Click 500, 300

    Sleep 1000

    Click 700, 500
}
```

이것이 가장 기본적인 형태의 마우스 자동화이다.

---

# 18. 좌표 자동화의 문제점

좌표를 이용하는 방법은 간단하지만 문제가 있다.

예를 들어 다음 코드가 있다고 생각해보자.

```ahk
Click 500, 300
```

프로그램의 창 위치가 변경되면 버튼의 좌표도 변경된다.

```text
처음

┌────────────────────┐
│       [확인]       │
└────────────────────┘

        ↓ 창 이동

         ┌────────────────────┐
         │       [확인]       │
         └────────────────────┘
```

기존 좌표를 그대로 클릭하면 원하는 버튼을 누르지 못하게 된다.

이를 해결하기 위해 프로그램의 창이나 버튼 자체를 찾아서 조작하는 방법을 사용할 수 있다.

그때 사용하는 도구가 **Window Spy**이다.

---

# 19. Window Spy

Window Spy는 화면에 실행 중인 프로그램의 정보를 확인할 수 있는 AutoHotkey 도구이다.

프로그램 창 위에 마우스를 올리면 다음과 같은 정보를 확인할 수 있다.

```text
Window Title
ahk_class
ahk_exe
ahk_pid
ahk_id
```

예:

```text
제목:
메모장

실행 파일:
ahk_exe notepad.exe

PID:
ahk_pid 12345
```

이 정보를 이용하면 좌표 대신 특정 프로그램을 지정하여 자동화할 수 있다.

---

# 20. Window Spy에서 확인할 주요 정보

## Window Title

현재 창의 제목이다.

예:

```text
새 텍스트 문서 - 메모장
```

---

## ahk_exe

프로그램의 실행 파일 이름이다.

예:

```text
ahk_exe notepad.exe
```

일반적으로 자동화할 프로그램을 지정할 때 많이 사용한다.

---

## ahk_class

Windows 프로그램의 창 클래스이다.

예:

```text
ahk_class Notepad
```

또는:

```text
ahk_class #32770
```

---

## ahk_pid

현재 실행 중인 프로세스의 PID(Process ID)이다.

예:

```text
ahk_pid 8532
```

같은 프로그램이 여러 개 실행되어 있는 경우 특정 프로세스를 구분할 때 유용하다.

---

# 21. Control 정보

Window Spy에서 버튼이나 입력창 위에 마우스를 올리면 해당 요소의 Control 정보를 확인할 수 있다.

예:

```text
Button1
Edit1
ComboBox1
```

이 값을 **ClassNN**이라고 부른다.

예를 들어 Window Spy에서 다음과 같이 나타났다고 해보자.

```text
ClassNN: Button17
```

AutoHotkey에서는 이 버튼을 다음 이름으로 지정할 수 있다.

```text
Button17
```

이후 `ControlClick` 등의 기능을 사용하면 마우스 좌표를 직접 사용하지 않고 버튼을 조작할 수 있다.

---

# 22. 특정 프로그램 창 지정하기

AutoHotkey에서는 여러 방법으로 특정 프로그램을 지정할 수 있다.

예를 들어 Window Spy에서 다음 정보를 확인했다고 하자.

```text
창 제목:
한진 운송장 출력

ahk_class:
#32770

ahk_exe:
ozcviewer.exe
```

## 창 제목 이용

```ahk
WinActivate "한진 운송장 출력"
```

## 실행 파일 이름 이용

```ahk
WinActivate "ahk_exe ozcviewer.exe"
```

## Window Class 이용

```ahk
WinActivate "ahk_class #32770"
```

## PID 이용

```ahk
WinActivate "ahk_pid 8532"
```

실무에서는 창 제목이 계속 변하는 프로그램도 있기 때문에 `ahk_exe`를 사용하는 경우가 많다.

---

# 23. 프로그램이 실행 중인지 확인하기

`WinExist()`를 이용하면 원하는 프로그램 창이 존재하는지 확인할 수 있다.

```ahk
if WinExist("ahk_exe notepad.exe")
{
    MsgBox "메모장이 실행 중입니다."
}
```

반대로 실행 중이지 않은 경우를 확인하려면 `!`를 사용할 수 있다.

```ahk
if !WinExist("ahk_exe notepad.exe")
{
    MsgBox "메모장이 실행되고 있지 않습니다."
}
```

여기서 `!`는 **NOT**의 의미이다.

```text
WinExist()
    ↓
창이 존재하는가?

!WinExist()
    ↓
창이 존재하지 않는가?
```

---

# 24. 프로그램 창 앞으로 가져오기

`WinActivate`는 원하는 프로그램 창을 활성화하여 화면 앞으로 가져온다.

```ahk
WinActivate "ahk_exe notepad.exe"
```

예:

```ahk
F1::
{
    WinActivate "ahk_exe notepad.exe"
}
```

F1을 누르면 실행 중인 메모장이 활성화된다.

---

# 25. WinExist와 WinActivate 함께 사용하기

프로그램이 실행 중인지 확인한 다음 실행 중이라면 앞으로 가져오도록 만들어보자.

```ahk
F1::
{
    if WinExist("ahk_exe notepad.exe")
    {
        WinActivate "ahk_exe notepad.exe"
    }
    else
    {
        MsgBox "메모장이 실행되고 있지 않습니다."
    }
}
```

동작 과정:

```text
F1
 ↓
메모장이 실행 중인가?
 ↓
┌───────────────┐
│               │
YES             NO
│               │
↓               ↓
메모장 활성화   안내 메시지
```

이 코드는 자동화에서 매우 자주 사용하는 기본 구조이다.

---

# 26. 조금 더 발전시키기

메모장이 실행되고 있지 않다면 메시지만 출력하지 않고 직접 실행하도록 만들 수도 있다.

```ahk
F1::
{
    if WinExist("ahk_exe notepad.exe")
    {
        WinActivate "ahk_exe notepad.exe"
    }
    else
    {
        Run "notepad.exe"
    }
}
```

동작 과정:

```text
F1
 ↓
메모장이 실행 중인가?
 ↓
YES ─────────→ 기존 메모장 활성화

NO
 ↓
새로운 메모장 실행
```

이렇게 하면 사용자가 프로그램이 실행되어 있는지를 직접 확인할 필요가 없다.

---

# 27. 종합 실습

다음 프로그램을 만들어보자.

## 요구사항

F2를 누르면 다음 작업을 수행한다.

1. 메모장이 실행 중인지 확인한다.
2. 실행 중이라면 기존 메모장을 활성화한다.
3. 실행 중이지 않다면 메모장을 실행한다.
4. 잠시 기다린다.
5. 다음 문장을 입력한다.

```text
AutoHotkey 자동화 수업입니다.
```

ESC를 누르면 프로그램을 종료한다.

## 예제 코드

```ahk
#Requires AutoHotkey v2.0

F2::
{
    if WinExist("ahk_exe notepad.exe")
    {
        WinActivate "ahk_exe notepad.exe"
    }
    else
    {
        Run "notepad.exe"
        Sleep 1000
    }

    SendText "AutoHotkey 자동화 수업입니다."
}

Esc::
{
    ExitApp
}
```

---

# 28. 이번 시간 핵심 정리

이번 시간에 배운 주요 기능은 다음과 같다.

| 기능 | AutoHotkey |
|---|---|
| 메시지 출력 | `MsgBox` |
| 단축키 | `F1::` |
| 프로그램 종료 | `ExitApp` |
| 문자열 입력 | `SendText` |
| 키 입력 | `Send` |
| 잠시 기다리기 | `Sleep` |
| 프로그램 실행 | `Run` |
| 마우스 이동 | `MouseMove` |
| 마우스 클릭 | `Click` |
| 좌표 기준 설정 | `CoordMode` |
| 창 존재 확인 | `WinExist` |
| 창 활성화 | `WinActivate` |

---

# 29. 자동화 방법의 발전

오늘 배운 자동화 방식을 정리하면 다음과 같다.

처음에는 단순히 좌표를 사용했다.

```ahk
Click 500, 300
```

하지만 좌표 기반 자동화는 프로그램 창 위치가 바뀌면 문제가 발생한다.

따라서 조금 더 안정적인 자동화를 만들기 위해 프로그램 자체를 찾는다.

```ahk
WinActivate "ahk_exe notepad.exe"
```

그리고 Window Spy를 이용하면 프로그램 내부의 버튼과 입력창 정보도 확인할 수 있다.

```text
Button1
Edit1
ComboBox1
```

다음 단계에서는 이러한 Control 정보를 이용하여 마우스를 실제로 이동시키지 않고도 Windows 프로그램의 버튼을 직접 조작하는 방법을 학습한다.

```ahk
ControlClick
ControlSend
ControlSetText
```

이를 이용하면 단순한 마우스 매크로보다 훨씬 안정적인 Windows 자동화 프로그램을 만들 수 있다.
