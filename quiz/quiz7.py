class SoldoutError(Exception):
    pass


chicken = 10
waiting = 1
while True:
    try:
        if chicken == 0:
            raise SoldoutError
        print("남은 치킨은 {} 마리 입니다.".format(chicken))
        order = int(input("몇 마리 주문 하시겠습니다? "))
        if order <= 0:
            raise ValueError
        elif order > chicken:
            print("재료가 부족합니다.")
        else:
            print("대기번호 {}이시고, {} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
    except ValueError as err:
        print(err)
    except SoldoutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
