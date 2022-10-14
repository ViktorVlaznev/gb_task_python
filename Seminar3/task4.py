# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# решение 1
# функция возвращает двоичное представление десятичного числа
def getNumberfromDecinBinar(number):
    result = ""
    while number > 0:
        result += str(number % 2)
        number =  int(number / 2)
    return "".join(reversed(result))

numberDec = int(input("Введите число: "))
print(f"- {numberDec} -> {getNumberfromDecinBinar(numberDec)}")

#решение 2
print(f"- {numberDec} -> {format(numberDec, 'b')}")