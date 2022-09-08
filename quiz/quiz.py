from random import *

day = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월", day, "일로 선정되었습니다.")


URL = "http://naver.com"
removedURL = URL.replace("http://", "")
shortURL = removedURL[:removedURL.index(".")]  # 처음에서부터 .이 있는 위치인덱스 미만까지의 문자열로 초기화한다 == [0:5]
moreShortURL = shortURL[:3]
length = len(shortURL)
countNum = shortURL.count("e")
print(f"생성된 비밀번호 : {moreShortURL}{length}{countNum}!")

password = moreShortURL + str(length) + str(countNum)
print("{0}의 비밀번호는 {1} 입니다.".format(URL, password))
