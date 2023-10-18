# 문자열의 이해(string)
# 활용 예: 데이터분석 자연어 처리 응용, 사용자로부터 값 입력받고 처리용도,

# 1. 문자열 인덱스(index)
# - 문자열은 각 문자마다 순서(인덱스)가 있음
# - 첫번째 문자부터 마지막 문자까지 순차적으로 인덱스
# - 인덱스 시작은 0
# - 인덱스는 공백포함
print("="*100, "기초문자열")
print("python")


# 2.문자추출
# - 인덱스를 통해서 문자 추출
# - 인덱스 범위 벗어난 경우 오류(Error: index out of range)
lang = "python"
print(lang[0])
print(lang[2])
# print(lang[9]) error

# -1 인덱스(reverse index)
# - 우측에서 좌측으로 인덱스
# - 시작값은 -1

# 3.문자열 슬라이싱
# - lang[?]: 문자 1개만 추출
# - 부분 문자열 추출하고 싶은경우
# - 시작인덱스, 끝인덱스 필요

msg = "python is all you need"
print(msg[0:6]) # 끝인덱스는 반드시 +1
print(msg[:6])  # 시작인덱스 생략 -> 자동 0 입력
print(msg[0:])  # 끝인덱스 생략 -> 자동 -1 입력
print(msg[:])  # 처음부터 끝까지

# 개발자 (웹, 앱, 웹퍼블릿, 웹디자너, 인공지능, ERP)
# 서버엔지니어, 데이터베이스 엔지니어+관리자, SQL 튜너, 데이터 모델러, 네트워크 엔지니어, 데이터 엔지니어, 보안개발자, 데이터 분석가 등등
# 언어 하나 마스터는 필수
# 직업경험도 거의 필수


# quiz
# msg에서 "need"만 추출
#정방향
print(msg[18:])
#역방향
print(msg[-4:])


# 4.문자열 함수
str = "Hello World"

print("="*100, "문자열 함수")
# 4-1. len() : 문자열 길이계산
print(len(str))

# 4-2. upper() and lower() : 대소문자 변경
#  - ID
#  - 데이터 전처리 -> 1A, 1a -> upper()써서 1A로 통일
print(str.upper())
print(str.lower())

# 4-3. replace() : 문자열 내의 특정 문자 치환
print(str.replace("H", "J"))

# 4-4. split() : 구분자를 기준으로 문자열 분할(Degault: 공백)
b = "hello world what a nice weather"
print(b.split()) # 보통쓰임 또는 "/"
print(b.split("w"))

# 4-5. srtip() : 문자열의 좌우공백 제거
id = "                               python1004                       "
print(id.strip())


id = "     SDJ1004      "
# id.lower() "     sdj1004     "
print(id.lower().strip()) #"       sdj1004        "

# 4-6. find() and rfind(0 : 문자열 내부의 특정 문자 위치 인덱스 출력
print(str.find("o"))   # Hell^o^ World
print(str.rfind("o"))  # Hello W^o^rld
print(str.find("world"))  # 못 찾으면 -1 출력
print(str.find("World"))  # 단어의 첫글자 인덱스 출력
print(str.rfind("World"))


# 4-7. in() : 특정 문자열 포함하는지 확인(T, F 출력)
print("Hi" in "Hi Python")

# quiz

id = "cherry1004@gmail.com" #cherry1004 출력
print(id[:10])

# "abc@gmail.com"이와도 출력가능하게
idx = id.find("@")
val = id[:idx]
print(val)

url = "www.naver.com"  # 변화가능
a = url.find(".") + 1
b = url.rfind(".")
val = url[a:b]
print(val)

