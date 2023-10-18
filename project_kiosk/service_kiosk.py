# 키오스크 기능들
# 사용자 메뉴 선택

# max_cnt = 메뉴별 갯수

def user_choice(max_cnt, menu_type="sub"):   # sub대신 공백도 가능
    while True:
        choice = int(input(">> 번호:"))
        if choice == 99 and menu_type == "main":
            return choice
        if (max_cnt>= choice >= 1):
            return choice
        else:
            print("올바른 번호를 입력 하세요")

#메뉴 출력기능
def show_menu():
    for i, menu in enumerate(main_name.values()):
            print(f"□  {i+1}.{menu}")

        for key, value in drink_name.items():
           print(f"● {key}.{value}({drink_price[key]}원)")

        for i, value in enumerate(bakery_name.values()):
            print(f"● {i+1}.{value}({bakery_price[i+1]}원)")

        for i in range(len(coffee_name)):
            print(f"● {i+1}.{coffee_name[i+1]}({coffee_price[i+1]}원)")

        for i in range(len(bakery_name)):
            print(f"● {i+1}.{bakery_name[i+1]}({bakery_prise[i+1]}원)")