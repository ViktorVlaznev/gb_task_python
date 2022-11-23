# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

from random import randint

# функция создания квадратной матрицы
def CreatMatrix(size, min, max):
    listMatrix =[]
    for i in range(size):
        listMatrix.append([randint(min, max) for i in range(size)])
    return listMatrix

# функция возвращает сумму элементов главной диагонали квадратной матрицы
def GetSumMainDiagonal(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum    

# функция подсчитывает в скольких строк квадратной матрицы сумма элементов превосходит сумму главной диагонали
def GetCountSumRowandMain(matrix):
    count = 0
    for i in range(len(matrix)):
        if GetSumMainDiagonal(matrix) < sum(matrix[i]):
            count += 1
    return count

matrixSize = int(input("Введите размер матрицы: "))
minElement = int(input("Введите минимально возможное значение матрицы: "))
maxElement = int(input("Введите максимально возможное значение матрицы: "))

squareMatrix = CreatMatrix(matrixSize, minElement, maxElement)

print(*squareMatrix, sep="\n")
print(f"Сумма элементов на главной диагонали = {GetSumMainDiagonal(squareMatrix)}")
print(f"В {GetCountSumRowandMain(squareMatrix)} строках(-е) сумма элементов превышает сумму главной диагонали.")