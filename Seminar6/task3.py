# Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11

# функция возвращает список простых чисел до number
def GetListPrimeNumber(number):
    listPrimeNumber = [1]
    for num in range(2, number + 1):
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            listPrimeNumber.append(num)
    return listPrimeNumber

# функция возвращает список простых несократимых дробей
def  GetIrreducibleFractionPrimeNumbers(number):
    listPrimeNumber =  GetListPrimeNumber(number)
    listFraction = []
    for i in range(len(listPrimeNumber)):
        for j in range(i,len(listPrimeNumber)):
            if i != j:
                listFraction.append(str(listPrimeNumber[i]) + "/" + str(listPrimeNumber[j]))
    return listFraction

maxPrimeNumber = 11
print(GetIrreducibleFractionPrimeNumbers(maxPrimeNumber))