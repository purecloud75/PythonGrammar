# 클래스는 서로 연관이 있는 변수와 함수의 집합. 붕어빵 틀
# 생성자함수를 호출하면서 Unit클래스의 인스턴스, 즉 붕어빵 하나가 만들어졌습니다
# 매개변수로 받은 매개값을 Unit클래스의 필드 중 하나인 name에 할당하는 모습
# 단 매개변수이름과 필드이름이 같을 때는 구분을 위해 필드명을 굳이 self.필드명 으로 표시해 주는것을 권장한다.
from random import *


class Unit:
    def __init__(self, name, hp, speed):  # 생성자 함수
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} 유닛이 생성되었습니다.".format(self.name))

    def move(self, location):
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 의 데미지를 입었습니다.".format(self.name, damage))
        self.hp = self.hp - damage
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
        else:
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))


class AttackUnit(Unit):  # Unit클래스를 상속받음
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)  # 부모클래스의 생성자함수를 호출하여 객체생성에 관여하는 모습
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" \
              .format(self.name, location, self.damage))  # print()내에서 역슬래시 하나가 갖는 의미는 길 때, 이어서 쓰자!


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            print("{} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("체력이 부족하여 사용불가".format(self.name))


class Tank(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if self.seize_mode == False:
            print("{} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):  # 다중상속. 이 클래스가 제일 자식클래스이고, 가장 많은걸 가지고 있다.
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상속도가 0 이라는 의미
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == False:
            print("{} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True
        else:
            print("{} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    print("Player : GG")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")
