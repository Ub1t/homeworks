def f(x):
    if 3 < x < 12:
        return x - 10
    else:
        return x + 10
def fr():
    loop = True
    ran = -5
    while -5 <= ran < 5:
        print("f(", ran, ") = ", f(ran), sep='')
        ran += 0.5
fr()
