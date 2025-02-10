# 2. 변수로 임의의 유저 아이디와 패스워드를 저장하고 input을 통하여 
# 입력한 아이디와 패스워드가 맞는지 확인할 수 있는 유효성 로직 구현

username = "Elena"
password = 123456

input_username = input("유저의 이름을 입력하세요")
input_password = int(input("패스워드를 입력하세요"))

if username != input_username and password != input_password:
  print("유저 이름과 패스워드가 모두 잘못되었습니다.")
elif username != input_username:
  print(f"{input_username}는 잘못된 유저 이름입니다. ")
elif password != input_password:
  print(f"{input_password}는 잘못된 패스워드입니다")
else:
  print(f"{username}님, 환영합니다!")