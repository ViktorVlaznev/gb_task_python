# Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

from random import randint

lengthList = int(input("Введите длину списка: "))
listNumbers = [randint(1, 10) for i in range(lengthList)]
resultList = []
firstIndex = randint(0, lengthList - 1)
minIndex, maxValue, nextIndex = firstIndex, listNumbers[firstIndex], randint(firstIndex + 1, lengthList)
resultList.append(maxValue)
while nextIndex < lengthList:
    if (listNumbers[nextIndex] > maxValue):
        resultList.append(listNumbers[nextIndex])
        maxValue = listNumbers[nextIndex]
    firstIndex, nextIndex = nextIndex, randint(firstIndex + 1, lengthList)
print(listNumbers, " => ", resultList)
