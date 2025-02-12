import random as ran

num = ran.randrange(1, 100)

playing = True
count = 1

while playing:
  input_num = int(input("숫자를 입력하세요"))
  # 랜덤숫자가 입력숫자보다 더 클때
  if num < input_num:
    print("Down😵")
    count += 1
  elif num > input_num:
    print("Up😎")
    count += 1
  elif num == input_num:
    playing = False
    print("BOOOOOOOOM😍")
    print(f"{count}번 만에 맞췄습니다!!")

    # 카운트 횟수를 제한할 수도 있고
    # 카운트 횟수와, 점수를 계산하는 로직을 구현할 수도 있다(게임적 요소)