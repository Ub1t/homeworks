from random import randint
def shif():
    b = -1
    loop = True
    loop2 = True
    while loop:
        try:
            s = int(input("Введите число >>> "))
            loop = False
        except ValueError:
            print("Ошибка!")
    while loop2:
        ss = input("Введите строку >>>")
        loop2 = False
    c = 0
    for i in str(s):
        c += len(ss) / len(str(s))
        f = randint(b + 1, int(c))
        b = f
        ss
        ss = list(ss)
        ss.insert(f, i)
    print('Результат:', ''.join(ss))
    return ss
def deshif(x):
    k = []
    l = 0
    for i in x:
        if i.isalpha() or i == ' ':
            k.extend(i)
            del x[l]
            x.insert(l, '')
            l +=1
        else:
            l += 1
    print("Число: {}".format(''.join(x)))
    print("Строка: {}".format(''.join(k)))
deshif(shif())