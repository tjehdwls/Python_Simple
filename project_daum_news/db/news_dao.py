# DAO: Database Access Object
#   - 데이터 작업(CRUD)을 하는 객채

# 예시)
# 회원 -> member_dao
#           ㄴ 회원가입, 회원수정, 회원노회, 회원검색, 회원삭제

# 로그인 -> login_dao
#           ㄴ 로그인, 로드아웃, ID찾기, PW찾기


from db.common.connection import conn_mongodb


# 뉴스(제목, 본문, 날짜) 저장

def add_news(data):
    conn = conn_mongodb()   # 1. connection
    conn.insert_one(data)   # 2. DB에 저장
