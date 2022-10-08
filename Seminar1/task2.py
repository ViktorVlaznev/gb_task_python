# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

from math import sqrt

ordinateA = int(input("Введите Х точки А: "))
abscissaA = int(input("Введите Y точки А: "))
ordinateB = int(input("Введите Х точки B: "))
abscissaB = int(input("Введите Y точки B: "))

print(round(sqrt( (ordinateA - ordinateB)**2 + (abscissaA - abscissaB)**2 ), 2))