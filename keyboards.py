from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отримати прайс")],
        [KeyboardButton(text="Залишити контакти")],
    ],
    resize_keyboard=True
)