# 카테고리별 실시간 다음 뉴스 수집기 ver 1.0
# - 작성자: eoiksy
# - 작성일자: 2023.11.08
# _ 라이브러리: requests, beutifulsoup4, pymongo
# - 프로세스(비지니스 로직)
#   1) 수집가능한 뉴스 카테고리 출력
#   2) 사용자로부터 원하는 카테고리 입력
#   3) 입력 된 카테고리 다음 실시간 뉴스 수집(제목, 본문 날짜)
#   4) 수집 된 뉴스 데이터 데이터베이스에 저장

# 도메인 지식: 내가 개잘하고자 하는 분야의 전문지식
# ex) 은행 프로그램 -> 도메인 지식(은행로직)
# ex) 인사 프로그램 -> 도메인 지식(노동법)
# ex) 회계 프로그램 -> 도메인지식(회계)


import requests
from bs4 import BeautifulSoup
from service1.service_news import get_news


news_category = {
    "사회" : "society",
    "정치" : "politics",
    "경제" : "economic",
    "국제" : "foreign",
    "문화" : "culture",
    "연예" : "entertain",
    "스포츠" : "sports",
    "IT" : "digital",
}

print("="*150)
print("카테고리목록")
for i, item in enumerate(news_category):
    print(f" = {i+1}.{item}")
print("수집할 뉴스의 카테고리를 입력하시오.")

while True:
    news = input(">카테고리: ")
    if news  in list(news_category):
        break
    else:
        print("올바른 카테고리를 입력하시오.")



a = 0  # 수집된 전체 기사 수
page = 1  # 시작페이지 1로 고정

while True:
    url = f"https://news.daum.net/breakingnews/{news_category[news]}?page={page}"
    result = requests.get(url)

    if result.status_code == 200:
        print("URL접속성공")
        doc = BeautifulSoup(result.text, "html.parser")
        url_list = doc.select("ul.list_news2 a.link_txt")

        if len(url_list) == 0:
            break

        for url in url_list:
            a += 1
            print(f"{a}", "=" * 150)
            print(f"번호:{a}")
            get_news(url["href"])
    else:
        print("잘못된 URL입니다. 다시한번 확인해주세요.")
    page += 1
