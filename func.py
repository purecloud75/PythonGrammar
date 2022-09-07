def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balanc, money):
    print("입급이 완료되었습니다. 잔액은 {0}원 입니다.".format(balanc + money))
    return balanc + money


def withdraw(balanc, money):
    if balanc >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balanc - money))
        return balanc - money
    else:
        print("출금 불가. 다시 시도하세요. 잔액은 {0}원입니다.".format(balanc))
        return balanc


def withdraw_night(balanc, money):
    commissio = 100
    return commissio, balanc - money - commissio  # 두 개 이상을 동시에 반환가능하다


open_account()
balance = 0
balance = deposit(balance, 5600)
balance = withdraw(balance, 2000)
print(balance)
balance = withdraw(balance, 4000)
print(balance)
commission, balance = withdraw_night(balance, 500)  # 튜플 형식으로 여러개의 반환값을 동시에 받기가 가능
print(f"수수료는 {commission}이며, 잔액은 {balance}입니다.")
