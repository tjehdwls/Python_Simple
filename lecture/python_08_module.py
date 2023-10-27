    # 라이브러리, 패키지, 모듈
    # - 라이브러리 >= 패키지 >= 모듈

    # 1.라이브러리 : 여러패키지와 모듈의 묶음
    # 2. 패키지 : 특정기능과 관련된여러 모듈의 묶음
    # 3. 모듈 : 이미 작성된 프로그램(일반적으로 하나의 파일(.py)을 의미)

    # ** 모듈의 종류
    # 1. 내부모듈: python내에서 제공하는 모듈
    # 2. 외부모듈: 다른 개발자가 개발해놓은 모듈
    # 3. 사용자 정의 모듈: 직접 개발해서 사용하는 모듈

    # ** 모듈 사용방법
    # - 라이브러리 또는 모듈을 사용하기 위해서는 "import" 필요!

    # 가정: "requests"라이브러리 안에는 1000개의 모듈이있다

    # 1. import
    # ex) inport requests
    #  -> "requests" 라이브러리 전체 호출(1000개)
    #  -> requests.get()

    # 2. for ~ import
    # ex) from requests import get
    #   -> "requests" 라이브러리 내에서 "get" 모듈만 호출(1000개중 1개)
    #   -> get()

    # 3. as(Alias: 별명)
    # ex) import requests as req
    #   -> "requests" 라이브러리 전체 호출, 그리고 "req"라는 별명 붙이기
    #   -> req.get()