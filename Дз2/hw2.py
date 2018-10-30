while True:
    s = 1
    n = int(input("Введите число факториал, которого мы ищем >>> "))
    if n <= 0:
        print("Введите заново!")
    else:
        for i in range(1, n + 1):
            s *= i
        print(str(n) + "!", "=", s)
        break