# 맨처음에는 waitingNum에 0이 들어가서 실행문을 거치고 1 증가해서, 다음에는 1이 waitingNum에 들어가서 실행문거치고... 반복
for waitingNum in range(5):  # 0부터 5미만까지를 나타낸다. range(1, 6) == 1이상 6미만을 나타낸다.
    # print("대기번호 : %d" % waitingNum)
    # print("대기번호 : {}" .format(waitingNum))
    print(f"대기번호 : {waitingNum}")

ediya = ["테드창", "이동휘", "신하균", "이하늬"]
for customer in ediya:
    print("{0}님, 주문하신 커피 나왔습니다!".format(customer))

students = ["james", "bob", "cathedy", "anna"]
students = [len(i) for i in students]  # students라는 리스트변수에 들어있는 요소가 i에 들어와서 한바퀴 돌면서 길이가 다시 리스트로!
print(students)

num = [1, 2, 3, 4, 5]
num = [i + 100 for i in num]
print(num)
