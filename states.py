from aiogram.fsm.state import State, StatesGroup

class ContactForm(StatesGroup):
    name = State()
    phone = State()