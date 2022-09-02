# 애완동물을 소개해 주세요~

animal = "노트북"
name = "레노버 슬림5"
age = 2
pros = "가성비"
is_good = age <= 5

print("우리집 " + animal + "의 이름은 " + name + "입니다.")
print(name + "는 " + str(age) + "살이며, 장점은 " + pros + "입니다.")
print(name + "는 좋은걸까요? " + str(is_good))

# 숫자와 진리값을 출력하려면, str()로 감싸줘. 단 아래처럼 콤마를 쓴다면 이 함수는 필요없다.
'''
여러문장 주석처리가
됩니다!
'''

print("우리집 ", animal, "의 이름은 ", name, "입니다.")
print(name, "는 ", age, "살이며, 장점은 ", pros, "입니다.")
print(name, "는 좋은걸까요? ", is_good)

print(2 * 3)
print(2 ** 3)  # 제곱
print(5 / 3)  # 실제 나눗셈 결과값
print(5 // 3)  # 몫
print(5 % 3)  # 나머지

print(10 > 30)
print(1 == 1)
print(99 != 99)
print(not (99 != 99))
print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))
print((3 < 0) or (3 > 5))
print((3 < 0) | (3 > 5))
print(20 > 10 > 5)
