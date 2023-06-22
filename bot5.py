from aiogram import Bot, Dispatcher, executor, types
from property import *

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo'])
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Hello')
    await message.reply('Hello')

@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', url='https://www.youtube.com/watch?v=BvPaua-oC08&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=7'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)

@dp.callback_query_handler()
async def info(call):
    await call.message.answer(call.data)

@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Site'))
    await message.answer('Hello', reply_markup=markup)
    
executor.start_polling(dp)