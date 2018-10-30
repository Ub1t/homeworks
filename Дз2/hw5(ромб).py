n = 0
l = 10
for i in range(2):
    for j in range(3):
        print(" " + " "*l, "*" + "*"*n)
        l -= 1
        n += 2
for i in range(2):
    for j in range(3):
        print(" " + " "*l, "*" + "*"*n)
        l += 1
        n -= 2