# class Human:
#   def __init__(self):
#     print("응애응애")

# areum = Human()

# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.

# class Human:
#   def __init__(self, name, age, gender):
#     self.name = name
#     self.age = age
#     self.gender = gender

# result = Human("엘레나", "10세", "여자")
# print(f"이름은 {result.name}입니다. 나이는 {result.age}이고 {result.gender}입니다")

# ------------------------------------------------------------

# **** super()는 부모 클래스의 메서드를 자식 클래스에서 호출할 때 사용하는 함수
# 특히 생성자(__init__())를 호출할 때 사용함 ****

# *문제
# =>자동차 관리 시스템 만들기
# =>부모 클래스에는 자동차의 brand와  fuel_type을 저장한다 / 자동차가 출발하고 정지하는 기능을 포함한다
# =>자식 클래스에는 부모 클래스를 상속받아 배터리 용량을 추가로 저장한다
# =>연료타입은 정기로 자동 설정해야 한다
# =>charge()메서드 구현해서 "배터리 충전 중..." 을 출력한다.chr

# 출력결과
# 테슬라 모델3 출발합니다!
# 테슬라 모델3 정지합니다!
# 베터리 중전 중...

class Car:
  def __init__(self, brand, fuel_type):
    self.brand = brand
    self.fuel_type = fuel_type

  def start_car(self):
    return(f"{self.brand} 출발합니다!")
  
  def stop_car(self):
    return(f"{self.brand} 정지합니다!")
  
  
class E_car(Car):
  def __init__(self, brand, battery):
    super().__init__(brand, "전기")
    self.battery = battery

  def charge(self):
    return("배터리 충전 중...")

elec_car = E_car("테슬라 모델3", "100kwh")
print(elec_car.start_car())
print(elec_car.stop_car())
print(elec_car.charge())

print(f"자동차 브랜드: {elec_car.brand}")
print(f"연료타입: {elec_car.fuel_type}")
print(f"배터리 용량: {elec_car.battery}")