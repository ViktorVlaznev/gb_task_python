# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

from statistics import mean
from random import randint

numbersGroup = int(input("Введите количество групп: "))
listReportCard = []
listMean = []

for i in range(numbersGroup):
    listReportCard.append([randint(1, 5) for i in range(randint(20, 30))])
    listMean.append(mean(listReportCard[i]))

print(*listReportCard, sep='\n')
print(f"Группа с наилучшим средним баллом - {listMean.index(max(listMean)) + 1}")