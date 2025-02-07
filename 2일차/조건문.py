# num_1 = 10
# num_2 = 20

# if num_1 > num_2:
#   print("num_1이 큽니다!")
# elif num_1 < num_2:
#   print("num_2가 큽니다!")
# else:
#   print("gggg")

value = input("숫자를 입력하세요:")
# =>터미널에 값을 입력할 수 있음
# =>반환값은 str

result = int(value)
# =>str타입을 int타입으로 변환

# print("당신의 나이는: ", value)
# print(type(value))

# print(type(result))
# print(result + 101)

if result % 2 == 0:
  print(result, "는(은) 짝수입니다!")
else:
  print(result, "는(은) 홀수입니다") 

