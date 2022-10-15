# Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

# функция возвращает n-ый член последовательности Фибоначи
def getFibonachi(number):
    result = 0
    resultNext = 1
    for i in range(1, number + 1):
        temp = result
        result += resultNext
        resultNext = temp
    return result

num = int(input("Введите целое число: "))
data = open("task1.txt", "w")
strFib = f"{num} -> "
for i in range(num + 1):
    strFib += str(getFibonachi(i)) + " "
data.write(strFib)
data.close()