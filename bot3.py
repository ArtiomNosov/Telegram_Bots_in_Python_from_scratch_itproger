import telebot
import requests
import json
from property import *

bot = telebot.TeleBot(token)
API = '0e6fb7a90ad12e07bac20a4660093924'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')

@bot.message_handler(commands=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    if len(city.split()) > 1:
        city = city.split()[1]
    bot.reply_to(message, city)
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')
        image = 'sun.png' if temp > 5.0 else 'photo0.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Неверно указан город: {city}')

bot.polling(none_stop=True)