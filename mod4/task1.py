def numCheck(numList):

    n = list(map(int, numList.split()))

    s = len(n)

    n = set(n)

    if len(n) == 1:

        print("Все числа равны")

    elif len(n) == s:

        print("Все числа разные")

    else:
        print("Есть равные и неравные числа")


numCheck('1 1 1 1')

numCheck('1 0 1 1')

numCheck('1 2 3 4')
