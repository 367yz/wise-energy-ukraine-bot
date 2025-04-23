import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN
from handlers import start_handler, pdf_handler, request_contact, contact_name, contact_phone

dp = Dispatcher(storage=MemoryStorage())

dp.message.register(start_handler, commands=["start"])
dp.message.register(pdf_handler, lambda msg: msg.text == "Отримати прайс")
dp.message.register(request_contact, lambda msg: msg.text == "Залишити контакти")
dp.message.register(contact_name, state="ContactForm:name")
dp.message.register(contact_phone, state="ContactForm:phone")

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())