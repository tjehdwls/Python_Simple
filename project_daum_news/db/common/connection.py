# 파일시스템: 폴더 또는 디렉토리로 데이터를 저장하는 방법
# 데이터 베이스: 데이터를 효율적으로 저자아고 관리해주는 시스템

# 데이터베이스 관리 시스템(DBMS): 데이터베이스 제품

# ** DBMS종류(상호보안적)
#  1. 관계형 데이터베이스(RDB) : 전통적
#   - ORACLS
#   - MySQL
#   - MariaDB

#  2. NoSQL: 새로운(빅데이터)
#   - MongoDB
#   - Redis

# ** DBMS 프로세스
#   - DB에 ID와 PW저장
#   Pycharm(Python) --------------------------------------------------- DB(MongoDB)
#   1. Pycharm과 DB Connection 맺기
#    - IP: 컴퓨터의 주소
#    - PORT: 컴퓨터 내에 프로그램의 위치
#    - ID, PW
#   2. SQL을 사용해서 작업(CRUD) 진행
#    - SQL(구조질의어): RDB를 사용하기 위해서는 반드시 사용
#    - RDB(SQL)을 사용, NoSQL
#     CREATE   -> INSERT
#     READ     -> SELECT
#     UPDATE   -> UPDATE
#     DELETE   -> DELETE

# ** MongoDB 사용방법 2가지
# 1. 직접설치
#   - IP, PORT, ID PW 필요
#   - 사용편함, 관리편함, 커스터마이징 가능
#   - 설치과정 복잡, 설정 직접, 컴퓨터 자원부족
# 2. MongoDB에서 제공하는 web Cloud 사용
#   - URL, ID, PW 필요
#   - 사용편함, 설치 필요 없음, 설정 필요없음, 컴퓨터 자원소모 안함
#   - 관리안됨, 커스터마이징 안 됨

# ** MongoDB 구조
#   설치: MongoDB(DBMS) : 시스템
#           ㄴ DB(카카오톡) : 폴더
#               ㄴ collection(회원) : 표
#               ㄴ collection(톡)
#               ㄴ collection(친구)
#               ㄴ etc
#           ㄴ DB(카카오뱅크) : 폴더
#               ㄴ collection(회원)
#               ㄴ collection(계좌)
#               ㄴ collection(대출)
#               ㄴ etc
#           ㄴ DB(카카오페이) : 폴더
#               ㄴ etc


# pymongo : python - mongoDB 연결해서 사용

from pymongo import MongoClient
# MongoDB Connection
def conn_mongodb():
    # URL,ID,PW
    DB_ID = "root"  # 상수(전체 대문자로 변수명을 사용) **불변
    DB_PW = "1234"  # ex) 은행에서의 금리(상수)
    client = MongoClient(f"mongodb+srv://{DB_ID}:{DB_PW}@daumcluster.pyxob0o.mongodb.net/") # URL
    db = client["daum"]
    collection = db.get_collection("news")
    return collection













