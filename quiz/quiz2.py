from random import *

users = range(1, 21)  # 1부터 20까지의 숫자를 생성. 하지만 range타입이라서 list에서 쓸 수 있는 함수를 못 쓴다.
print(type(users))
users = list(users)  # 그래서 타입변환을 해준다. 자료구조의 변환
print(type(users))

shuffle(users)

winners = sample(users, 4)  # 4명 중에서 1명은 치킨, 3명은 커피
print(type(winners))

print(f"--당첨자 발표--\n치킨 당첨자 : {winners[0]}\n커피 당첨자 : {winners[1:4]}\n--축하합니다--")
