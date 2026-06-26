from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # 요소를 찾기 위한 모듈 추가
from selenium.webdriver.common.keys import Keys  # 키보드 입력을 위한 모듈 추가
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd



def click_xpath(xpath,delay):
    time.sleep(delay)
    btn = driver.find_element(By.XPATH, xpath)
    btn.click()
    return btn
    
def click_css(css,delay):
    time.sleep(delay)
    btn = driver.find_element(By.CSS_SELECTOR, css)
    btn.click()
    return btn

# 1. 크롬 드라이버 자동 설치 및 서비스 설정
service = Service(ChromeDriverManager().install())

# 2. 브라우저 열기
driver = webdriver.Chrome(service=service)

search_word = "삼성전자"

url = f"https://search.naver.com/search.naver?ssc=tab.news.all&query={search_word}&sm=tab_opt&sort=1&photo=0&field=0&pd=-1&ds=2026.06.26&de=2026.06.26&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0&office_category=0&service_area=0"

print(url)

driver.get(url)

time.sleep(2)

for i in range(5):

    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)



# 여러 class를 동시에 가진 뉴스 기사 영역 선택
articles = driver.find_elements(
    By.CSS_SELECTOR,
    ".sds-comps-vertical-layout.sds-comps-full-layout.U7hwzP3DLKcLg5Q7"
)

print(f"수집된 기사 개수: {len(articles)}")

news_data = list()

for idx, article in enumerate(articles, start=1):
    temp_list = list()
    
    print("=" * 50)
    print(f"{idx}번째 기사")
    
    temp_list.append(idx)
    
    article_list = article.text.replace('네이버뉴스\n','').split('\n')
    
    list_index = 0
    
    print(article_list[list_index])  #신문사
    temp_list.append(article_list[list_index])
    list_index += 1
    
    if '전' in article_list[1]:
        print(article_list[1])
        temp_list.append(article_list[1])
        list_index += 1
    elif '전' in article_list[2]:
        print(article_list[2]) 
        temp_list.append(article_list[2])
        list_index += 2
            
    print(article_list[list_index])
    temp_list.append(article_list[list_index])
    list_index += 1
    
    print(article_list[list_index])
    temp_list.append(article_list[list_index])
    
    news_data.append(temp_list)

# 컬럼명 지정
columns = ["순번", "신문사", "발행시각", "제목", "요약"]

# 데이터프레임 생성
df = pd.DataFrame(news_data, columns=columns)

# 엑셀로 저장
df.to_excel("naver_news_sample.xlsx", index=False)

print("엑셀 저장 완료: naver_news_sample.xlsx")


















