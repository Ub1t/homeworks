print("Дано квадратное уравнение ax² + bx + c = 0")
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
D = b ** 2 - 4 * a * c
if D > 0:
    print("x1 =", (-b + D ** 0.5) / 2 * a)
    print("x2 =", (-b - D ** 0.5) / 2 * a)
elif D == 0:
    print("x =", -b / 2 * a)
else:
    print("Корней нет!")