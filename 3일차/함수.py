# def food():
#   print("국밥")
#   print("딸기")
#   print("삼겹살")
#   print("장칼국수")

# food()

# food_all = {
#   "menu_1": "국밥",
#   "menu_2": "딸기",
#   "menu_3": "삼겹살",
#   "menu_4": "장칼국수",
# }

# def food_list():
#   for foods in food_all:
#     print(f"{foods}: {food_all[foods]}")

# food_list()

# def intro_1():
#   print("안녕, 내 이름은 엘레나야. 나이는 12세야.")

# def intro_2():
#   print("안녕, 내 이름은 정환이야. 나이는 11세야.")

# intro_1()
# intro_2()

def intro_1(name="익명", age=0):
  # 매개변수 기본값을 설정해줄 수 있음
  print(f"안녕, 내 이름은 {name}(이)야. 나이는 {age}세야.")

# intro_1("엘레나", 12)
# intro_1("정환", 11)
# intro_1("정현", 10)

intro_1()