# Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial

number = int(input("Введите число: "))
listFactorial = []
listFactorialstr = []
for i in range(1, number+1):
    listFactorial.append(factorial(i))
    strFactorial = "1"
    for j in range(2, i+1):
        strFactorial += f"*{j}"
    listFactorialstr.append(strFactorial)
print(listFactorial, end=" (")
print(*listFactorialstr, end=")\n", sep=", ")