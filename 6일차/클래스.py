# *클래스
# =>비슷한 코드가 자주 사용하게 되면 메모리 등 효율적으로 만들 수 없기 때문에
# 데이터 및 기능을 함께 묶어 새로운운 객체의 형태로 만듬

# 변수 = 메모리 주소에 값이 할당됨

# Human
# =>머리
# =>몸통
# =>팔
# =>다리

# 함수형태로 만든다면?

# 1번사람의 함수
# 머리: ㅁㅁㅁ
# 몸통: ㅇㅇㅇ
# 팔: ㅎㅎㅎ
# 다리: ㄴㄴㄴ

# 2번사람의 함수
# 머리: ㅁㅁㅁ
# 몸통: ㅇㅇㅇ
# 팔: ㅎㅎㅎ
# 다리: ㄴㄴㄴ

# ... 사람을 만들 때마다 함수를 계속 만들어야 한다는 단점이 있음.

# --------------------------------------------------------------

# 클래스는? =>1번사람이 필요해! 라고 한다면?
# =?1번사람 머리특징, 몸통특징, 팔특징, 다리특징

# Human
# =>머리: 머리특징
# =>몸통: 몸통특징
# =>팔: 팔특징
# =>다리: 다리특징

# 필요한걸 미리 제작함.

# --------------------------------------------------------------

# *함수

# num_1 = 0
# num_2 = 0

# def plus(a, b):
#   num_1 = a
#   num_2 = b
#   return num_1 + num_2

# def minus(a, b):
#   num_1 = a
#   num_2 = b
#   return num_1 - num_2


# plus_result = plus(1, 2)
# minus_result = minus(2, 1)

# print(f"뎃셈결과: {plus_result}")
# print(f"뺄셈결과: {minus_result}")


# *클래스
# def __init__(self)
# =>init(초기값셋팅하는 메서드), 매개변수(self반드시 넣어줘야함. 규칙임/this와 비슷함)

# class Calc:
#   def __init__(self, a, b):
#     self.num_1 = a
#     self.num_2 = b

#   def plus(self):
#     return self.num_1 + self.num_2
  
#   def minus(self):
#     return self.num_1 - self.num_2
  
# input_num = Calc(2, 4)
# # 생성자 함수(인스턴스)라고 함
# print(f"덧셈결과: {input_num.plus()}")
# print(f"뺄셈결과: {input_num.minus()}")


# input_num_2 = Calc(6, 4)
# print(f"덧셈결과: {input_num_2.plus()}")
# print(f"뺄셈결과: {input_num_2.minus()}")

class Calc:
  def __init__(self, a, b):
    self.num_1 = a
    self.num_2 = b

  def plus(self):
    return self.num_1 + self.num_2
  
  def minus(self):
    return self.num_1 - self.num_2
  
  def multiply(self):
    return self.num_1 * self.num_2
  
  def divide(self):
    return self.num_1 / self.num_2
  
result = Calc(2, 4)
print(f"덧셈결과: {result.plus()}")
print(f"뺄셈결과: {result.minus()}")
print(f"곱셈결과: {result.multiply()}")
print(f"나눗셈결과: {result.divide()}")

result_01 = Calc(5, 10)
print(f"덧셈결과: {result_01.plus()}")
print(f"뺄셈결과: {result_01.minus()}")
print(f"곱셈결과: {result_01.multiply()}")
print(f"나눗셈결과: {result_01.divide()}")