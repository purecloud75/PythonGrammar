# open(파일명, 파일을 여는 목적, 인코딩정보)을 통해서 파일을 열 수가 있습니다.

score_file = open("score.text", "w", encoding="utf8")  # write  최초에 적을 때 쓰나보다. 이어서 쓰고자할 때 덮어쓰기 될 수 있음
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()  # 파일을 닫아준다.

score_file = open("score.text", "a", encoding="utf8")  # append  이미 있는 파일에다가 뒤에 이어서 쓰고싶을 때
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.text", "r", encoding="utf8")  # read  파일 내의 모든 내용을 여기 콘솔창에서 읽을 수 있다.
print(score_file.read())
score_file.close()

score_file = open("score.text", "r", encoding="utf8")
while True:
    line = score_file.readline()  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
    if not line:
        break
    print(line, end="")  # print()에 한번, readline()에서 한번 총 2번의 엔터가 되므로, end=""을 통해 하나 빼준다고 생각하자
score_file.close()
