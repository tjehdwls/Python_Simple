# SELENIUM

# pip install selenium
# pip install webdriver_manager

# ** Selenium을 사용하는 이유?
# - Requests는 현재 URL의 정적 페이지 소스코드만 수집 가능
#   -> "더보기" 버튼 클리과 같은 동적인 동작 불가
# - Selenium은 전용 브라우저를 사용해서 동작
#   -> 따라서 chrome 드라이버와 같이 브라우저 설정이 반드시 필요
#   tmi) Selenium은 처음에 웹브라우저 테스트 용으로 개발

# ** Selenium

import math
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 2. url접속
url = "https://movie.daum.net/moviedb/grade?movieId=165591"
driver.get(url)
time.sleep(2)

# 3. 페이지 전체코드 가져오기
doc_html = driver.page_source

# 4. Selenium -> BeautifulSoup
doc = BeautifulSoup(doc_html, "html.parser")

# 5. 영화제목 수집
movie_title = doc.select("span.txt_tit")[0].get_text()
print(f"영화 제목: {movie_title}")
print("="*100)

# 6. 전체 리뷰 출력 "평점더보기" 클릭
# - 다음 영화 최초페이지 -> 10개
# - "평점 더보기" 클릭 -> 30개
# - "평점 더보기" 몇번 클릭? -> 전체 리뷰 출력

# 전체리뷰 187
#수식올림((187-10)/30)

# 6-1. 전체 리뷰 수집
total_review_cnt = doc.select("span.txt_netizen")[0].get_text()

# 6-2. 전체 리뷰에서 숫자만 추출
# - 문자열 슬라이싱
# (187명) 012345 [1:-2](동적코딩)
# print(total_review_cnt[1:-2])
# - 정규식 -> 숫자만 추출
num_review = int(re.sub(r"[^~0-9]", "", total_review_cnt))

# 6-3 평점 더보기 클릭 회숫 계산
click_cnt = math.ceil((num_review - 10) / 30)

# 7. Selenium을 통해서 평점 더보기 클릭
for i in range(click_cnt):
    driver.find_element(By.CLASS_NAME, "link_fold").click()
    time.sleep(1)

# 8. 전체소스코드 가져오기
doc_html = driver.page_source
doc = BeautifulSoup(doc_html, "html.parser")
review_list = doc.select("")