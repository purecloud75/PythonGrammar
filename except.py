class MyErrorClass(Exception):  # 사용자 정의 예외처리
    pass


try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자 입력하세요 : "))
    num2 = int(input("두번째 숫자 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise MyErrorClass  # 문법상 오류가 없더라도, 사용자의 의도와 다르게 흘러갈 시 일부러 에러를 발생시킬 수도 있다.
    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))

except MyErrorClass:
    print("잘못된 값을 입력하였으니, 한 자리 숫자만 입력하세요")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)

finally:  # 앞에서 에러가 발생하던 안하던 알바아니고 무조건 여기 구문을 전부 다 실행된다.
    print("계산기 기능을 종료합니다.")

# 자바하고 거의 비슷함. try 내의 코드를 쭉 진행하다가 에러가 있다? 해당되는 except로 가서 거기의 코드를 실행시킨다.
# Exception은 모든에러의 총집합이니 가장 아래에 두고 쓰자. 그래서 어떤 에러로 여기로 온건지 정확히 알기 어렵다.
# 하지만 Exception이라도 뒤에 as arr 해주고 이를 출력하면 더 자세한 에러사항 알려주기에 사용하기 좋아보인다.

# 이걸 왜 하나면 예측가능한(예측이 힘들면 그냥 Exception 하면되고) 범위 내에서 에러가 발생 시, 프로그램이 자동으로 종료되는 것을 막고,
# except 로 내려가서 내가 적어놓은 구문을 실행시키고 이어서 마저 진행할 수 있도록 하기위함이다. 프로그램 종료 막을려고 하는거임
