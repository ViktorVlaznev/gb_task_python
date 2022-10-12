# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

str1 = input()
str2 = input()

#решение 1
for i in set(str1):
    counter = 0
    for j in str2:
        if i == j:
            counter += 1
    print(f"{i} - {counter}")

#решение 2
for i in set(str1):
    print(f"{i} - {str2.count(i)}")