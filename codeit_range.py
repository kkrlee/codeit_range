numbers = [2, 3, 5, 7, 11, 13, 17, 19]
for i in range(len(numbers)):
    print(i, numbers[i])

for i in range(0, 11):
    print("%d^%d = %d" % (2, i, 2**i))

for i in range(1, 10):
    for j in range(1, 10):
        print("%d * %d = %d" % (i, j, i * j))

for a in range(1, 333):
    for b in range(a + 1, 500):
        c = 1000 - a - b
        if (a ** 2 + b ** 2 == c ** 2):
            print(a * b * c)
