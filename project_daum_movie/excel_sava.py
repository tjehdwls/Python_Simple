# DB에 저장되어 있는 수집 데이터를 엑셀로 저장
# python(dict, list 컬렉션)
#
# pandas의 dataframe
#
# file(CSV, Excel)



import pandas as pd

from db.movie_dao import get_reviews
from datetime import datetime

reviews = get_reviews()
for item in reviews:
    print(item)

df_save = pd.DataFrame(reviews)
print(df_save)

now = datetime.now().strftime("%Y%m%d")
df_save.to_excel(f"./review_{now}.xlsx", index=False)