import math


def func(x):
    return math.fabs(math.tan(math.fabs(x)+0.1))


a = int(input("a = "))
b = int(input("b = "))
h = int(input("h = "))

for i in range(a, b, h):
    print(i, func(i))