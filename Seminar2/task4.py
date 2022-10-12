# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

number = abs(int(input("Введите число диапазона: ")))
shift = int(input("Введите число смещения: "))
listNumber = []
for i in range(-number, number + 1):
    listNumber.append(i)
print(listNumber[len(listNumber)-shift:] + listNumber[:len(listNumber)-shift])