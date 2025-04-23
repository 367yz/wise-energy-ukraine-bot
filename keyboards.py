from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отримати PDF з цінами")],
        [KeyboardButton(text="Залишити заявку")]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)