# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

# функция возвращает значение n-ого члена чисел Фибоначи
def GetFibonachi(number):
    if number == 1 or number == 2:
        return 1
    else: 
        return GetFibonachi(number - 1) + GetFibonachi(number - 2)

numberFib = abs(int(input("Введите число: ")))
arrFibNeg = []
arrFibPos = []
for i in range(1, numberFib + 1):
    arrFibNeg.append(((-1) ** (i + 1)) * GetFibonachi(i))
    arrFibPos.append(GetFibonachi(i))
arrFibNeg.reverse()
arrFibNeg.append(0)
arrFib = arrFibNeg + arrFibPos
print(arrFib)