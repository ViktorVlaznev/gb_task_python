# Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

import numpy as np

try:
    size = int(input("Введите размер списка: "))
    min = int(input("Введите минимально возможное значение списка: "))
    max = int(input("Введите максимально возможное значение списка: "))
    random_list = np.random.randint(min,max + 1, size)
    num_unique = np.unique(random_list)
    print("Данный список элементов:")
    print(random_list)
    print()
    print("Cписок уникальных элементов: ")
    print(num_unique)
    print()
    print(f"Количество уникальных элементов данного списка равно {len(num_unique)}.")
except:
    print("Введено не число. Перезапустите программу.")