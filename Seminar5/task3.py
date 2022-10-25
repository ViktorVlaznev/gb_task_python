# Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке.
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают. Список уникальных элементов [1, 4, 2, 3, 6, 7]

from random import randint
listNumbers = [randint(1, 10) for i in range(int(input("Введите длину списка: ")))]
listdDubles = []
for i in range(len(listNumbers)):
    if listNumbers.count(listNumbers[i]) > 1: listdDubles.append(listNumbers[i])
print(f"{listNumbers} => {len(list(set(listdDubles)))}", end=" ")
print(f"элемента совпадают.Список уникальных элементов {list(set(listNumbers))}")