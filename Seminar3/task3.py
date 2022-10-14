# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# функция создания массива c вещественными числовыми элементами вводом из консоли
def getRealArray(length):
    array = []
    for i in range(length):
        array.append(float(input(f"Введите {i}-й элемент массива целое число: ")))
    return array

# функция возвращает массив с элементами без целой части числа
def getArrwithoutWholePart(array):
    for i in range(len(array)):
        array[i] = array[i] % 1
    return array

arr = getRealArray(int(input("Введите длину массива: ")))
print(f"- {arr} => {round(max(getArrwithoutWholePart(arr)) - min(getArrwithoutWholePart(arr)), 2)}")