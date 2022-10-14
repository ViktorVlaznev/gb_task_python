# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from math import ceil

# функция создания массива вводом из консоли
def getArray(length):
    array = []
    for i in range(length):
        array.append(int(input(f"Введите {i}-й элемент массива целое число: ")))
    return array

# функция возвращает список из произведений пар элементов первый и последний элемент,
#  второй и предпоследний и т.д.
def getArrCoupleElem(array):
    resArr = []
    for i in range(ceil(len(array)/2)):
        resArr.append(array[i] * array[len(array) - i - 1])
    return resArr

arr = getArray(int(input("Введите длину массива: ")))
print(f"\n{arr} => {getArrCoupleElem(arr)}\n")
