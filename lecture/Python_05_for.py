# 제어문
# 1.조건문(if)
# 2.반복문(for, while)

# 반복문(Loop)
# - 반복적인 작업을 가능하게 해주는 도구
# - list, str, tuple 등 컬렉션 타입의 아이템을 하나씩 순회하면서 사용가능(for)
# - 특정 조건을 만족하는 경우(while)

# 반복횟수 안다 = for
# 반복횟수 모른다 = while

# for 문 기본문법(list 활용)
for num in [1, 2, 3]:
    print(num)

# range함수
# - range(시작, 끝, 증감)
# - default 시작(0), 증감(+1)
# - range(3):           출력: 0 1 2
# - range(1, 10):       출력: 1 2 3 4 5 6 7 8 9
# - range(2, 5, 2):     출력: 2 4

print("="*50)
# range() 함수를 활용해서 1~9까지 출력하는 for문
for i in range(1,10):
    print(i)

print("="*50)
# list를 활용한 for문
temp = ["A", "B", "C", "D", "E"]
for alpha in temp:
    print(alpha)

# enumerate() 함수
# - 반복횟수 정보를 사용하고 싶을때
# - 0번부터 시작
for i, alpha in enumerate(temp):
    print(i+1, alpha)

print("="*50)
# dict를 활용한 for문
# - dict를 for로 출력하면 => key값만 출력
# - dict.keys(), dict.values(), dict.items()
temp = {"A": 1,
        "B": 2,
        "C": 3,
        "D": 4}
for element in temp.values():
    print(element)

print("="*50)

for key, value in temp.items():    # tuple타입(key, value)
    print(key)
    print(value)


print("="*50)
# break: 즉시 반복문을 빠져나가라
# a를 출력하다가 3을 만나면 멈추세요
a = [1, 2, 3, 4, 5]
for i in a:
    if i == 3:
        break
    print(i)


print("="*50)
# continue: 즉시 다음 반복으로 넘어가라
# 1~10까지에서 홀수만 출력하시오
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


print("="*50)
# 구구단 2단 코드
for i in range(1,10):
    print("2 x",i,"=",2*i)

print("="*50)

for i in range(1,10):
    print(f"2x{i}={i*2}")


