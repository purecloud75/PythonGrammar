def profile(name, main_lang, age=25):  # 디폴트매개변수는 그냥 매개변수보다 반드시 뒤에 위치시켜야 한다.
    print(f"이름은 {name}이고, 주사용언어는 {main_lang}이고, 나이는 {age}입니다.")


def profile2(name, main_lang, age):
    print(name, main_lang, age)


# 매개변수앞에 *을 붙이면 원하는 개수만큼 인자를 보낼 수 있다. 가변인자라고 한다.
def profile3(name, age, *language):
    print("이름은 {}이고 나이는 {}이다. 주사용언어는".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("정은비", "python")
profile("최유나", "java")
profile("정예린", "go", 26)  # 디폴트매개변수를 쓴 함수를 호출할 때, 보통은 해당 부분을 적지않으나, 변경이 필요하면 적어준다.

profile2(age=30, name="김응수", main_lang="java")  # 함수를 호출할 때부터 이렇게 매핑해서 보내면, 순서 상관없이 적재적소로 전달!

profile3("황은비", 24, "자바", "파이썬", "스위프트")
profile3("김소정", 27, "한국어", "영어")
