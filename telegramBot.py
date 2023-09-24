from token_name import TOKEN_NAME
from aiogram import Bot, types
from aiogram import Dispatcher, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, KeyboardButton
from bs4 import BeautifulSoup
from keyboards import kb, kb2, kb3

# import bot_backend

bot = Bot(token=TOKEN_NAME)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Здравствуте, уважаемый пользователь. Вы хотите отправить или получить конспект?',
                           reply_markup=kb)


@dp.message_handler(Text(equals="Отправить"))
async def start_send(message: types.Message):
    await message.answer(
        text='Какой конспект вы хотите отправить?',
        reply_markup=kb2)


@dp.message_handler(Text(equals="Получить"))
async def start_get_lesson(message: types.Message):
    await message.answer(
        text='Какой конспект вы хотите получить?',
        reply_markup=kb2)


@dp.message_handler(Text(equals="Математический Анализ"))
async def start_get_LP(message: types.Message):
    await message.answer(
        text='Лекция или практика?',
        reply_markup=kb3)


# @dp.message_handler(Text(equals="Лекция"))
# async def start_get(message: types.Message):
#    await message.answer(
#        text='Лекция или практика?',
#        reply_markup=kb3)


if __name__ == '__main__':
    executor.start_polling(dp)
