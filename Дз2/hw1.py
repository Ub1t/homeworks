while True:
    a = int(input("Введите первое число >>> "))
    b = int(input("Введите второе число >>> "))
    if a > b:
        print("Введите заново!")
    elif a < 0:
        print("Введите заново!")
    else:
        for i in range(a, b + 1):
            print(i)
            continue