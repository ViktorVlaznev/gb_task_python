# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

# функция возвращает список простых чисел до number
def GetListPrimeNumber(number):
    listPrimeNumber = []
    for num in range(2, number + 1):
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            listPrimeNumber.append(num)
    return listPrimeNumber

# функция возвращает список простых множителей числа
def GetListSimpleDivisors(number):
    listSimpleDivisors = []
    listPrimeNumber = GetListPrimeNumber(int(number / 2))
    for elem in listPrimeNumber:
        while  number % elem == 0:
            listSimpleDivisors.append(elem)
            number = number / elem
    return listSimpleDivisors

inputNumber = int(input("Ввдеите целое число: "))
if inputNumber > 0:
    print(f"{inputNumber} -> {GetListSimpleDivisors(inputNumber)}")
else: print("Введено не натуральное число.")