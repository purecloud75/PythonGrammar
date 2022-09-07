x = 10


def check():
    a = 30
    global x
    x = 100
    print(x)
    print(a)
    return


if True:
    b = 40

check()
# print(a) 오류
print(b)
print(x)
