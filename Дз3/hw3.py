def sl(a, b):
    print(a, "+", b, "=", a + b)
def minus(a, b):
    print(a, "-", b, "=", a - b)
def s(a, b):
    print(a, "*", b, "=", a * b)
def d(a, b):
    while True:
        if b == 0:
            print("Введите второе число заново! Деление на ноль не возможно")
            b = float(input("Введите второе число >>>"))
            continue
        else:
            print(a, "/", b, "=", a / b)
            break
while True:
    v = input("""Выберите действие:
    1. Сложение
    2. Вычитание
    3. Умножение
    4. Деление
    5. Выход
    >>> """)
    if v == "5":
        print("Выход...")
        break
    elif v == "1" or v == "2" or v == "3" or v == "4":
        z = float(input("Введите первое число >>>"))
        zz = float(input("Введите второе число >>>"))
        if v == "1":
            sl(z, zz)
        elif v == "2":
            minus(z, zz)
        elif v == "3":
            s(z, zz)
        elif v == "4":
            d(z, zz)
    else:
        print("Выберите заново!")
