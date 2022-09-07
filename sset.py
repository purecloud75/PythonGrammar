# 집합. 중복 불허, 순서 없음
mySet = {1, 2, 3, 3, 3}
print(mySet)
yourSet = set([2, 3, 5, 7, 7])
print(yourSet)

print(mySet & yourSet)  # 교집합
print(mySet | yourSet)  # 합집합
print(mySet - yourSet)  # 차집합

yourSet.add(85)
yourSet.remove(3)
print(yourSet)
