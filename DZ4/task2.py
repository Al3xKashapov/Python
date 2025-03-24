def fastSt(a, n):

    if (n % 2) == 0:

        print(int((a ** 2) ** (n / 2)))

    else:

        print(int(a * a ** (n - 1)))


fastSt(2, 0)

fastSt(2, 8)

fastSt(2, 3)
