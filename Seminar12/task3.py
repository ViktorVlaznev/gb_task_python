# Создайте двумерный массив случайного размера. Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

import numpy as np
from random import randint

try:
    min = int(input("Введите минимально возможное значение списка: "))
    max = int(input("Введите максимально возможное значение списка: "))
    row = randint(1, 10)
    col = randint(1, 10)
    random_list = np.random.randint(min,max, (row,col))
    max_index = np.argmax(random_list)
    index_row_max = ((max_index + 1) // col) + 1
    index_col_max = ((max_index + 1) // row) + 1
    print(random_list)
    print(f"Максимальный элемент стоит  в {index_row_max} ряду и в {index_col_max} столбце.")
    print()
    min_index = np.argmin(random_list)
    index_row_min = ((min_index + 1) // col) + 1
    index_col_min = ((min_index + 1) // row) + 1
    print(random_list)
    print(f"Минимальный элемент стоит  в {index_row_min} ряду и в {index_col_min} столбце.")
    print()
    print(f"Список элемнтов главной оси равен {np.diagonal(random_list)}")
except:
    print("Введено не число. Перезапустите программу.")