import math


def roots(a, b, c):
    if a == 0:
        print("Это не квадратное уравнение")
    else:
        disc = b ** 2 - 4 * a * c
        if disc > 0:
            root1 = (-b + math.sqrt(disc)) / (2 * a)
            root2 = (-b - math.sqrt(disc)) / (2 * a)
            print("Два корня:", root1, "и", root2)
        elif disc == 0:
            root = -b / (2 * a)
            print("Один корень:", root)
        else:
            print("Нет корней")


a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
roots(a, b, c)
