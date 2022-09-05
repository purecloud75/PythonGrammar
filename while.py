customer = "류승룡"
index = 5
while index >= 1:
    print("{1}님, 커피나왔어요. {0}번 남았어요".format(index, customer))
    index -= 1
    if index == 0:
        print("\"안오시네..\" 그냥 내가 마셔야겠다")

target = "허민지"
customer = "unknown"
while customer != target:  # 조건식이 거짓이 되는순간, 즉 두 변수값이 같은순간 이 반복문을 탈출한다.
    print(f"{target}님, 주문하신 밀크티 나왔습니다.")
    customer = input("이름이 어떻게 되세요? ")
print("이용해주셔서 감사합니다 {}님".format(customer))
