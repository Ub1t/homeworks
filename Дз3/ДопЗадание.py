run = True
def s_arif(a, b, c):
    print("({} + {} + {}) / 3 =".format(a, b, c), (a + b + c) / 3)
while run:
    run1 = True
    s1 = int(input("Введите первое число >>> "))
    s2 = int(input("Введите второе число >>> "))
    s3 = int(input("Введите третье число >>> "))
    s_arif(s1, s2, s3)
    print()
    while run1:
        s = input("""Хотите повторить?
    1.Да       2.Нет
    >>> """)
        if s == "1":
            run1 = False
        elif s == "2":
            print("Выключение...")
            run = False
            run1 = False
        else:
            print("Повторите ввод!")
