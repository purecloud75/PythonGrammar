from random import *

total = 0
for passenger in range(1, 51):
    playTime = randint(5, 50)
    if 5 <= playTime <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(passenger, playTime))
        total += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(passenger, playTime))
print(f"총 탑승 승객 : {total} 분")
