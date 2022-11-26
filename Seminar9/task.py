import telebot
import requests
import time
from datetime import date
from numexpr import evaluate
from random import randint

count = 0
hidden_number = 0

bot = telebot.TeleBot("", parse_mode=None)

@bot.message_handler(commands=['start', 'help', 'hello'])

def send_welcome(message):
	bot.reply_to(message, "Приступим!")
	
@bot.message_handler(content_types=["text"])

def hello_user(message):
	global count
	global hidden_number
	if "привет" in message.text:
		bot.reply_to(message, "Привет, " + message.from_user.first_name)
	elif message.text == "играть":
		count = 0
		hidden_number = randint(1,1000)
		msg = bot.reply_to(message, 'Угадай число от 1 до 1000. Введи число:')
		bot.register_next_step_handler(message, process_game)
	elif message.text == "посчитать":
		msg = bot.reply_to(message, 'Введите числовое выражение: ')
		bot.register_next_step_handler(message, process_evalution)
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

bot.infinity_polling()