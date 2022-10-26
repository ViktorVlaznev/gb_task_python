# Создайте игру в крестики-нолики.

listBoard = list(range(1,10))

# функция рисует игровое поле
def DrawBoard(list):
    print ("-" * 13)
    for i in range(3):
        print ("|", list[0 + i * 3], "|", list[1 + i * 3], "|", list[2 + i * 3], "|")
        print ("-" * 13)

# функция ввода хода игрока
def GetPlayerChoice(choice, list):
    valid = False
    while not valid:
        answer = int(input("Куда поставим " + choice + "? "))
        if answer >= 1 and answer <= 9:
            if (str(list[answer - 1]) not in "XO"):
                list[answer - 1] = choice
                valid = True
            else:
                print ("Эта клетка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9, чтобы продолжить.")

# функция проверяет выйгрышную ситуацию
def checkWin(board):
    winComb = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for elem in winComb:
        if board[elem[0]] == board[elem[1]] == board[elem[2]]:
            return board[elem[0]]
    return False

# функция реализации порядка игры
def mainGame(list):
    counter = 0
    win = False
    while not win:
        DrawBoard(list)
        if counter % 2 == 0:
            GetPlayerChoice("X", list)
        else:
            GetPlayerChoice("O", list)
        counter += 1
        if counter > 4:
            check = checkWin(list)
            if check:
                print (check, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    DrawBoard(list)

mainGame(listBoard)