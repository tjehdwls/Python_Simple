# 다음 실시간 뉴스 목록(15) 기사 [ 제목 , 본문, 날짜] 수집기

import requests
from bs4 import BeautifulSoup
from service1.service_news import get_news

url = "https://news.daum.net/breakingnews/digital"
result = requests.get(url)

a = 0  # 수집된 전체 기사 수

if result.status_code == 200:
    print("URL접속성공")
    doc = BeautifulSoup(result.text, "html.parser")
    url_list = doc.select("ul.list_news2 a.link_txt")

    for url in url_list:
        a += 1
        print(f"{a}", "="*150)
        print(f"번호:{a}")
        get_news(url["href"])
else:
    print("잘못된 URL입니다. 다시한번 확인해주세요.")

