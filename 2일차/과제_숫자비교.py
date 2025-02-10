# 1. 두개의 숫자를 입력해서 누가 더 큰지?

num_1 = int(input("첫번째 숫자를 입력하세요."))
num_2 = int(input("두번째 숫자를 입력하세요."))

if num_1 > num_2:
  print(f"{num_1}이(가) 더 큽니다.")
elif num_1 < num_2:
  print(f"{num_2}이(가) 더 큽니다.")
else:
  print("두 숫자가 똑같아욥!")