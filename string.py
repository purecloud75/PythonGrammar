char = "문장입니다."
print(char)

char1 = """
문장인데요,
좀 깁니다.
ㅋㅋㅋ
"""
print(char1)

ID = "981204-1234567"
print("성별 :", ID[7])
print("생년월일 :", ID[0:6])  # 0 ~ 6 미만까지
print("생년월일 :", ID[:6])  # 처음부터

print("뒤 7자리 :", ID[7:14])
print("뒤 7자리 :", ID[7:])  # 끝까지
print("뒤 7자리 :", ID[-7:])  # 뒤에서부터 하면 인덱스가 -1부터 시작임을 명심하자.

sentence = "Python is Amazing"
print(sentence.lower())  # 다 소문자로 바꿔준다.
print(sentence.upper())
print(sentence[0].isupper())  # 0번째 인덱스요소가 대문자인지를 검사한다.
print(len(sentence))  # 길이
print(sentence.replace("Python", "java"))

index = sentence.index("n")  # n이 쓰인 최초의 위치를 반환한다.
print(index)
index = sentence.index("n", index + 1)  # (target, start)
# 쓰인 최초의 위치 바로 다음을 시작점으로해서 다시 n이 쓰인 위치를 찾는다 == 두번째 n을 찾는다
print(index)
print(sentence.count("n"))  # n이 몇 번 나왔는지 횟수를 반환한다.

print(sentence.find("is"))  # 해당 문자열변수에 저장된 문자열에, 괄호안의 text가 없다면 -1을 리턴한다. 있으면 그 단어의 시작인덱스를!
print(sentence.index("bad"))  # 없다면 error을 내면서 프로그램을 종료시킨다. 그래서 find()가 더 좋아보인다.
