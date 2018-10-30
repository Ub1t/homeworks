print("Введите два числа")
n1 = int(input("Первое число: "))
n2 = int(input("Второе число: "))
if n1 > n2:
    print("Разница чисел равна", n1 - n2)
elif n2 > n1:
    print("Сумма чисел равна", n1 + n2)
else:
    print(n1, "=", n2)