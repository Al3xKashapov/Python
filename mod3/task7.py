n = input()

nomer = list(n)

s = len(n)

for i in range(s):

    if n[i] == '-':

        del nomer[i]

        i + 1

        if n[i] == '(':

            del nomer[i]

            i + 1

            if n[i] == ')':

                del nomer[i]

                i + 1

                if n[i] == ' ':

                    del nomer[i]

                    i + 1
i + 1


N = ''

for el in nomer:

    N += str(el)

print(N)
