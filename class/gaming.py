from starcraft import *

# import 뒤에 *이 오면 starcraft.py 에 정의된 모든 함수와 클래스에 접근가능하다는 의미이고,
# 특정 함수명과 클래스명을 적어서 그것만 가져올 수도 있다.
# 만약에 import starcraft as st 라고 했으면 각 문장의 앞마다 st.을 다 붙였어야 한다
# (그나마 as st 라도 없었으면 starcraft. 를 모든 문장에 다 붙여야하는 재앙이 일어난다....)

# 모듈 : 필요한것들끼리 부품처럼 잘 만들어진 파일. 부품만 교체 및 추가하면 유지보수 쉽고 코드의 재사용이 쉽다.
# 함수정의나 클래스 등의 파이썬 문장들을 담고있는 파일을 모듈이라고하고, 확장자는 .py 이다.

# 패키지는 모듈들을 모아놓은 집합이다.

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 공격 모드 준비 (마린은 스팀팩,탱크는 시즈모드, 레이스는 클로킹모드 발동)
for unit in attack_units:
    if isinstance(unit, Marine):  # 리스트의 요소인 unit이 Marine클래스의 객체(인스턴스)인지 확인한 후에 진행
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20))  # 공격은 랜덤으로 받음

# 다 죽어서 게임종료
game_over()
