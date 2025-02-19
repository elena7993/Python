# *문제
# =>동물원 관리 시스템만들기
# =>부모 클래스에는 동물의 이름과 종을 저장한다 / make_sound()라는 메서드를 임의로 만들어 "소리를 낸다"를 출력한다
# =>자식 클래스1은 포유류이며, 부모 클래스를 상속받고 추가 속성에 털 색상을 가진다. make_sound()를 오버라이딩해서 "포유류가 소리를 낸다!"를 출력한다.
# =>자식 클래2는 조류이며, 부모 클래스를 상속받고 추가로 날개길이를 가진다. make_sound()를 오버라이딩해서 "새가 미친듯이 지저귄다!"를 출력한다.

# 출력결과
# 🦁 사자의 소리: 포유류가 소리를 낸다!
# 🦜 앵무새의 소리: 새가 지저귄다!

class Animal:
  def __init__(self, name, species):
    self.name = name
    self.spcies = species

  def make_sound(self):
    return("소리를 낸다!!")
  
class Mammal(Animal):
  def __init__(self, name, color):
    super().__init__(name, "포유류")
    self.color = color

class Bird(Animal):
  def __init__(self, name, wing_length):
    super().__init__(name, "조류")
    self.wing_length = wing_length

  def make_sound(self):
    return ("미친듯이 지저귄다")

mammals = Mammal("호랑이", "Brown")
print(f"{mammals.name}가 {mammals.make_sound()}")

birds = Bird("앵무새", "40cm")
print(f"{birds.name}가 {birds.make_sound()}")
