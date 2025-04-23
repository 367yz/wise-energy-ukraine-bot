import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from handlers import start_handler, pdf_handler, request_contact, contact_name, contact_phone
from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

dp.message.register(start_handler, Command("start"))
dp.message.register(pdf_handler, Command("price"))
dp.message.register(request_contact, Command("contact"))

dp.message.register(contact_name, lambda msg, state: state.state == "name")
dp.message.register(contact_phone, lambda msg, state: state.state == "phone")


async def main():
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())