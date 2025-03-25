def nod(a, b):

    a = int(a)

    b = int(b)

    d = 0

    if a > b:

        while d != 1:

            c = a % b

            if c != 0:

                a = c

                b = b % c

            else:

                d = d + 1

                print(b)
    else:

        while d != 1:

            c = b % a

            if c != 0:

                b = c

                a = a % c

            else:

                d = d + 1

                print(a)


nod(30, 18)

nod(18, 30)
