N = input("Введите число \n")

i = 0

j = 0

s = len(N)

n = 0

for n in range(s):

    if N[n] == '1':

        i = i + 1

    else:
        j = j + 1

# print(i, j)

if i == j:
    print("yes")
else:
    print("no")
