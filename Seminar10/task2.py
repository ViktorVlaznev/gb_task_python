# Добавьте боту модуль, который позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.
import task1
from tkinter import *
from tkinter import ttk

root = None
frm = None
input = None
label = None
def createMenu():
    global root
    global frm
    global input
    global label
    CreateForms("Техническая поддержка")
    label = ttk.Label(frm, text=PrintQuestion()).grid(column=0, row=0)
    input = ttk.Entry(frm)
    input.grid(column=0, row=1)
    ttk.Button(frm, text="Ответить", command=SendAnswer).grid(column=0, row=2)
    root.mainloop()

# функция создает форму
def CreateForms(title):
    global root
    global frm
    root = Tk()
    root.title(title)
    root.iconbitmap(default="favicon.ico")
    frm = ttk.Frame(root, padding=30)
    frm.grid()
    ttk.Button(frm, text="Закрыть", command=root.destroy).grid(column=2, row=1000)

# функция возвращает первую строку из файла
def PrintQuestion():
    try:
        data = open('user_support.txt', 'r+', encoding='utf-8')
        question = data.readlines()
        question1 = question[0]
        data.close()
        return question1
    except:
        return "Обращений нет."

# функция отправляет сообщение пользователю, удаляет обращение из файла и отврывает форму с новым обращением
def SendAnswer():
    task1.bot.send_message(PrintQuestion().split(" ")[1], f"Ответ на Ваше обращение от {PrintQuestion()}: {input.get()}")
    DeleteFirstString('user_support.txt')
    createMenu()

# функция удаляет первую строку из файла
def DeleteFirstString(file):
    with open(file, 'r') as start:
        data = start.read().splitlines(True)
    start.close()
    with open(file, 'w') as finish:
        finish.writelines(data[1:])
    finish.close()

createMenu()