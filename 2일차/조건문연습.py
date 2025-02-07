age = int(input("나이를 입력하세요: "))

if age <= 7 or age >= 66:
  print(age, "세 는 무료 승차 가능합니다^^")
elif age >= 8 and age <= 19:
  print(age, "세는 청소년 요금 1,000원입니다.")
elif age >= 20 and age <= 65:
  print(age, "세는 성인 요금 1,500원입니다")