# Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.

import numpy as np

try:
    size = int(input("Введите размер квадратного массива: "))
    min = int(input("Введите минимально возможное значение списка: "))
    max = int(input("Введите максимально возможное значение списка: "))
    random_list = np.random.randint(min,max + 1, (size,size))
    print("Данный список элементов:")
    print(random_list)
    print("Одинаковые строки есть." if (random_list == random_list[0]).all() else "Одинаковыx строк нет.")
except:
    print("Введено не число. Перезапустите программу.")