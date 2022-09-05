from random import *

# 파이썬에서 제공하는 random 라이브러리를 사용할 수 있다. 난수, 무작위로 숫자를 뽑아주는 걸 말한다.
# 쓰고자하는 라이브러리의 이름으로 해당 파일의 이름을 지으면 안된다. 사용불가가 된다.
print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)
print(int(random() * 10))
print(int(random() * 10) + 1)  # 1 ~ 10 이하의 임의의 값 생성
print()

# 로또번호 추첨
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성. 양쪽을 다 포함.
