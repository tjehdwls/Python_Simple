# 컬렉션 타입
# - 변수 하나에 값을 여러개 저장
# - 실질적으로 변수에 컬렉션 1개가 저장
# - list(중요), Tuple(파이썬에서 씀), Dictionary(중요), set(거의안씀)
#      (인덱스를가지고있음          /

# 1. 리스트(List)  - 기차와 비슷하다
# - 시퀀스 자료형(연속 된 값 저장)
# - index 사용 (Slicing 가능)
# - [] 사용
# - 정렬 가능
# - mutable(생성 된 후 변경 가능)
# - packing 과 unpacking 가능
# - 멤버함수 : append(0, extend(), insert(), remove(), pop(), index(), sorted() 등
# - 2차원 리스트는 표(table)와 동일한 형태

list_a = [1, 2, 3]
list_b = []
list_c = ["chosun", 5, 3.14, [1, 2, 3]] # 2차원리스트 포함

# packing and unpacking
list_d = [ "a", "b", "c"]  # packing
a, b, c = ["a", "b", "c"]  # unpacking

                        # JAVA, C
                        # a = list_d[0]
                        # b = list_d[1]
                        # c = list_d[2]

# append(값) : 리스트의 맨 마지막에 값을 추가
a = [1, 2, 3]
a.append(4)
print(a)

# insert(인덱스, 값) : 리스트의 원하는 인덱스에 값을 추가
b = [1, 2, 3]
b.insert(1, 9)
print(b)

# extend(list) : list와 list를 병함
a = [1, 2, 3]
b = [4, 5, 6]
#a.extend(b)
#print(a)
c = a+b
print(c)

# remove(값) : 리스트 내의 원소를 값으로 삭제
# pop(인덱스) : 리스트 내의 원소를 인덱스로 삭제
abc = [1,2,3,4,5]
abc.remove(3) # 3이라는 값을 삭제
print(abc)
e = abc.pop(0)  # 0번 인덱스를 삭제(이렇게 쓰면 원래값 저장됨)
print(abc)
print(e)

# index() : ()안의 값의 인덱스값을 출력
a = ["A", "B"]
print(a.index("B"))

# sort() and sorted() : 리스트 안의 원소들을 정렬
# - sort() : 원본값 자체를 정렬 (원본값 삭제)  (사용자제하셈)
# - sorted() : 원본값을 복제해서 정렬 (원본값유지)
a = [95, 34, 52, 45, 3, 9]
b = sorted(a) # 디폴트 : 오름차순
c = sorted(a, reverse=True) #내림차순
print(a)
print(b)
print(c)

# 2.튜플(Tuple) = 기차
# - List와 대부분 도일
# - 시퀀스 자료형
# - index 사용(Slicing 가능)
# - packing과 unpacking 가능
# - immutable(생성 된 후 변경 불가능)
# - 정렬 불가능
# - () 사용(생략 가능)
# * 직접 생성하느 경우는 없다
#    -> python에서 결과값을 tuple로 제공

print("="*100)
a = [1, 2, 3]   # List
b = (1, 2, 3)   # Tuple
c = 1, 2, 3     # Tuple

a[0] = 99    # list
print(a)

# b[0] = 99   # 값변경 불가
# print(b)


# 컨트롤 d, z, x, 쉬프트 F10, 쉬프트 위아래


# 튜플 원소가 1개인 경우!
a = (1, 2, 3)  # Tuple
b = 1, 2, 3    # Tuple
c = (1)        # Tuple
d = 1          # int
e = 1,         # Tuple

print(type(b))
print(type(d))
print(type(e))

a = 5
b = 8

# a와 b를 교환하는 코드

# Java. C에서 swap
# temp = a
# a = b
# b = temp

a, b = b, a   # tuple의 packing and unpacking을 이용

print(a)  # 8
print(b)  # 5


# 3.세트(set)
#  - 수학의 집합 개념
#  - 순서없음(index 없음, 정렬불가)
#  - 중복값 허용하지 않음(중요)
#  - {} 사용
#  - 멤버함수 : union(), interesection(), difference()....

# ** 대부분 중복값 제거 할때 활용

set_a = {1, 1, 1, 2, 2, 3, 4, 5}
print(set_a)

# 중복값 제거 활용 방법
# - a List의 중복값제거
a = ["A", "A", "B", "B", "C"]   #list
# a = set(a)   # ()안의 값을 set type 으로 변경
# a = list(a)  # ()안의 값을 list type 으로 변경
print(list(set(a)))   # list -> set(중복값제거) -> list


# 4.사전(dict)  ** Key 중요
# - 순서가 없음 (인덱스 없음, 정렬 불가)
# - {key:value} -> key, value 1pair
# - key(중복불가) , value(중복가능)
# - key를 통해서만 value 접근가능
# - 멤버함수: update(), get(), keys(), values(), items()

# 사전(dict) type의 중요성
# - 외부에서 데이터를 주고 받는 표준 규격: JSON
#  {"id":"abc123", "pw":"@!123", "name":"cherry"}
# - pythondml dict == JSON
print("="*100)


dict_a = {"korea":"Seoul",
          "Canada":"ottwas",
          "USA":"Washington D.C"}
print(dict_a)
import pprint
pprint.pprint(dict_a)   # pprint 원래는 엔터쳐서 이쁘게 나옴

# update() : dict와 dict 병합
a = {"a":1,
     "b":2}
b = {"b":3,
     "c":5}
a.update(b)
print(a)   # 병함시 중복key는 입력값이 우선된다

# pop(key) : dict 원소를 key를 통해 삭제
abc = {"a":1, "b":2, "c":3}
c = abc.pop("a")
print(abc)
print(c)

# in() : ()안의 key값이 존재확인
print("c" in abc)
print("f" in abc)

# get() : 값 접금
# listm tuple, dict 접근 -> 컬렉션[index or key]
print(abc["b"])
# print(abc["f"])   # key가 없으면 Error 발생
print(a.get("f"))   # key가 없으면 none 출력 (error X)

# keys(), values(), items()
print(a)
print(a.keys())   # key만 추출
print(a.values()) # value만 추출
print(a.items())  # (둘, 다) 추출

print(list(a.keys()))   # 활용

# clear() : dict 초기화
print(abc)
abc.clear()
print(abc)


# quiz (타입확인)

a = {}

print(type(a))


#  dict = JSON (데이터전송포맷)
















