

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
