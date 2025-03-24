'#На вход подается доменное имя сайта. Необходимо вывести все домены по'
' порядку начиная с домена первого уровня.'

Domen = input()

d = 0

s = len(Domen)

for i in range(s):

    if Domen[i] == '.':

        d = i

        break

d1 = Domen[(d+1):]

d = Domen[:d]

for i in range(len(d1)):

    if d1[i] == '.':

        d2 = i

        break
j = d2

d2 = d1[(d2+1):]

d1 = d1[:j]

print(d2, d1, d)
