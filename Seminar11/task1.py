# Постройте график функции𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

# функция для нахождения корней квадратного уравнения
def solve(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return (x1, x2)
    else:
        return 'Вещественных корней нет'

zeroList = solve(5,10,-30)

plt.title("График функции")
plt.xlabel("Ось Х")
plt.ylabel("Ось У")

x = np.linspace(-15, 15, 201)
y = lambda x: 5 * x ** 2 + 10 * x - 30
line, = plt.plot(x, y(x))
line.set_label("f(x)=5x^2+10x-30")
line = plt.axline((0, 0), (1, 0),color="r")
line.set_label(f"Отрицательный участок функции от {round(zeroList[1],2)} до {round(zeroList[0],2)}")
line = plt.axline((0, 0), (0, 1),color="g")
plt.legend()
plt.show()