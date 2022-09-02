import sys

print("toeic", "tofle", "g_telp")
print("toeic", "tofle", "g_telp", sep=",", end="?")  # 디폴트는 sep=" "(콤마기준)이고 end="\n"이었구나
print("toeic", "tofle", "g_telp", sep="@@@")

print(1, 2, file=sys.stdout)  # 표준 출력
print(3, 4, file=sys.stderr)  # for 에러 탐색

scores = {"국어": 70, "수학": 85, "코딩": 100}
for subj, score in scores.items():
    print(subj.ljust(8), str(score).rjust(4), sep=":")  # 8칸구하고 왼쪽정렬, 4칸구해서 오른쪽정렬

for num in range(1, 11):
    print("대기번호", str(num).zfill(3), sep=" : ")  # zfill() 괄호안 크기만큼의 공간을 확보후, 값을 집어넣는데 빈 공간은 0으로 꽉

print("{0: >+10}".format(500))
print("{0:,}".format(100000000000))
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

print("{0:f}".format(5 / 3))
print("{0:.2f}".format(5 / 3))

answer = int(input("정수를 입력하세요 : "))
print(answer + 10)

answer2 = input("문자열을 입력하세요 : ")  # input의 디폴트는 문자열이기에, 숫자계산 등에 활용하고프면, int() 등으로 감싸주자
print(answer2 + "10")
