# TODO : 1. 스케쥴링
#        2. 리뷰 중복 체크(중복 수집X)
#        3. DB에 저장 된 데이터 Excel 다운로드
#        4. DB에 저장 된 데이터 -> 데이터 분석
#        5. DB에 저장된 데이터 -> WordCloud 시각화


from collect.collect_daum_movie_review import review_collector
# from apscheduler.schedulers.blocking import Block



from db.movie_dao import get_last_review

def main():
    print("="*100)
    print("==영화리뷰수집기==")
    print("="*100)
    movie_code = input("영화 코드>>") #169328
    print("알림: 매일12시간에 수집")

    # 중복리뷰 체크
    # 1. 리뷰 수(X)
    # - DB에 저장 된 리뷰 수(17)
    # - 현재 수집 할 리뷰 수 (20)
    # - 20-17=3 (리뷰 삭제 고려X)
    # 2. 날짜 비교
    # - Last_date = DB에 저장 된 랩 중 가장 최신 날짜 get
    # - 수집리뷰_date 비교 Last_date
    # 예시)
    # Last_date = 2023.11.2. 02:25   ->   202311270225
    # 수집리뷰_date = 2023.11.28. 02:25  -> 202311280225

    lsat_date = get_last_review()

    if lsat_date == None:
        lsat_date = 0
    else:
        lsat_date = int(lsat_date["int_regdate"])




    # scheduler = BlockingSchduler()
    # scheduler.add_job(review_collector,
    #                   args=[movie_code],
    #                   trigger-"cron",
    #                   hour="12",
    #                   minute="0")
    #
    # scheduler.start()

    review_collector(movie_code, lsat_date) # 삭제

if __name__ == "__main__":
    main()
