# 해당 URL에 접속후에 기사의 제목, 본문 날짜를 수집한다
import requests
from bs4 import BeautifulSoup
from db.news_dao import add_news

def get_news(url: str):
    result = requests.get(url)
    print(result)

    doc = BeautifulSoup(result.text, "html.parser")

    reg_date = doc.select("span.num_date")[0].get_text()
    print(f"날짜: {reg_date}")

    #  - slect() -> 결과(list type)
    title = doc.select("h3.tit_view")[0].get_text()
    print(f"제목:{title}")

    content_list = doc.select("div.article_view p")

    content = ""
    for p in content_list:
        content += p.get_text()
    print(f"본문: {content}")


# 수집한 데이터 DB에 저장
# MongoDB -> JSON = Dict Type
    data = {
        "title": title,
        "content": content,
        "data": reg_date
    }

    add_news(data)