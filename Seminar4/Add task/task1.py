# Даны три числовых массива. Реализуйте метод, в который определяет 
# в каком из первых двух массивов чаще всего встречаются элементы третьего.

import random

# функция возвращает список случайных чисел из указанного диапазона, заданной длины
def GetListIntRandom(min, max, length):
    listResult =[]
    for i in range(length):
        listResult.append(random.randint(min, max))
    return listResult

# функция возвращает кол-во одинаковых чисел в двух массивах
def GetCountMatchingElements(list1, list2):
    list1 = list(set(list1))
    list2 = list(set(list2))
    counter = 0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                counter += 1
    return counter

minElement = int(input("Введите минимальное значение списка: "))
maxElement = int(input("Введите максимальное значение списка: "))
lengthList = int(input("Введите длину списка: "))
list1 = GetListIntRandom(minElement, maxElement, lengthList)
list2 = GetListIntRandom(minElement, maxElement, lengthList)
list3 = GetListIntRandom(minElement, maxElement, lengthList)

print(list1)
print(list2)
print(list3)
print(GetCountMatchingElements(list1, list3))
print(GetCountMatchingElements(list2, list3))
if GetCountMatchingElements(list1, list3) > GetCountMatchingElements(list2, list3):
    print("В первом массиве больше одинаковых чисел с третьим массивом")
elif GetCountMatchingElements(list1, list3) < GetCountMatchingElements(list2, list3):
    print("Во втором массиве больше одинаковых чисел с третьим массивом")
else:  print("Равно")
