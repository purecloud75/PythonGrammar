# 사전이 단어가 있고 거기에 매핑된 뜻이 있는것처럼, 키와 밸류 형태로 있다. 키와 밸류는 어떠한 자료형도 가능하다.

cabinet = {3: "노란색", 100: "분홍색"}
print(cabinet[3])  # 딕셔너리변수옆의 대괄호 안에 인덱스와 유사한 "키"를 넣게되면, 거기에 매핑된 "밸류"를 나타내게 된다.
print(cabinet.get(3))

# print(cabinet[5]) 
# 딕셔너리에 없는 키를 입력할 경우, 대괄호는 오류발생으로 프로그램종료인 반면, get()은 None을 리턴하고 정상진행한다. 즉 얘를 쓰자
print(cabinet.get(5))

# 이 딕셔너리에 3, 5라는 키와 어떠한 밸류가 묶인 형태가 존재하는지를 알려줌
print(3 in cabinet)
print(5 in cabinet)

wallet = {"A": "ID_card", "B": 10, "C": False, 50: 100}
print(wallet.get(50))
print(wallet.get("C"))

wallet["D"] = "creditCard"  # 맨 뒤에서부터 추가. "D"는 키, "creditCard"는 밸류 형태이다.
wallet[70] = 150
wallet["B"] = "10$"
print(wallet)

del wallet[70], wallet[50]  # 키밸류라는 이 한 덩어리를 통째로 삭제 using only key
print(wallet)

print(wallet.keys())
print(wallet.values())
print(wallet.items())

wallet.clear()
print(wallet)