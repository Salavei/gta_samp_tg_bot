from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from main import *
import pyautogui
import pyperclip, time


class FSMchat(StatesGroup):
    message_send = State()


async def start_fsm(message: types.Message):
    await FSMchat.message_send.set()
    await message.answer('Напишите ваше сообщение:')


@dp.message_handler(state=FSMchat.message_send)
async def write_brand(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['message_send'] = message.text

    def type(text: str):
        pyperclip.copy(text)
        pyautogui.press('f6')
        time.sleep(1)
        pyperclip.paste()
        time.sleep(1)
        pyautogui.press('enter')

    type(data['message_send'])
    await message.answer(f"Ваше сообщение отправлено!! {data['message_send']}")
    await state.finish()
