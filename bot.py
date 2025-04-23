import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
from handlers import start_handler, pdf_handler, request_contact, contact_name, contact_phone

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(commands=["start"])
async def cmd_start(message: Message):
    await start_handler(message)

@dp.message(lambda m: m.text == "Отримати PDF з цінами")
async def get_pdf(message: Message):
    await pdf_handler(message)

@dp.message(lambda m: m.text == "Залишити заявку")
async def start_request(message: Message, state):
    await request_contact(message, state)

@dp.message(lambda m: True, state="name")
async def get_name(message: Message, state):
    await contact_name(message, state)

@dp.message(lambda m: True, state="phone")
async def get_phone(message: Message, state):
    await contact_phone(message, state)

async def main():
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())