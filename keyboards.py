from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(KeyboardButton("Отримати PDF з цінами"))
main_kb.add(KeyboardButton("Залишити заявку"))