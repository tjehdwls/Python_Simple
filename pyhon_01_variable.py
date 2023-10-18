# 주석(comment): 간단 메모, 실행X
# 글씨체: D2Coding (폰트 -> 멘로)

# 1. 출력 함수(print)
# - ()안의 값을 출력
# - 변수값 확인 용도로 많이 사용
print("hello python")
print("=" * 200)

# 문자열 타입(string type)
# - Python: '' or "" -> string
# but C, Java : ''(char), ""(string)

# 참고 : escape code
# - 문법 : \ + @
# - 문자열(string) 내의 일부 문자의 의미를 달리하여 특정한 효과 주기
# - 예) \n : 한 줄 개행=엔터, \t: 탭(8칸공백)
print("Hello \nPython")
# =print("hello")
#  print("Python")
print("Hello \tPython")
# 알아먹기 쉽게 코드를 작성해야 함
# 회사 -> 안정적인걸 선호함
print("=" * 200)

# 2.자료형(Type)
# - python의 모든 자료형은 객체(object)이다
# - java 정수형: byte, short, int, long
# - Python 정수형: int
# 1) 문자열(string): "Hello", 'hi'
# 2) 정수형(int): 3, -1, 0
# 3) 실수형(float): 3.14, 0.0, -2.2
# 4) 논리형(boolean): True, False
# 영타 300 목표


# 설명: 동일함 Type에서 다양한종류의 자료형을 사용하는 이유?
# - 메모리(저장공간)을 효율적으로 사용하기 위해서
# - 대부분 만들어진지 오래 된 언어는 다양한 종류릐 자료형 사용!
# - 자료형은 저장 할 수 있는 크기의 범위가 지정됨
# - 가정: int(-10000 ~ 10000)
# - 가정: short(-100 ~ 100)
# - 특정값: 0~9 -> 어떤 Type을 사용하면 효율적일까 = short


# 3.동적 타이핑 언어(Dynamic Typing Language)
# - JAVA: int num = 4;
# - Python: num = 4
# - Python은 코드가 실행될 때 자동으로 Type을 지정
# - type()한수: ()안의 값의 Type을 확인할떄 사용
print(type("ABC"))
print(type(3.14))
print(type(5))
print("=" * 200)
#꽤 잘씀


# 4.형 변환(Type Casting) (논리형은 제외)
# - Type Casting을 사용하면 값을 원하는 자료형으로 변환 가능
# - 1) int(): 정수형으로 변환
# - 2) float(): 실수형으로 변환
# - 3) str(): 문자열형으로 변환
# 문자열 자체를 정수형이나 실수형으로는 불가능
# 문자열 실수형
# 문자열 정수형
int_a = 3
float_b = 3.14
str_int_c = "9"
str_float_d = "9.2"

# 정수형(3) -> 실수형(3.0) 가능
print(float(int_a))
# 정수형(3) -> 문자열("3")
print(str(int_a))
# 실수형(3.14) -> 정수형(3) 주의!(파일 손실 생김)
# 실수형(3.14) -> 문자열("3.14")
print(str(float_b))
# 문자열 정수형("3") -> 정수형(3)
print(int(str_int_c))
# 문자열 정수형("3") -> 실수형(3.0)
print(float(str_int_c))
# 문자열 실수형("3.14") -> 정수형(Error)
# print(int(str))
# 문자열 실수형("3.14") -> 실수형
print(float(str_float_d))
print("=" * 200)

# 5.None
# - 아무런 값을 갖지 않을떄 사용
# - 일반적으로 변수가 초기값을 갖지 않게 하고 생성할 때 사용
# - 기타 언어의 Null과 같은 의미로 사용

# C, JAVA: 변수생성 -> int num;
# Python: 변수생성 -> num (Error)
# python: 변수생성 -> num = None
student_name = None  # 이건 절대 사용금지! # "Null Pointer Exception"=재앙
student_name = ""    # 적극권장

# 기본 자료형: 변수에 값이 그대로 저장
# - int num = 4;
# 객채 자료형: 변수에 값이 위치한 "주소"가 저장
# - string name = "10";

# - JAVA, C : 기본, 객채 둘다 사용
# - python: 객채만 사용



# 6.변수
# - 변수: 하나의 갑을 저장할 수있는 메모리공간
num = 4
num = 10
print(num) # 출력값: 10

# - 변수 생성 및 초기화
# 문법: num = 5
#   * num: "nume" 변수생성
#   * 대입연산자(=): 우측의 값을 좌측에 저장
#   * 동등연산자(==): 좌측과 우측의 값이 같다
#   * 초기화? 초기 변수를 생성하면 쓰레기 파일들이 존재, 수에 값을 대입하면 공간이 초기화 되고 값만 저장
#     - 원래있었던 쓰레기 파일을 싹 다 지우고 변수 값을 넣기 때문에 싹 다 지우는 과정을 두고 초기화라고 한다

# name(변수명), =(대입연산자), "cherry"(값)
name = "cherry"



# 7.명명규칙(naming rule)
# * 변수, 함수, 클래스 등의 사용자 정의 이름에 사용
# * 명확하고 알아보기 쉽게!!

# 1. 영문 대소문자, 숫자, 특수문자(_)만 사용
# 2. 숫자로 시작할 수 없음
# 3. 영어 대소문자 구별
#    abc Abc ABC ABc... (모두 다른 변수)
# 4. 예약어 사용 불가
#    예약어: python 에서 미리 선점하여 사용중인 키워드
#      ex) print, for, while, if else, class, and, return, import, def, pass...



# 8.Naming Method
# - 변수, 함수, 클래스 등의 사용자 정의이름에 사용하는 기법
# - 프로그래밍 언어벼로 사용하는  naming method가 다름

# 1.snake_case: 소문자만 사용, 합성어는 _사용
#   ex) sudent_name
# 2.camelCase: 첫글자 소문자, 합성어 첫글자 대문자
#   ex) shosunStudentName
# 3.PascalCase: 첫글자 대문자, 합성어 첫글자 대문자
#   ex) ChosunStudentName


#             변수          함수           클래스
# Java, C  camelCase    camelCase()   PascalCase
# Python   snake_case   snake_case()   PascalCase



# 9.동적 출력
print("=" * 200)
student_num = 20203219
student_name = "ME"
# 출력 예: "조선대학교 20203219, ME 입니다."
print("조선대학교 20203219, ME 입니다.") # 하드 코딩 지양

# 1. format() - old
print("조선대학교 {}, {} 입니다.".format(student_num, student_name))
# 2. f-string - new
print(f"조선대학교 {student_num}, {student_name} 입니다.")


# 10.간단한 사칙연산
# + : 더하기
# - : 빼기
# * : 곱하기
# ** or ^ : 제곱  ex) 3^2
# 5/2 : 나누기        2.5
# 5%2 : 나누기(나머지) 1
# 5//2 : 나누기(몫)   2

# quiz
num = 9
num - 1
num + 2
print(num) # 9가 나옴