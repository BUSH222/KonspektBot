from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='Отправить')
b2 = KeyboardButton(text='Получить')
kb.add(b1, b2)


kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton(text='Математический Анализ')
bp2 = KeyboardButton(text='Линейная Алгебра')
bp3 = KeyboardButton(text='Вычислительные машины, сети и системы')
bp4 = KeyboardButton(text='История России')
bp5 = KeyboardButton(text='Программирование и алгоритмизация')
bp6 = KeyboardButton(text='Основы Российской Государственности')

kb2.add(bp1, bp2).add(bp3, bp4).add(bp5, bp6)

kb3 = ReplyKeyboardMarkup(resize_keyboard=True)
blp1 = KeyboardButton(text='Лекция')
blp2 = KeyboardButton(text='Практика')
kb3.add(blp1, blp2)
