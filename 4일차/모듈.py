# *모듈
# =>여러 변수, 함수를 가지고 있는 집합체로, 표준모듈, 외부모듈이 있음.
# =>표준모듈: 파이썬에 기본적으로 내장되어 있음.
# =>외부모듈: 외부 또는 다른사람이 만들어 공개, 배포 해둔 모듈.
# =>모듈을 사용할 때는 반드시 import를 사용한다.

# import math
# =>모듈을 불러와서 메서드를 연결하여 사용할 수 있는, 불러오는 방식

from math import cos, tan, floor, ceil, trunc
# =>여러 모듈을 한번에 불러올 때 from을 사용한다

# from math import * 
# => *을 사용하면 math 사용하는데, 전부 다~ 불러오겠다라는 뜻! 비효율적!
# => 모든 내용을 가져오기 때문에 상황에 따라 코드의 충돌이 있을 수도 있다

import math as m
# =>as를 사용하여 모듈의 이름을 바꿀 수 있다

# print(math.cos(1))
print(cos(1))
# =>from을 썼을 경우 math를 쓰지 않는다

print(tan(1))

print(m.floor(3.5))
# print(math.ceil(3.5))
# =>올림
# print(math.trunc(3.5))
# =>반올림
