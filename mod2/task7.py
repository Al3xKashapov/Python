si = input("Введите данные через запятую\n")

d = 0

for j in range(len(si)):

    if si[j] == ',':

        s = si[:j]

        c = j + 1

        i = si[c:]

for j in range(2):

    if s[j] == i:

        d = d + 1
print("количество ", i, " =", d)
