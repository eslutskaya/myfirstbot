import Telebot #подключаем необходимые бибилиотеки
import requests

token='345421719:AAE5qQFSbXnLM7ACqkQshFrQzpVz0MlE6NI'
TelegramBot = telebot.Bot(token) #Токен получен блпгодаря BotFather
URL = 'https://api.telegram.org/bot' # URL на который отправляется запрос

try: # обрабатываем исключения
request = requests.post(URL TOKEN '/getUpdates', data=data) # собственно сам запрос
except:
print('Error getting updates')
return False

if not request.status_code == 200: return False # проверяем пришедший статус ответа
if not request.json()['ok']: return False

@bot.message_handler(commands=['start'])
def handler_start(message):
User_markup=telebot.types.ReplyKeyboardMarkup(True, False)
User_markup.row("Привет")
User_markup.row("/start")

@bot.message_handler(content_types=['text'])
def handler_text(message):
if message.text=="Привет":
bot.send_message(massage.from_user.id, "Привет-привет!")
if message.text=="Мне скучно":
bot.send_message(massage.from_user.id, "Посмотри Клинику")
if message.text=="Как дела?":
bot.send_message(massage.from_user.id, "Отлично, а у тебя")
if message.text=="Хорошо":
bot.send_message(massage.from_user.id, "Я рад за тебя)")
if message.text=="Плохо":
bot.send_message(massage.from_user.id, "Не грусти")

@bot.message_handler(content_types=['audio'])
def handler_text(message):
bot.send_message(massage.from_user.id, "Хороша песня, а я классику люблю")

@bot.message_handler(content_types=['voice'])
def handler_text(message):
bot.send_message(massage.from_user.id, "Я не понимаю:(")
