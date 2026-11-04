
import os
import pyperclip

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


# 작성할 블로그 글
BLOG_TITLE = "자동화 테스트 제목"

BLOG_CONTENT = """안녕하세요.

오늘 작성할 블로그 본문입니다.

첫 번째 문단입니다.

두 번째 문단입니다.

감사합니다.
"""

BLOG_ID = "dimof"

BLOG_CATEGORY = "디모프 신상 업데이트"

BLOG_TAGS = [
    "첫번째태그입니다",
    "두번째태그입니다",
]


def run():

    with sync_playwright() as p:

        # 실행 중인 Chrome에 CDP 연결
        browser = p.chromium.connect_over_cdp(
            "http://127.0.0.1:9222"
        )

        # 기존 브라우저 컨텍스트 사용
        context = browser.contexts[0]

        # 기존 탭 사용
        pages = context.pages

        page = pages[0] if pages else context.new_page()

        # 네이버 접속
        page.goto("https://www.naver.com/")

        print("네이버 로그인 후 진행해주세요.")

        input("로그인 완료 후 Enter를 눌러주세요.")

        # 내 블로그 글쓰기 화면
        page.goto(
            f"https://blog.naver.com/{BLOG_ID}?Redirect=Write&"
        )

        # 블로그 메인 프레임
        main_frame = page.frame_locator(
            'iframe[name="mainFrame"]'
        )

        # 에디터 로딩 대기
        main_frame.locator(
            'iframe[title*="스마트 에디터"]'
        ).wait_for(
            state="visible",
            timeout=30000
        )

        print("글쓰기 에디터 로딩 완료")

        # 스마트에디터 내부 프레임
        editor = main_frame.frame_locator(
            'iframe[title*="스마트 에디터"]'
        )

        # 본문 입력 영역
        body = editor.locator("body")

        # visible 대신 attached 사용
        body.wait_for(
            state="attached",
            timeout=15000
        )

        # 실제 편집 가능한 상태인지 확인
        print("본문 요소 확인:", body.get_attribute("contenteditable"))

        # 사용자에게 포커스 확인 요청
        #input("브라우저에서 본문 작성 영역을 클릭하고 커서를 위치시킨 후 Enter를 누르세요.")

        # 클립보드에 본문 복사
        import pyperclip

        pyperclip.copy(BLOG_CONTENT)

        # 스마트에디터 내부 프레임
        editor = main_frame.frame_locator(
            'iframe[title*="스마트 에디터"]'
        )

        body = editor.locator("body")

        # DOM 연결 확인
        body.wait_for(
            state="attached",
            timeout=15000
        )

        # 실제 편집 가능 여부 확인
        print("contenteditable:", body.get_attribute("contenteditable"))

        # 사용자에게 실제 본문 커서 위치 확인 요청
        #input("본문 작성 영역을 직접 클릭하고 커서를 놓은 다음 Enter를 누르세요.")

        # iframe 내부에 키보드 이벤트 전달
        body.press("Control+V")

        print("본문 붙여넣기 명령 실행 완료")

        #input("본문 입력 결과를 확인하세요. 잘 입력되었으면 Enter 입력하세요")

        # 제목 입력 영역 찾기
        title_area = main_frame.get_by_role(
            "paragraph"
        ).filter(
            has_text="제목"
        )

        # 제목 영역 클릭
        title_area.click()

        # 제목 복사
        pyperclip.copy(BLOG_TITLE)

        # 제목 붙여넣기
        page.keyboard.press("Control+V")

        print("제목 입력 완료")

        #input("제목과 본문을 확인하고 Enter를 누르세요.")


        # ==================================
        # 첫 번째 발행 버튼 클릭
        # ==================================

        publish_button = main_frame.get_by_role(
            "button",
            name="발행",
            exact=True
        )

        publish_button.wait_for(
            state="visible",
            timeout=15000
        )

        publish_button.click()

        print("발행 설정 화면 진입")

        # ==================================
        # 카테고리 목록 열기
        # ==================================

        category_button = main_frame.get_by_role(
            "button",
            name="카테고리 목록 버튼"
        )

        category_button.wait_for(
            state="visible",
            timeout=15000
        )
    
        category_button.click()

        print("카테고리 목록 열기 완료")

        page.locator("iframe[name=\"mainFrame\"]").content_frame.get_by_role("button", name="디모프 신상 업데이트").click()
        print("카테고리 선택 완료")
        
        # ==================================
        # 태그 입력
        # ==================================

        tag_input = main_frame.get_by_role(
            "combobox",
            name="태그 입력 (최대 30개)"
        )

        tag_input.wait_for(
            state="visible",
            timeout=15000
        )

        for tag in BLOG_TAGS:

            tag_input.fill(tag)

            tag_input.press("Enter")

            print("태그 등록:", tag)

        # ==================================
        # 최종 발행
        # ==================================

        final_publish_button = main_frame.get_by_test_id(
            "seOnePublishBtn"
        )

        final_publish_button.wait_for(
            state="visible",
            timeout=15000
        )

        input("카테고리와 태그를 확인한 후 Enter를 누르면 최종 발행합니다.")

        final_publish_button.click()

        print("최종 발행 버튼 클릭 완료")


        # CDP 연결 브라우저 유지
        print("자동화 작업 종료")


if __name__ == "__main__":
    run()
