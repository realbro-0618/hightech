# AutoHotkey v2 - ImageSearch 이미지 찾기 수업자료

## 1. 오늘 배울 내용

지난 시간에는 AutoHotkey를 이용해서

- 키보드 입력
- 클립보드 붙여넣기
- 창 활성화
- 마우스 클릭

등을 배웠습니다.

이번 시간에는 화면에 보이는 **특정 이미지를 찾아서 자동화하는 방법**을 배웁니다.

오늘의 목표는 다음과 같습니다.

1. 전체 화면에서 이미지 찾기
2. 찾은 이미지 위치로 마우스 이동하기
3. 특정 영역에서만 이미지 찾기
4. 이미지 검색 범위를 줄여 속도 개선하기
5. 이미지 허용 오차 조정하기
6. 실무에서 ImageSearch를 안정적으로 사용하는 방법 익히기

---

# 2. ImageSearch란?

`ImageSearch`는 화면에 특정 이미지가 있는지 찾아주는 AutoHotkey 기능입니다.

예를 들어 다음과 같은 버튼이 있다고 생각해봅시다.

```text
[ 로그인 ]
```

버튼 이미지를 캡처해서

```text
login.png
```

로 저장합니다.

AutoHotkey는 화면을 검색해서 `login.png`와 같은 이미지가 있는 위치를 찾을 수 있습니다.

기본 구조는 다음과 같습니다.

```ahk
ImageSearch(&x, &y, X1, Y1, X2, Y2, "이미지파일")
```

각 값의 의미는 다음과 같습니다.

| 값 | 의미 |
|---|---|
| `&x` | 찾은 이미지의 X 좌표 |
| `&y` | 찾은 이미지의 Y 좌표 |
| `X1`, `Y1` | 검색 시작 위치 |
| `X2`, `Y2` | 검색 끝 위치 |
| `"이미지파일"` | 찾을 이미지 |

---

# 3. 실습 준비

먼저 AutoHotkey 파일과 이미지 파일을 같은 폴더에 준비합니다.

예:

```text
AHK_ImageSearch/
│
├─ image_search.ahk
└─ target.png
```

`target.png`는 화면에서 찾고 싶은 버튼이나 아이콘을 캡처한 이미지입니다.

---

# 4. 화면 좌표 기준 설정하기

ImageSearch를 사용할 때 좌표 기준을 명확하게 설정하는 것이 중요합니다.

```ahk
CoordMode "Pixel", "Screen"
CoordMode "Mouse", "Screen"
```

`Pixel`은 이미지 검색 좌표를 의미합니다.

```ahk
CoordMode "Pixel", "Screen"
```

은 이미지 검색 좌표를 **전체 화면 기준**으로 사용한다는 뜻입니다.

마우스도 동일하게 설정합니다.

```ahk
CoordMode "Mouse", "Screen"
```

따라서 기본 코드는 다음과 같이 시작합니다.

```ahk
#Requires AutoHotkey v2.0

CoordMode "Pixel", "Screen"
CoordMode "Mouse", "Screen"
```

---

# 5. 전체 화면에서 이미지 찾기

전체 화면의 크기는 다음 값을 사용할 수 있습니다.

```ahk
A_ScreenWidth
A_ScreenHeight
```

예를 들어 모니터 해상도가

```text
1920 × 1080
```

이라면 대략 다음과 같습니다.

```text
A_ScreenWidth  = 1920
A_ScreenHeight = 1080
```

전체 화면을 검색하는 코드는 다음과 같습니다.

```ahk
#Requires AutoHotkey v2.0

CoordMode "Pixel", "Screen"
CoordMode "Mouse", "Screen"

imagePath := A_ScriptDir "\target.png"

F2::
{
    if ImageSearch(
        &x,
        &y,
        0,
        0,
        A_ScreenWidth,
        A_ScreenHeight,
        imagePath
    )
    {
        MsgBox "이미지를 찾았습니다."
    }
    else
    {
        MsgBox "이미지를 찾지 못했습니다."
    }
}
```

---

# 6. 찾은 이미지 위치로 마우스 이동하기

`ImageSearch`가 성공하면 `x`, `y`에 이미지 위치가 저장됩니다.

따라서 다음처럼 사용할 수 있습니다.

```ahk
MouseMove x, y
```

전체 코드는 다음과 같습니다.

```ahk
#Requires AutoHotkey v2.0

CoordMode "Pixel", "Screen"
CoordMode "Mouse", "Screen"

imagePath := A_ScriptDir "\target.png"

F2::
{
    if ImageSearch(
        &x,
        &y,
        0,
        0,
        A_ScreenWidth,
        A_ScreenHeight,
        imagePath
    )
    {
        MouseMove x, y
    }
    else
    {
        MsgBox "이미지를 찾지 못했습니다."
    }
}
```

---

# 7. ImageSearch가 반환하는 위치

중요한 점이 있습니다.

`ImageSearch`에서 찾은

```text
x, y
```

좌표는 이미지의 **왼쪽 위 모서리**입니다.

예를 들어 다음과 같은 버튼을 찾았다고 생각해봅시다.

```text
(x, y)
  ↓
  ┌─────────────────┐
  │     로그인      │
  └─────────────────┘
```

따라서 정확히 버튼 중앙으로 마우스를 이동하고 싶다면 약간의 값을 더해줍니다.

예:

```ahk
MouseMove x + 30, y + 15
```

또는 클릭:

```ahk
Click x + 30, y + 15
```

---

# 8. 첫 번째 실습

## 목표

F2를 누르면 전체 화면에서 `target.png`를 찾습니다.

찾았다면 이미지 위로 마우스를 이동합니다.

```ahk
#Requires AutoHotkey v2.0

CoordMode "Pixel", "Screen"
CoordMode "Mouse", "Screen"

imagePath := A_ScriptDir "\target.png"

F2::
{
    if ImageSearch(
        &x,
        &y,
        0,
        0,
        A_ScreenWidth,
        A_ScreenHeight,
        imagePath
    )
    {
        MouseMove x + 10, y + 10
    }
    else
    {
        MsgBox "이미지를 찾지 못했습니다."
    }
}

Esc::
{
    ExitApp
}
```

---

# 9. 전체 화면 검색의 문제점

전체 화면을 검색하면 편리합니다.

하지만 단점이 있습니다.

```text
1920 × 1080 화면
```

이라면 AutoHotkey가 매우 넓은 영역을 검사해야 합니다.

특히

- 4K 모니터
- 듀얼 모니터
- 반복 검색
- 여러 이미지를 연속으로 검색

하는 경우에는 검색 비용이 증가합니다.

따라서 실무에서는 가능하면 **이미지가 나타날 것으로 예상되는 영역만 검색**하는 것이 좋습니다.

---

# 10. 특정 영역에서만 이미지 찾기

예를 들어 화면 오른쪽 위에 버튼이 나타난다는 것을 알고 있다고 가정합니다.

검색 범위를 다음처럼 지정할 수 있습니다.

```text
X1 = 1200
Y1 = 0

X2 = 1920
Y2 = 500
```

코드는 다음과 같습니다.

```ahk
ImageSearch(
    &x,
    &y,
    1200,
    0,
    1920,
    500,
    imagePath
)
```

---

# 11. 특정 영역 ImageSearch 예제

```ahk
#Requires AutoHotkey v2.0

CoordMode "Pixel", "Screen"
CoordMode "Mouse", "Screen"

imagePath := A_ScriptDir "\target.png"

F3::
{
    if ImageSearch(
        &x,
        &y,
        1200,
        0,
        A_ScreenWidth,
        500,
        imagePath
    )
    {
        MouseMove x + 10, y + 10
    }
    else
    {
        MsgBox "지정된 영역에서 이미지를 찾지 못했습니다."
    }
}
```

---

# 12. 검색 영역을 줄이면 왜 빨라지는가?

전체 화면:

```text
┌──────────────────────────────┐
│                              │
│       전체 영역 검색        │
│                              │
│                              │
│                              │
└──────────────────────────────┘
```

특정 영역:

```text
┌──────────────────────────────┐
│                  ┌─────────┐ │
│                  │ 검색    │ │
│                  │ 영역    │ │
│                  └─────────┘ │
│                              │
└──────────────────────────────┘
```

검색해야 하는 픽셀 수가 줄어들기 때문에 일반적으로 더 빠르게 찾을 수 있습니다.

따라서 실무에서는

> 이미지 자체를 바꾸기 전에 먼저 검색 범위를 줄일 수 있는지 확인한다.

는 습관이 중요합니다.

---

# 13. 특정 프로그램 영역만 검색하기

실무에서는 전체 화면의 좌표를 직접 입력하기보다 특정 창의 위치를 구해서 검색하는 방법도 사용할 수 있습니다.

예를 들어 Chrome 위치를 가져옵니다.

```ahk
WinGetPos &winX, &winY, &winW, &winH, "ahk_exe chrome.exe"
```

그러면

```text
winX = 창의 X 위치
winY = 창의 Y 위치
winW = 창의 너비
winH = 창의 높이
```

를 얻을 수 있습니다.

---

# 14. Chrome 영역에서만 이미지 찾기

```ahk
#Requires AutoHotkey v2.0

CoordMode "Pixel", "Screen"
CoordMode "Mouse", "Screen"

imagePath := A_ScriptDir "\target.png"

F4::
{
    if !WinExist("ahk_exe chrome.exe")
    {
        MsgBox "Chrome이 실행되고 있지 않습니다."
        return
    }

    WinGetPos &winX, &winY, &winW, &winH, "ahk_exe chrome.exe"

    if ImageSearch(
        &x,
        &y,
        winX,
        winY,
        winX + winW,
        winY + winH,
        imagePath
    )
    {
        MouseMove x + 10, y + 10
    }
    else
    {
        MsgBox "Chrome 화면에서 이미지를 찾지 못했습니다."
    }
}
```

이 방식은 실무에서 상당히 유용합니다.

---

# 15. 이미지 정확도 조절하기

실제 화면에서는 이미지가 항상 완전히 똑같지 않을 수 있습니다.

예를 들어

- 밝기 차이
- 안티앨리어싱
- 화면 색상 차이
- 프로그램 렌더링 차이

등이 발생할 수 있습니다.

이때 사용할 수 있는 것이 `*n` 옵션입니다.

예:

```ahk
"*30 " imagePath
```

전체 코드는 다음과 같습니다.

```ahk
if ImageSearch(
    &x,
    &y,
    0,
    0,
    A_ScreenWidth,
    A_ScreenHeight,
    "*30 " imagePath
)
{
    MouseMove x, y
}
```

---

# 16. `*n` 옵션의 의미

예를 들어:

```text
*0
*10
*30
*50
*100
```

처럼 사용할 수 있습니다.

숫자가 커질수록 이미지의 색상 차이를 더 많이 허용합니다.

즉,

```text
*0
```

은 매우 엄격하게 비교합니다.

```text
*30
```

은 어느 정도 색상 차이를 허용합니다.

```text
*80
```

은 더 큰 색상 차이를 허용합니다.

---

# 17. 중요한 오해

`*n` 값은 **검색 속도를 직접 조절하는 옵션이 아닙니다.**

즉 다음 설명은 정확하지 않습니다.

```text
정확도를 낮추면 무조건 검색 속도가 빨라진다.
```

`*n`의 핵심 역할은

> 이미지의 색상 차이를 어느 정도 허용할 것인가

입니다.

검색 속도를 개선하는 가장 효과적인 방법은 보통 다음입니다.

```text
1. 검색 영역 줄이기
2. 검색할 이미지를 작게 만들기
3. 불필요한 반복 검색 줄이기
```

---

# 18. 허용 오차가 너무 높으면?

예를 들어:

```ahk
"*100 " imagePath
```

처럼 값을 너무 높이면 비슷한 색상의 다른 이미지를 잘못 찾을 가능성이 높아집니다.

따라서 일반적으로는 작은 값부터 테스트합니다.

예:

```text
*10
 ↓
*20
 ↓
*30
 ↓
*40
```

정확하게 찾을 수 있는 **가장 낮은 허용 오차 값**을 사용하는 것이 좋습니다.

---

# 19. 실무 팁 1 - 이미지를 작게 캡처하기

다음과 같은 버튼이 있다고 가정합니다.

```text
┌───────────────────────────┐
│         주문하기          │
└───────────────────────────┘
```

전체 버튼을 모두 캡처할 필요는 없습니다.

특징적인 부분만 잘라서 사용할 수 있습니다.

예:

```text
주문하기
```

또는 버튼의 특징적인 아이콘만 사용할 수도 있습니다.

이미지가 작아지면 비교할 픽셀이 줄어들기 때문에 검색 부담도 줄어듭니다.

---

# 20. 실무 팁 2 - 너무 작은 이미지도 문제

이미지를 무조건 작게 만드는 것이 좋은 것은 아닙니다.

예를 들어 다음처럼 단순한 아이콘:

```text
X
```

만 캡처하면 화면의 다른 `X`와 구분하기 어려울 수 있습니다.

따라서 좋은 검색 이미지는

```text
작으면서
+
고유한 특징이 있는 이미지
```

여야 합니다.

---

# 21. 좋은 이미지와 좋지 않은 이미지

## 좋지 않은 예

```text
[ 확인 ]
```

화면에 `확인` 버튼이 여러 개 있는 경우 잘못 찾을 수 있습니다.

## 좋은 예

```text
[ ✓ 주문 완료 확인 ]
```

처럼 주변에 고유한 특징이 있는 영역을 포함시키면 더 안정적입니다.

---

# 22. 실무 팁 3 - 화면 배율 확인

ImageSearch에서 자주 발생하는 문제 중 하나입니다.

예를 들어 캡처 당시 브라우저 확대 비율이

```text
100%
```

였는데 실행할 때

```text
125%
```

라면 이미지 크기가 달라집니다.

ImageSearch는 이런 경우 실패할 가능성이 높습니다.

따라서 자동화 환경을 가능하면 고정합니다.

예:

```text
Windows 배율 : 100%
Chrome 확대 : 100%
프로그램 창 크기 : 일정
```

---

# 23. 실무 팁 4 - 마우스 Hover 효과 주의

어떤 버튼은 마우스를 올려놓으면 색상이 변합니다.

평상시:

```text
[ 로그인 ]
```

마우스를 올렸을 때:

```text
[ 로그인 ]
  ↑ 색상 변경
```

이 경우 캡처 이미지와 실제 화면 이미지가 달라질 수 있습니다.

따라서 이미지를 캡처할 때는

- 마우스를 버튼에서 치운 상태
- 실제 자동화가 실행될 때와 같은 상태

에서 캡처하는 것이 좋습니다.

---

# 24. 실무 팁 5 - 한 번만 찾지 말고 기다리기

웹사이트나 프로그램은 버튼이 즉시 나타나지 않을 수 있습니다.

잘못된 방법:

```ahk
if ImageSearch(...)
{
    Click x, y
}
else
{
    MsgBox "실패"
}
```

버튼이 0.5초 늦게 나타나도 바로 실패합니다.

실무에서는 일정 시간 동안 반복해서 찾는 방법을 많이 사용합니다.

---

# 25. 이미지가 나타날 때까지 기다리기

```ahk
WaitImage(imagePath, timeout := 5000)
{
    startTime := A_TickCount

    while A_TickCount - startTime < timeout
    {
        if ImageSearch(
            &x,
            &y,
            0,
            0,
            A_ScreenWidth,
            A_ScreenHeight,
            imagePath
        )
        {
            return {x: x, y: y}
        }

        Sleep 100
    }

    return false
}
```

사용 방법:

```ahk
F5::
{
    result := WaitImage(A_ScriptDir "\target.png")

    if result
    {
        MouseMove result.x, result.y
    }
    else
    {
        MsgBox "5초 동안 이미지를 찾지 못했습니다."
    }
}
```

---

# 26. 왜 반복 검색에 Sleep을 넣는가?

다음처럼 작성하면:

```ahk
while true
{
    ImageSearch(...)
}
```

컴퓨터가 계속 매우 빠른 속도로 이미지를 검색합니다.

CPU 사용량이 높아질 수 있습니다.

따라서 다음처럼 약간 기다리는 것이 좋습니다.

```ahk
Sleep 100
```

또는

```ahk
Sleep 200
```

---

# 27. 실무 팁 6 - 찾았다고 바로 클릭하지 않기

실제 자동화에서는 이미지가 발견되었다고 해서 바로 클릭하지 않는 경우도 있습니다.

예:

```text
이미지 발견
   ↓
마우스 이동
   ↓
조금 기다림
   ↓
클릭
```

코드:

```ahk
if ImageSearch(
    &x,
    &y,
    0,
    0,
    A_ScreenWidth,
    A_ScreenHeight,
    imagePath
)
{
    MouseMove x + 20, y + 10

    Sleep 200

    Click
}
```

---

# 28. 실무 팁 7 - 클릭 후 결과 확인하기

더 좋은 자동화는

```text
버튼 찾기
   ↓
클릭
   ↓
다음 화면이 나왔는지 확인
```

까지 진행합니다.

예:

```text
[ 로그인 버튼 ]
      ↓
   클릭
      ↓
[ 로그인 완료 이미지 ] 검색
```

즉 **행동 후 결과를 확인하는 방식**으로 자동화를 구성합니다.

---

# 29. 실무 예제 - 버튼 찾고 클릭 후 결과 확인

```ahk
#Requires AutoHotkey v2.0

CoordMode "Pixel", "Screen"
CoordMode "Mouse", "Screen"

buttonImage := A_ScriptDir "\button.png"
successImage := A_ScriptDir "\success.png"

F6::
{
    if ImageSearch(
        &x,
        &y,
        0,
        0,
        A_ScreenWidth,
        A_ScreenHeight,
        buttonImage
    )
    {
        MouseMove x + 20, y + 10
        Click

        Sleep 500

        if ImageSearch(
            &successX,
            &successY,
            0,
            0,
            A_ScreenWidth,
            A_ScreenHeight,
            successImage
        )
        {
            MsgBox "작업이 정상적으로 완료되었습니다."
        }
        else
        {
            MsgBox "클릭은 했지만 결과를 확인하지 못했습니다."
        }
    }
    else
    {
        MsgBox "버튼을 찾지 못했습니다."
    }
}
```

---

# 30. 실무 팁 8 - 여러 상태 이미지 준비하기

프로그램의 버튼 모습이 상황마다 달라질 수 있습니다.

예:

```text
button.png
button_hover.png
button_selected.png
```

여러 이미지를 준비해 순서대로 검색하는 방법도 있습니다.

```ahk
images := [
    A_ScriptDir "\button.png",
    A_ScriptDir "\button_hover.png",
    A_ScriptDir "\button_selected.png"
]
```

그리고 하나씩 검사합니다.

```ahk
for imagePath in images
{
    if ImageSearch(
        &x,
        &y,
        0,
        0,
        A_ScreenWidth,
        A_ScreenHeight,
        imagePath
    )
    {
        MouseMove x, y
        break
    }
}
```

---

# 31. 실무 팁 9 - 가능하면 ImageSearch보다 먼저 다른 방법 검토

ImageSearch는 매우 유용하지만 항상 가장 좋은 방법은 아닙니다.

Windows 프로그램:

```text
ControlClick
ControlSend
ControlSetText
```

웹사이트:

```text
Playwright
DOM Selector
```

같은 방법이 가능한 경우에는 이미지 검색보다 안정적인 경우가 많습니다.

따라서 자동화 방법의 우선순위를 다음처럼 생각할 수 있습니다.

```text
1. 프로그램의 실제 요소를 직접 제어할 수 있는가?
        ↓
2. ControlClick / Playwright 등을 사용

안 된다면
        ↓
3. ImageSearch

그것도 어렵다면
        ↓
4. 고정 좌표 Click
```

---

# 32. ImageSearch를 사용하기 좋은 상황

다음과 같은 경우 ImageSearch가 유용합니다.

- Window Spy에서 Control을 찾을 수 없는 프로그램
- 그래픽으로 만들어진 버튼
- 게임 형태의 UI
- 원격 데스크톱 화면
- 이미지 기반 프로그램
- 오래된 Windows 프로그램
- 브라우저 안에서 간단한 화면 상태를 확인할 때

---

# 33. 실무용 이미지 검색 함수 만들기

매번 ImageSearch 코드를 반복해서 작성하면 코드가 길어집니다.

따라서 함수로 만들 수 있습니다.

```ahk
FindImage(imagePath, x1 := 0, y1 := 0, x2 := 0, y2 := 0, variation := 20)
{
    if x2 = 0
        x2 := A_ScreenWidth

    if y2 = 0
        y2 := A_ScreenHeight

    option := "*" variation " " imagePath

    if ImageSearch(
        &x,
        &y,
        x1,
        y1,
        x2,
        y2,
        option
    )
    {
        return {x: x, y: y}
    }

    return false
}
```

사용 방법:

```ahk
F7::
{
    result := FindImage(
        A_ScriptDir "\target.png",
        1000,
        0,
        A_ScreenWidth,
        500,
        30
    )

    if result
    {
        MouseMove result.x, result.y
    }
    else
    {
        MsgBox "이미지를 찾지 못했습니다."
    }
}
```

---

# 34. 실무용 기다리기 함수

좀 더 발전시키면 이미지가 나타날 때까지 기다리는 함수를 만들 수 있습니다.

```ahk
WaitForImage(
    imagePath,
    timeout := 5000,
    variation := 20,
    x1 := 0,
    y1 := 0,
    x2 := 0,
    y2 := 0
)
{
    if x2 = 0
        x2 := A_ScreenWidth

    if y2 = 0
        y2 := A_ScreenHeight

    startTime := A_TickCount

    option := "*" variation " " imagePath

    while A_TickCount - startTime < timeout
    {
        if ImageSearch(
            &x,
            &y,
            x1,
            y1,
            x2,
            y2,
            option
        )
        {
            return {x: x, y: y}
        }

        Sleep 100
    }

    return false
}
```

사용:

```ahk
F8::
{
    result := WaitForImage(
        A_ScriptDir "\target.png",
        5000,
        30
    )

    if result
    {
        MouseMove result.x + 10, result.y + 10
    }
    else
    {
        MsgBox "시간 초과"
    }
}
```

---

# 35. 수업 실습 1

## 문제

화면 전체에서 `target.png`를 찾아서 마우스를 이동시키세요.

조건:

```text
F2 : 이미지 검색
ESC : 프로그램 종료
```

힌트:

```ahk
ImageSearch(...)
MouseMove(...)
```

---

# 36. 수업 실습 2

## 문제

화면 오른쪽 위 영역에서만 이미지를 검색하세요.

검색 영역:

```text
X : 1000 ~ 화면 끝
Y : 0 ~ 500
```

찾으면 마우스를 이동시킵니다.

---

# 37. 수업 실습 3

## 문제

`*30` 허용 오차를 적용해보세요.

그리고 다음 값을 각각 테스트합니다.

```text
*0
*10
*30
*50
*80
```

다음 내용을 관찰합니다.

- 언제 검색에 성공하는가?
- 너무 높은 값을 사용했을 때 잘못된 이미지를 찾는가?
- 화면 상태에 따라 결과가 어떻게 달라지는가?

---

# 38. 수업 실습 4

다음 함수를 이용해서

```text
최대 5초 동안
0.1초마다
target.png를 검색
```

하도록 만들어보세요.

이미지를 찾으면 마우스를 이동합니다.

찾지 못하면:

```text
이미지를 찾지 못했습니다.
```

라는 메시지를 출력합니다.

---

# 39. 이미지 자동화에서 가장 중요한 개념

ImageSearch 자동화를 다음처럼 만들면 불안정합니다.

```text
이미지 검색
 ↓
없음
 ↓
바로 실패
```

실무에서는 다음처럼 구성하는 것이 좋습니다.

```text
프로그램 실행
     ↓
화면 나타날 때까지 대기
     ↓
특정 영역 검색
     ↓
이미지 발견
     ↓
클릭
     ↓
결과 이미지 확인
     ↓
다음 작업
```

즉 단순히

```text
이미지를 찾는다
```

가 아니라

```text
화면 상태를 판단한다
```

라는 개념으로 생각해야 합니다.

---

# 40. 오늘의 핵심 정리

### 전체 화면 검색

```ahk
ImageSearch(
    &x,
    &y,
    0,
    0,
    A_ScreenWidth,
    A_ScreenHeight,
    imagePath
)
```

### 특정 영역 검색

```ahk
ImageSearch(
    &x,
    &y,
    1000,
    0,
    A_ScreenWidth,
    500,
    imagePath
)
```

### 찾은 위치로 이동

```ahk
MouseMove x, y
```

### 허용 오차 적용

```ahk
"*30 " imagePath
```

---

# 41. 실무에서 기억해야 할 7가지

```text
1. 전체 화면보다는 검색 영역을 줄인다.

2. 검색 이미지는 작고 특징적으로 만든다.

3. *n은 속도 옵션이 아니라 색상 허용 오차다.

4. Windows 배율과 브라우저 확대 비율을 일정하게 유지한다.

5. 한 번 검색하고 실패하지 말고 일정 시간 반복 검색한다.

6. 클릭한 뒤 결과 화면까지 확인한다.

7. ControlClick이나 Playwright처럼 더 안정적인 방법이 있다면
   ImageSearch보다 먼저 검토한다.
```

---

# 다음 시간

이번 시간에는 화면에서 특정 이미지를 찾아 자동으로 행동하는 방법을 배웠습니다.

다음 단계에서는 다음과 같은 자동화를 만들 수 있습니다.

```text
이미지 A가 나타나면
        ↓
버튼 클릭

이미지 B가 나타나면
        ↓
오류 처리

이미지 C가 나타나면
        ↓
작업 완료
```

이를 이용하면 단순한 매크로를 넘어

**화면의 상태를 판단하면서 동작하는 자동화 프로그램**

을 만들 수 있습니다.
