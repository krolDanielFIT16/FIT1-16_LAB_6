import math


def func(x):
    return math.fabs(math.tan(math.fabs(x) + 0.1))


a = float(input("a = "))
b = float(input("b = "))
h = float(input("h = "))

arr1 = []
arr2 = []

x = a
while x < b:
    arr1.append([x, func(x)])                   # додаємо у перший масив аргумент та значення функції
    arr2.append(arr1[-1][0] * arr1[-1][1])      # додаємо у другий масив добуток елементів з першого
    x += h

print(arr1)
print()
print(arr2)
