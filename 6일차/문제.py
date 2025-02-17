# *문제
# =>회원가입 클래스를 제작 하려고 하는데 이 때,
# =>자동으로 회원가입 날짜를 상속 받을 수 있도록 함
# =>클래스 두 개 생성
# =>부모 클래스에는 회원 가입 날짜 출력하는 함수 제작(datetime 모듈 사용)
# =>자식클래스 기능은 유저의 아이디, 패스워드를 입력한 값 출력

# =>출력결과
# 아이디: sideway / 패스워드: 1234
# 회원가입 날짜: 2023-02-08 19:05:34.605578

import datetime as dt

class Info_1:
  def date(self):
    return dt.datetime.now()


class Info_2(Info_1):
  def __init__(self, id, pw):
    self.username = id
    self.password = pw

user = Info_2("sideway", 1234)

print(f"아이디: {user.username} / 비밀번호: {user.password}")
print(f"회원가입 날짜: {user.date()}")





