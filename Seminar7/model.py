import view

# функция добавления контакта в файл
def AddContact():
    if (view.inputSurname.get() != "" and view.inputName.get() != "" and
    view.inputBirthday.get() != "" and view.inputNumberTel.get() != "" and
    view.inputPatronymic.get() != "") :
        data = open("contacts.txt", "a", encoding="utf-8")
        data.write(f"{view.inputSurname.get()} {view.inputName.get()} {view.inputPatronymic.get()} ")
        data.write(f"{view.inputBirthday.get()} {view.inputNumberTel.get()}\n")
        data.close()
        view.GetPopupWindow("Запись добавлена в справочник!", "Телефонный справочник")
    else: view.GetPopupWindow("Заполнены не все поля!", "Ошибка")

# функция экспорта в html
def ExportHTML():
    data = open("contacts.txt", encoding="utf-8")
    contactEntry = data.readlines()
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    for i in range(len(contactEntry)):
        html += '    <p {}>{}</p>\n'\
            .format(style, contactEntry[i])
    html += '  </body>\n</html>'
    with open('index.html', 'w') as page:
        page.write(html)
    data.close()
    return html
