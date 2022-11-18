import model
from tkinter import *
from tkinter import ttk

root = None
frm = None
inputName = None
inputPatronymic = None
inputBirthday = None
inputNumberTel = None

# Создает основное меню
def createMenu():
    global root
    global frm
    global textSurname
    global inputSurname
    global inputName
    global inputPatronymic
    global inputBirthday
    global inputNumberTel
    root = Tk()
    root.title("Телефонный справочник")
    root.iconbitmap(default="favicon.ico")
    frm = ttk.Frame(root, padding=30)
    frm.grid()
    ttk.Label(frm, text="Фамилия").grid(column=0, row=0)
    ttk.Label(frm, text="Имя").grid(column=1, row=0)
    ttk.Label(frm, text="Отчество").grid(column=2, row=0)
    ttk.Label(frm, text="Дата рождения").grid(column=3, row=0)
    ttk.Label(frm, text="Номер телефона").grid(column=4, row=0)
    inputSurname = ttk.Entry(frm)
    inputSurname.grid(column=0, row=1)
    inputName = ttk.Entry(frm)
    inputName.grid(column=1, row=1)
    inputPatronymic = ttk.Entry(frm)
    inputPatronymic.grid(column=2, row=1)
    inputBirthday = ttk.Entry(frm)
    inputBirthday.grid(column=3, row=1)
    inputNumberTel = ttk.Entry(frm)
    inputNumberTel.grid(column=4, row=1)
    ttk.Button(frm, text="Добавить", command=model.AddContact).grid(column=0, row=2)
    ttk.Button(frm, text="Поиск", command=SearchContact).grid(column=1, row=2)
    ttk.Button(frm, text="Показать все", command=PrintFromFile).grid(column=2, row=2)
    ttk.Button(frm, text="Экспорт в HTML", command=model.ExportHTML).grid(column=3, row=2)
    ttk.Button(frm, text="Закрыть", command=root.destroy).grid(column=4, row=2)
    root.mainloop()

# функция всплывающего окна сообщения
def GetPopupWindow(message, title):
    root = Tk()
    root.title(title)
    root.iconbitmap(default="favicon.ico")
    frm = ttk.Frame(root, padding=30)
    frm.grid()
    ttk.Label(frm, text=message).grid(column=0, row=0)
    ttk.Button(frm, text="Закрыть", command=root.destroy).grid(column=0, row=1)

# функция вывода всего списка из файла
def PrintFromFile():
    root = Tk()
    root.title("Телефонный справочник")
    root.iconbitmap(default="favicon.ico")
    frm = ttk.Frame(root, padding=30, borderwidth=1)
    frm.grid()
    ttk.Button(frm, text="Закрыть", command=root.destroy).grid(column=4, row=1000)
    data = open("contacts.txt", encoding="utf-8")
    contactEntry = data.readlines()
    for i in range(len(contactEntry)):
        for j in range(5):
            if j != 4:
                ttk.Label(frm, text=contactEntry[i].split(" ")[j]).grid(column=j, row=i)
            else: ttk.Label(frm, text=contactEntry[i].split(" ")[j][:-1]).grid(column=j, row=i)
    data.close()

# функция поиска 
def SearchContact():
    root = Tk()
    root.title("Телефонный справочник")
    root.iconbitmap(default="favicon.ico")
    frm = ttk.Frame(root, padding=30)
    frm.grid()
    ttk.Button(frm, text="Закрыть", command=root.destroy).grid(column=4, row=1000)
    data = open("contacts.txt", encoding="utf-8")
    contactEntry = data.readlines()
    for i in range(len(contactEntry)):
        for j in range(5):
            if(inputSurname.get() == contactEntry[i].split(" ")[0] or
            inputName.get() == contactEntry[i].split(" ")[1] or
            inputPatronymic.get() == contactEntry[i].split(" ")[2] or
            inputBirthday.get() == contactEntry[i].split(" ")[3] or
            inputNumberTel.get() == contactEntry[i].split(" ")[4][:-1]):
                if j != 4:
                    ttk.Label(frm, text=contactEntry[i].split(" ")[j]).grid(column=j, row=i)
                else: ttk.Label(frm, text=contactEntry[i].split(" ")[j][:-1]).grid(column=j, row=i)
    data.close()