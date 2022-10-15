# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:  - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# функция создания массива c целочисленными элементами вводом из консоли
def getIntArray(length):
    array = []
    for i in range(length):
        array.append(int(input(f"Введите {i}-й элемент массива целое число: ")))
    return array

# функция находит сумму элементов массива на нечётных позициях
def sumElemArrayinOddIndex(array):
    sum = 0
    for i in range(1, len(array), 2):
        sum += array[i]
    return sum

# функция выводит на печать элементы массива с нечётными индексами
def printElemArrayinOddIndex(array):
    for i in range(1, len(array), 2):
        if i == 1:
            print(array[i], end=" и ")
        elif i < len(array) - 2:
            print(array[i], end=", и ")
        else: print(array[i], end="")

arr = getIntArray(int(input("Введите длину массива: ")))

print(f"\n - {arr} -> на нечётных позициях элементы ", end=" ")
printElemArrayinOddIndex(arr)
print(f", ответ: {sumElemArrayinOddIndex(arr)}\n")