# Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x
# 2. 3x^2 + x + 8
# Результат: 8x^2 + 4x + 8

import re

# функция возвращает список пар коэффициент и степень
def GetlistCoefPolinom(str):
    list = str.split(" + ")
    listCoef = []
    for elem in list:
        if elem.isdigit() == True:
            listCoef.append([elem, "0"])
        else:
            listCoef.append(re.findall(r'\d+', elem))
    for elem in listCoef:
        if len(elem) == 1:
            elem.append("1")
        if len(elem) == 0:
            elem.append("1")
            elem.append("1")
    return listCoef

# функция возвращает список коэфициентов и степеней приведенный к однородным членам
def GetlistNormalCoefPolinom(list):
    count = 0
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i][1] == list[j][1]:
                list[i] = [str(int(list[i][0]) + int(list[j][0])), list[i][1]]
                count += 1
    for k in range(1, count + 1):
        list.pop()
    return list

def PrintPolinomfromList(list):
    strPolinom = ""
    for i in range(len(list)):
        if list[i][1] != "0":
            list[i] = list[i][0] + "x^" + list[i][1]
            strPolinom += list[i] + " + "
        else:
            list[i] = list[i][0]
            strPolinom += list[i]
    return strPolinom
    

with open("polinom1.txt") as polinom1:
    strPolinom1 = polinom1.readline()
    print("1. ",strPolinom1)
    listPolinom1 = GetlistNormalCoefPolinom(GetlistCoefPolinom(strPolinom1))

with open("polinom2.txt") as polinom2:
    strPolinom2 = polinom2.readline()
    print("2. ",strPolinom2)
    listPolinom2 = GetlistNormalCoefPolinom(GetlistCoefPolinom(strPolinom2))

listSum = GetlistNormalCoefPolinom(listPolinom2 + listPolinom1)
print("Результат: ", PrintPolinomfromList(listSum))