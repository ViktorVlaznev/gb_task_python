# В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный 7-дневный 
# промежуток этого периода. Выведите его даты.

from random import randint
from statistics import mean
import datetime

# функция определения кол-ва дней в месяце в не високосном году
def GetDaysMonth(num):
    listMonthDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return listMonthDay[num] if 0 <= num <= 11 else -1

# функция создания двумерного массива температур
def CreatMatrixTemp(startMonth, endMonth, minTemp, maxTemp):
    listMatrix =[]
    for i in range(startMonth, endMonth + 1):
        listMatrix.append([randint(minTemp, maxTemp) for j in range(GetDaysMonth(i))])
    return listMatrix

# функция разворачивает двухмерный массив в одномерный
def CreateListTwoDimensionaltoOneDimensional(listTwoDimensional):
    listOneDimension = []
    for i in range(len(listTwoDimensional)):
        for j in range(len(listTwoDimensional[i])):
            listOneDimension.append(listTwoDimensional[i][j])
    return listOneDimension

# возвращает список с двумя элементами(макс индекс, мин индекс) для средних значений срезов списка
def GetMinMaxIndexListSlice(list, slice):
    max = min = mean(list[:slice])
    listIndex = [0, 0]
    for i in range(len(list) - slice):
        if max < mean(list[i : i + slice]):
            max = mean(list[i : i + slice])
            listIndex[0] = i
        if min > mean(list[i : i + slice]):
            min = mean(list[i : i + slice])
            listIndex[1] = i
    return listIndex

startMonth = int(input("Введите номер первого месяца: "))
endMonth = int(input("Введите номер последнего месяца: "))
minTemp = int(input("Введите минимально возможное значение температуры: "))
maxTemp = int(input("Введите максимально возможное значение температуры: "))
timeInterval = int(input("Введите временной интервал: "))
dateStart = datetime.date(2022, startMonth, 1)

listTempTwoDim = CreatMatrixTemp(startMonth - 1, endMonth - 1, minTemp, maxTemp)
print(*listTempTwoDim, sep="\n")

listTempOneDim = CreateListTwoDimensionaltoOneDimensional(listTempTwoDim)
listMinMax = GetMinMaxIndexListSlice(listTempOneDim, timeInterval)

dateMaxStart = dateStart + datetime.timedelta(days=listMinMax[0])
dateMaxEnd = dateMaxStart + datetime.timedelta(days=timeInterval)
dateMinStart = dateStart + datetime.timedelta(days=listMinMax[1])
dateMinEnd = dateMinStart + datetime.timedelta(days=timeInterval)

print(f"Cамый жаркий {timeInterval}-дневный промежуток этого периода был с {dateMaxStart} по {dateMaxEnd}.")
print(f"Cамый холодный {timeInterval}-дневный промежуток этого периода был с {dateMinStart} по {dateMinEnd}.")
