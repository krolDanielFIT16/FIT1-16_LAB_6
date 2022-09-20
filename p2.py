import math


def func(x):
    return math.fabs(math.tan(math.fabs(x) + 0.1))


a = float(input("a = "))
b = float(input("b = "))
h = float(input("h = "))

x = a
while x < b:
    print(x, func(x))
    x += h
