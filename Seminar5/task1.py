#Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. 
#Используйте для решения лямбда-функцию.
#2, 3, 4, 6, 7, 8 -> 6, 7, 8

from random import randint

listNumbers = [randint(1, 10) for i in range(int(input("Введите длину списка: ")))]
print(*listNumbers, sep=", ", end=" " + " -> ")
print(*list(filter(lambda x: x > 5, listNumbers)), sep=", ")
