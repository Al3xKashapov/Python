s = input("Введите числа через пробел:\n").split()


for i in range(len(s)):

    if s[i] != s[(i+1)]:

        s = False

    else:

        s = True

        break


print(s)
