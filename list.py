# 순서를 가지는 객체의 집합을 리스트라고 한다.
subway = ["메이크프렘", 12, "블루앰플", 100, True, 5 > 3]
print(subway)
print(subway.index("블루앰플"))  # 2

subway.append("독도토너")  # 맨 뒤에 추가
print(subway)

subway.insert(2, "올리브영")  # 중간에 삽입. 인덱스가 2인자리 == 세번째자리를 대체하고 그 뒤로 한 칸 씩 밀려나는 모습
print(subway)

print(subway.pop())  # 맨 뒤에서부터 삭제하고, 이 함수 자체를 출력하면 빠진 요소 == 맨 마지막요소였던 아이가 나온다
print(subway)
print(subway.pop())
print(subway)

print(subway.count(100))  # 같은 값이 몇 번 들어있는지 확인

numList = [3, 2, 5, 4, 1]
numList.sort()  # 오름차순으로 크기순서대로 정렬
print(numList)
numList.reverse()  # 내림차순으로 정렬
print(numList)

numList.extend(subway)  # 하나의 리스트로 합친다
print(numList)

numList.clear()
print(numList)