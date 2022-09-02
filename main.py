# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


a = [156, "apple", True]  # 리스트
b = {1: "love", "A": 65, "A-3": "secret"}  # 딕셔너리(의미는 사전)
c = {3, 3, 3, 5, 6, 8, "midori"}  # 집합(중복불가 순서무관)
d = ("홍길동", 30)  # 튜플(변경 및 추가 불가)
print(a)
print(b)
print(c)
print(d)

print(c, type(c))
c = list(c)
print(c, type(c))
c = set(c)
print(c, type(c))
