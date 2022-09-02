# 프로그램 상에서 사용하고있는 데이터를 파일 형태로 저장해주는 것이다. 누군가가 파일을 주면 우리는 그 파일을 열어서 피클을 이용해서
# 데이터를 가지고 와서 코딩에 또 쓸 수가 있다.
import pickle

profile_file = open("profile.pickle", "wb")  # write binary. pickle에서는 binary를 붙여줘야한다.
data = {1: "하늘색", 2: "분홍색", 3: "라벤더색"}
print(data)
pickle.dump(data, profile_file)  # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
data = pickle.load(profile_file)  # file에 있는 정보를 profile에 불러오기
print(data)
profile_file.close()

# 매번 close()를 쓰지 않아도 된다. with A as B
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("3시간33분16초 시점에서 난 이 부분을 배우고있다.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
