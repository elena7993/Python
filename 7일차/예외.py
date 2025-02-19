# *예외
# =>예상치 못한 상황 -> 오류!
# =>두가지의 오류가 있음

# 1. SyntaxError: 문법 오류
# 2. RuntimeError: 프로그램 실행 중 발행하는 오류

# 1.문법에러
# print("python"}

# 2.런타임에러
# print("running this line code")
# num[0]

# *예외처리 방법
# 1. 조건문으로 처리
# 2 try - except 처리

# input_num = input("Input your number: ")

# if input_num.isdigit():
#   input_num = int(input_num)
#   print(f"입력한 값은 {input_num}입니다")
# else:
#   print("숫자만 입력해주세요!")

try:
  input_num = int(input("Input your number: "))
  # 예외가 발생할 것 같은 코드를 넣는다
  print(f"입력한 값은{input_num}입니다")
except:
  print("오류오류!")
finally:
  print("무조건 실행! 오류가 나든 말든!")