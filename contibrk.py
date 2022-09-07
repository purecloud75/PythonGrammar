# continue 그 밑에 있는 문장을 실행하지 않고 다음 반복으로 이어서 간다.
# break 를 만나는 순간 즉시 반복문을 탈출한다.
absent = [2, 5]
noBook = [7]
for student in range(1, 11):
    if student in absent:  # if 뒤에 나오는 조건식이 참이면 continue 실행 후 바로 다음반복으로 이어간다.
        continue
    elif student in noBook:
        print("{0}학생은 출석점수 깎을겁니다.".format(student))
        break
    print("{0}학생, 책을 읽어봐".format(student))
