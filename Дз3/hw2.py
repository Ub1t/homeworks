from scipy import arange
def f(x):
    if 3 < x < 12:
        return x - 10
    else:
        return x + 10
def fr():
    for i in arange(-5.0, 5.0, 0.5):
        print("f(", i, ") = ", f(i), sep='')
fr()