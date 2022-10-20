# В первой строке файла находится информация об ассортименте мороженного, во второй 
# - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

# функция возрастает список отсутствующих элементов в проверяемой списке относительно основного списка
def GetMissingListItems(listGeneral, listChecked):
    listMissingListItems = []
    for elem in listGeneral:
        flag = False
        for el in listChecked:
            if el == elem:
                flag = True
                break
        if flag == False:
            listMissingListItems.append(elem)
    return listMissingListItems

with open("icecream.txt", encoding="utf-8") as data:
    wholeRange = data.readline()[:-1]
    inStock = data.readline()
    print(f"1. {wholeRange}")
    print(f"2. {inStock}")
    print("Закончилось:", end=" ")
    print(*GetMissingListItems(wholeRange.split(', '), inStock.split(', ')), sep=", ")