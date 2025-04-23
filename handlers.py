from aiogram import types
from config import PDF_PATH, CSV_PATH
from keyboards import main_kb
import csv
import os

async def start_handler(message: types.Message):
    await message.answer("Вітаємо у Wise Energy Ukraine!\nОберіть опцію нижче:", reply_markup=main_kb)

async def pdf_handler(message: types.Message):
    if os.path.exists(PDF_PATH):
        with open(PDF_PATH, "rb") as doc:
            await message.answer_document(doc, caption="Ось актуальний прайс-лист.")
    else:
        await message.answer("Вибачте, файл тимчасово недоступний.")

async def request_contact(message: types.Message, state):
    await message.answer("Будь ласка, введіть ваше ім'я:")
    await state.set_state("name")

async def contact_name(message: types.Message, state):
    await state.update_data(name=message.text)
    await message.answer("Ваш номер телефону:")
    await state.set_state("phone")

async def contact_phone(message: types.Message, state):
    data = await state.get_data()
    name = data.get("name")
    phone = message.text

    with open(CSV_PATH, "a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone])

    await message.answer("Дякуємо! Ми зв’яжемось з вами найближчим часом.")
    await state.clear()