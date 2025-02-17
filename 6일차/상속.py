# *상속
# =>특정 클래스의 내용을 그대로 가져올 때 사용
# =>상속한 클래스를 부모 클래스, 상속 받는 클래스를 자식 클래스

import datetime as dt

class ParentClass:
  def parent_text(self):
    return "부모 클래스"
  
# parent = ParentClass()
# print(parent.parent_text())


class ChildClass(ParentClass):
  def child_text(self):
    return "자식 클래스"
  
class Minsu(ParentClass):
  def minsu_text(self):
    return "I'm  Minsu😋"
  
# child = ChildClass()
# print(child.child_text())
# print(child.parent_text())


minsu = Minsu()
print(minsu.minsu_text())
print(minsu.parent_text())

print(dt.datetime.now())




