'#В единственной строке записаны три целых числа'
'#a, b, c (−1000≤a,b,c≤1000), числа разделены одиночными пробелами.'

'#print("Введите числа через пробел"'

'#Ввод и преобразование в список'

Array = input("Введите числа через пробел:\n").split()

'#Сортировка'

n = len(Array)

for i in range(n):

    for j in range(0, n - i - 1):

        if Array[j] > Array[j + 1]:

            Array[j], Array[j + 1] = Array[j + 1], Array[j]
                        
print(Array[1])
