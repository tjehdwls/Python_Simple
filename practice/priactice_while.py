#문제1) 로그인(pw) -> 3번이상 암호를 틀리면 프로그램 종료
# pw = 1234
# count = 0 # 틀린횟수
#
# while True:
#     if count >= 3:
#         print("암호를 3회이상 틀렸습니다")
#         break
#     input_pw = int(input("암호: "))
#     if pw == input_pw:
#         print("반갑습니다.")
#         break
#     else:
#         print("비밀번호가 틀립니다.")
#         count += 1

# 문제2) 1~100 까지 더해서 총합을 계산하시오.
# - for 문
x = 0
for y in range(1, 101):
    x += y
print(f"합(for):{x}")


# - while 문
x = 0
y = 0
while True:
    y += 1
    if y >= 101:
        break
    x += y
print(f"합(while):{x}")


























































































