# DB maraDB
# - type : 관계형 데이터베이스(RDB)

# **root 계정
# - 신급 권한을 가지는 계정
# - RDB는 반드시 root 계정 생성
# - "DB 관리자" -> root 사용X , new계정(권한 많이 부여)




import pymysql

def connection():
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="12341234",
            db="simple",
            charset="utf8",
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except pymysql.Error as e:
        print(f"mariadb 연결실패{e}")