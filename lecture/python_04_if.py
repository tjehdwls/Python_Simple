# 조건문(condition) : if~dlif~else
# - 특정조건을 만족하는 려우 수행할 적압에 사용
# - 모든 조건은 boolean으로 표현됨
# - 조건문의 경우 if, elif, else 블록 내 들여쓰기
# - 모든 블록문의 시작점의 마지막 :(콜론) 추가

# JAVA & C 에서의 조건문

# if (조건문 1) {
#   code
# } else if (조건문2) {
#   code
# } else if (조건문3) {
#   code
# } else {
#   code
# }

# python 에서의 조건문 (들여쓰기 필수)

# if 조건문 1:
#   code
# elif 조건문2:
#   code
# elif 조건문3:
#   code
# else
#   code

# if 조건문 1:
#   code
# if 조건문2:
#   code
# if 조건문3:
#   code

# if문을 활용한 조합식
# 1. if
# 2. if~else (두개의 조건)
# 3. if~elif~elif (여러개의 조건)
# 4. if~elif~else

# 논리 연산자(and, or, not)

# 1.and
# 조건 1  조건 2   결과
#  F  and   F      F
#  T  and   F      F
#  F  and   T      F
#  T  and   T      T

# 2.or
# 조건 1  조건 2   결과
#  F   or   F      F
#  T   or   F      T
#  F   or   T      T
#  T   or   T      T

# 3.not (토글)
# F -> T
# T -> F

# quiz
# A, B, C, D, F
# 4.1~4.5 : A
# 3.6~4.0 : B
# 3.1~3.5 : C
# 2.6~3.0 : D
# 2.5 이하 : F



score = 4.1 #학점

if score >= 4.1 and score <= 4.5:
    print("A")
elif score >= 3.6 and score <= 4.0:
    print("B")
elif score >= 3.1 and score <= 3.5:
    print("C")
elif score >= 2.6 and score <= 3.0:
    print("D")
else:
    print("F")

if 4.5 >= score >= 4.1:
    print("A")
elif 4.0 >= score >= 3.6:
    print("B")
elif 3.5 >= score >= 3.1:
    print("C")
elif 3.0 >= score >= 2.6:
    print("D")
else:
    print("F")

if 4.5 >= score >= 0.0:   # T: 0.0~4.5
    if score >= 4.1:      # F : 0.0~4.0
        print("A")
    elif score >= 3.6:    # F : 0.0~3.5
        print("B")
    elif score >= 3.1:    # F : 0.0~3.0
        print("C")
    elif score >= 2.6:    # F : 0.0~2.5
        print("D")
    else:
        print("F")
else:
    print("0.0~4.5 사이의 값을 입력하세요.")



print("="*50)

# 초 중 고 대 학생 X 판별
# input() : 키보드로 값을 입력, 문자열이 기본
born = input("나이:")      # "2001"

from datetime import datetime
now = datetime.today().year
age = now - int(born)+1

if 26 >= age >= 20:
    print("대학생")
elif 19 >= age >= 17:
    print("대학생")
elif 16 >= age >= 14:
    print("대학생")
elif 13 >= age >= 8:
    print("대학생")
else:
    print("학생이 아닙니다.")



