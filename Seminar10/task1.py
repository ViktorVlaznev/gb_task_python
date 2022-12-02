# Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot
import requests
import time
from datetime import date
from numexpr import evaluate
from random import randint
import os.path
from telebot import types

count = 0
hidden_number = 0

bot = telebot.TeleBot("", parse_mode=None)

markup = types.ReplyKeyboardMarkup()
itembtn1 = types.KeyboardButton('привет')
itembtn2 = types.KeyboardButton('регистрация')
itembtn3 = types.KeyboardButton('погода')
itembtn4 = types.KeyboardButton('котик')
itembtn5 = types.KeyboardButton('посчитать')
itembtn6 = types.KeyboardButton('играть')
itembtn7 = types.KeyboardButton('тех. поддержка')

markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)

@bot.message_handler(commands=['start', 'help', 'hello'])

def send_welcome(message):
	bot.reply_to(message, "Привет, " + message.from_user.first_name, reply_markup=markup)

@bot.message_handler(commands=['notice'])
def notice(message):
	data = open('users.txt', "r", encoding='utf-8')
	user_id = data.readlines()
	for id in user_id:
		try:
			bot.send_message(id, "оповещение")
		except telebot.apihelper.ApiTelegramException:
			print(f"Оповещение пользователю {id} не отправлено")
	data.close()

@bot.message_handler(content_types=["text"])
def text_message(message):
    global count
    global hidden_number
    if "тех. поддержка" in message.text:
        msg = bot.reply_to(message, 'Введите ваш вопрос: ')
        bot.register_next_step_handler(message, RecordFileSupport)
    elif message.text == "играть":
        count = 0
        hidden_number = randint(1,1000)
        msg = bot.reply_to(message, 'Угадай число от 1 до 1000. Введи число:')
        bot.register_next_step_handler(message, process_game)
    elif message.text == "посчитать":
        msg = bot.reply_to(message, 'Введите числовое выражение: ')
        bot.register_next_step_handler(message, process_evalution)
    elif "привет" in message.text:
        bot.reply_to(message, "Привет, " + message.from_user.first_name)
    elif message.text == "погода":
        r = requests.get('https://wttr.in/?0T')
        bot.reply_to(message, r.text)
    elif message.text == "котик":
        r = f'https://cataas.com/cat?t=${time.time()}'
        bot.send_photo(message.chat.id, r)
    elif message.text == "файл":
        data = open('user_message.txt')
        bot.send_document(message.chat.id, data)
        data.close()
    elif message.text == "регистрация":
        user_id = str(message.from_user.id)
        if os.path.exists('users.txt'):
            FileRegister('users.txt', "r+", user_id, message)
        else:
            FileRegister('users.txt', "a+", user_id, message)
    else:
        bot.send_message(message.from_user.id, "Не понимаю Вас. Введите /start или /help")
    data = open('user_message.txt', 'a+', encoding='utf-8')
    data.writelines(str(date.today()) + " " + str(message.from_user.id) + " " + message.text + "\n")
    data.close()

# функция для орпеделения числового выражения
def process_evalution(message):
	bot.reply_to(message, str(evaluate(message.text)))

# функция поиска числа
def process_game(message):
	global count
	global hidden_number
	count += 1
	if int(message.text) > hidden_number:
		bot.reply_to(message, "меньше")
		bot.register_next_step_handler(message, process_game)
	elif int(message.text) < hidden_number:
		bot.reply_to(message, "больше")
		bot.register_next_step_handler(message, process_game)
	else: bot.reply_to(message, f"Вы угадали за {count} ходов!")

# функция регистрации пользователя
def FileRegister(link, mode, value, message):
	data = open(link, mode, encoding='utf-8')
	lines = data.read()
	if value not in lines:
		data.writelines(str(message.from_user.id) + "\n")
		bot.send_message(message.from_user.id, "Успешно.")
	else: bot.send_message(message.from_user.id, "Данный аккаунт уже зарегистрирован.")
	data.close()

# функция записи в файл информации для тех поддержки 
def RecordFileSupport(message):
    data = open('user_support.txt', 'a+', encoding='utf-8')
    data.writelines(str(date.today()) + " " + str(message.from_user.id) + " " + message.text + "\n")
    data.close()
    bot.reply_to(message, f"Спасибо за Ваше обращение! Вам ответят в ближайшее время.")

bot.infinity_polling()