# TODO : 1. 스케쥴링
#        2. 리뷰 중복 체크(중복 수집X)
#        3. DB에 저장 된 데이터 Excel 다운로드
#        4. DB에 저장 된 데이터 -> 데이터 분석
#        5. DB에 저장된 데이터 -> WordCloud 시각화


from collect.collect_daum_moive_review import review_collector


def main():
    print("="*100)
    print("==영화리뷰수집기==")
    print("="*100)
    movie_code = input("영화 코드>>") #169328
    print("알림: 매일12시간에 수집")
    review_collector(movie_code)

if __name__ == "__main__":
    main()
