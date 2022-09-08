def game_start():
    print("새로운 게임을 시작합니다.")


def game_over():
    pass


game_start()
game_over()


# 함수든 클래스내의 생성자 혹은 메소드든간에 정의를 해놓지 않아도, pass 키워드 하나만 적어주면
# 일단은 오류없이 프로그램이 돌아가게 해준다. 물론 정의는 안하고 pass만 적었으니 의미는 없겠지만. 정의를 안해주면 그 자체로 오류이다.


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)  # 2 lines are totally same
        super().__init__(name, hp, 0)
        # super()를 쓸때는 self를 인자로 안 넣는다. 단 해당클래스가 2개 이상의 클래스를 상속받는 경우(다중상속)에는 쓰지 않는다.
        self.location = location
