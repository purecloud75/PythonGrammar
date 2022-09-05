weather = input("what's going on? ")

if weather == "snow":
    print("slippery")
elif weather == ("rainy" or "storm"):
    print("umbrella")
elif weather == "bad air":
    print("mask")
else:
    print("good")

# input()은 기본적으로 문자열로써 입력값을 받고 쓰기에, 정수를 원한다면 int()로 감싸자!
temp = int(input("what's the today's temperature? "))
if temp >= 30:
    print("hot today")
elif 15 <= temp < 30:
    print("good")
elif 0 <= temp < 15:
    print("chill")
else:
    print("cold today")
