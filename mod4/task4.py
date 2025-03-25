def palindrom(word):

    w = word

    i = 0

    j = 0

    d = 0

    if w.count(w[i]) % 2 == 0:

        for i in range(len(w)):

            if w.count(w[j]) % 2 == 0:

                j = j + 1

            elif d != 1:

                d = d + 1

                j = j + 1
            else:
                print("-")
            break
    else:
        print("-")


palindrom('')


palindrom('')
