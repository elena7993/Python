import random as ran
from math import ceil

# print(ceil(ran.random() * 100))
# =>random() 이 메서드는 0~1사이의 값을 랜덤하게 반환함

# print(ran.randrange(1, 101))
# =>랜덤한 값의 범위를 지정할 수 있다

# nums = [1, 2, 3, 4, 5, 6]

# ran.shuffle(nums)
# print(nums)
# =>리스트의 값을 랜덤하게 섞어준다

# random_num = ran.choices(nums)
# print(random_num)
# =>리스트에서 랜덤한 요소를 하나 선택해 준다


menus = ["딸기", "명란크림우동", "감자탕", "쇠주", "츄르", "김밥"]

print(f"오늘의 점메추: {ran.choices(menus)}" )
