from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from property import *

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://h20ch3po2.github.io/Telegram_Bots_in_Python_from_scratch_itproger/')))
    await message.answer('Привет, мой друг!', reply_markup=markup)


executor.start_polling(dp)