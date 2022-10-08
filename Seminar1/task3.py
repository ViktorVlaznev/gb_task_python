# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

# решение 1
quarter = int(input("Введите номер четверти: "))
dicQuarter = {1: "x > 0, y > 0", 2: "x < 0, y > 0", 3: "x < 0, y < 0", 4: "x > 0, y < 0"}
if 1 <= quarter <= 4:
    print(dicQuarter[quarter])
else:
    print("Введен не номер четверти")

# решение 2
listQuarter = ["x > 0, y > 0", "x < 0, y > 0", "x < 0, y < 0", "x > 0, y < 0"]
if  1 <= quarter <= 4:
    print(listQuarter[quarter - 1])
else:
    print("Введен не номер четверти")

# решение 3
if quarter == 1:
    print("x > 0, y > 0")
elif quarter == 2:
    print("x < 0, y > 0")
elif quarter == 3:
    print("x < 0, y < 0")
elif quarter == 4:
    print("x > 0, y < 0")
else:
    print("Введен не номер четверти")