# 리뷰저장

from db.common.connection import connection


def add_review(data):
    # 1. connection
    conn = connection()

    try:
        # 2. 일꾼 생성
        curs = conn.cursor()
        # 3. JOB 생성(SQL) -> INSERT, DELETE, UPDATE, SELECT
        sql = """
            INSERT INTO tbl_review(title, review, score, writer, reg_date)
            VALUES(%(title)s, %(review)s, %(score)s, %(writer)s, %(reg_date)s)
              """
        # 4. 작업시작
        curs.execute(sql, data)
    except Exception as e:
        print(e)
    finally:
        # 5. 자원해제
        conn.close()


def get_last_review():
    conn = connection()

    try:
        curs = conn.cursor()
        sql = """
                SELECT *
                FROM (
                    SELECT DATE_FORMAT(STR_TO_DATE(reg_date, '%Y. %m. %d. %H:%i'), '%Y%m%d%H%i') AS int_regdate FROM tbl_review
                    ORDER BY reg_date
                ) EX1
                ORDER BY int_regdate DESC LIMIT 1;
              """
        curs.execute(sql)
        # INSERT, DELETE, UPDATE -> 동작(체크)
        # SELECT -> DB로부터 데이터 받기(DICT타입)
        # - 단건 : fetchone()
        # - 복수건 : fetchall()
        result = curs.fetchone()
        return result
    except Exception as e:
        print(e)
    finally:
        conn.close()