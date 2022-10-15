# В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

data = open("task2.txt", encoding="utf-8")
textFruit = data.read()
listFruit = list(filter(None, list(set(textFruit.split("\t")))))
beginChar = input("Введите первую букву названия фруктов: ")
print(f"{beginChar} ->", end=" ")
for fruit in listFruit:
    if beginChar.lower() == fruit[0].lower():
        print(fruit, end=", ")
print()
data.close()
