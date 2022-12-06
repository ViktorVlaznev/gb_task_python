# Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

import matplotlib.pyplot as plt
from random import randint

houseSquareList = [randint(100, 300) for i in range(15)]
housePriceList = [randint(3000000, 20000000) for i in range(15)]

housePriceMetreList = [housePriceList[i] /houseSquareList[i] for i in range(15)]

plt.title("График стоимости квадратного метра объектов")
plt.xlabel("Порядковый номер объекта")
plt.ylabel("Стоимость квадратного метра")
plt.plot(housePriceMetreList, 'b.')
line = plt.axline((0, 50000), (1, 50000),color="r")

plt.show()


print(houseSquareList)
print(housePriceList)
print(housePriceMetreList)