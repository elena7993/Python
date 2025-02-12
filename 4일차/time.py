import time

# print("5초 뒤에 종료합니다.")
# time.sleep(5)
# print("프로그램이 종료되었습니다.")

# * 카운트다운 만들기

# count = 5
# print("카운트다운을 시작합니다👀")
# while count > 0:
#   print(count)
#   time.sleep(1)
#   count -= 1

# print("GO! 🎉")

# print("카운트다운을 시작합니다👀")

# for i in range(5, 0, -1):
#   print(i)
#   time.sleep(1)

# print("GO! 🎉")

# ------------------------------------

num = 6

count = True

while count:
  num -= 1
  time.sleep(1)
  print(f"{num}초")

  if num == 0:
    count = False
    print("GO! 🎉")
