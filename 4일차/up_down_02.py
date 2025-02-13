import random as ran

num = ran.randrange(1, 101)

playing = True
total_count = 10

for count in range(1, (total_count + 1)):
  input_num = int(input(f"({total_count - count + 1}회 남음) 숫자를 입력하세요!"))

  if num < input_num:
    print("Down😵")
  elif num > input_num:
    print("Up😎")
  else:
    score = (total_count - count + 1) * 100
    print(f"BOOOOOOOOM😍{count}번 만에 맞췄습니다!")
    print(f"최종점수는: {score}✨")
    break
else:
  print(f"모든 기회가 소진되었습니다! 정답은 {num}입니다")
