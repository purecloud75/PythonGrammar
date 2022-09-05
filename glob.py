gun = 10
gun2 = 10


def checkpoint(soldiers):
    gun = 10  # 지역변수이기 때문에, 함수호출이 끝나는 순간 밖에서 쓰이는 gun은 다시 전역변수의 gun이 되어서 여전히 10이다.
    gun -= soldiers
    print("[함수 내] 남은 총 : {}".format(gun))
    return gun


print("처음의 총 개수 : {}".format(gun))
print("남은 총 개수 :{}".format(checkpoint(3)))


def checkpoint2(soldiers):
    global gun2  # 전역공간에 있는 gun 사용
    gun2 -= soldiers
    print("[함수 내] 남은 총 : {}".format(gun2))


print("처음의 총 개수 : {}".format(gun2))
checkpoint2(3)
print("남은 총 개수 :{}".format(gun2))
