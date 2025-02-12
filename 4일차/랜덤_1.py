import random as ran

# *문제

# 아침, 저녁, 저녁 메뉴들 각각 저장
# 사용자가 아침 또는 점심 또는 저녁을 입력 받게 만들기
# 조건문을 사용하여 만약에 아침을 입력하면 아침메뉴중 랜덤하게 뽑아주기기

# 출력결과
# 렌덤메뉴 ~ 입니다
# 메뉴를 입력해주세요 (예, 아침, 점심, 저녁 입력)
# 저녁
# 선택된 메뉴는 보쌈입니다~

# 이런식으로 나오게끔!

breakfast = ["커피", "도넛", "토스트", "샐러드", "맥모닝", "미역국"]
lunch = ["해장국", "김밥", "국밥", "제육볶음", "돈까스", "카레", "중국집"]
dinner = ["치맥", "마라탕", "떡볶이", "순대볶음", "된장찌개", "초밥", "호박"]

time_for_meal = input("식사시간을 입력하세욥🍿")

if time_for_meal == "아침":
  get_menu = ran.choices(breakfast)
elif time_for_meal == "점심":
  get_menu = ran.choices(lunch)
elif time_for_meal == "저녁":
  get_menu = ran.choice(dinner)
else:
  print("올바른 식사시간이 아닙니다😵")

print(f"선택된 메뉴는 {get_menu}입니다. Enjoy your Meal 🍝")