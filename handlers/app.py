from aiogram.dispatcher.filters.builtin import CommandStart
from utils.func_async import *
from fsm.fsm import *


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет!')


async def error(message: types.Message):
    await message.delete()


@dp.message_handler(content_types=['text'])
async def command_start_text(message: types.Message):
    data = {
        '/f8': send_screen,
        '/f6': start_fsm,
        '/rec': reconnect,
        '/li': login_info,
        '/q': quitgame,
        'w': w,
        'a': a,
        's': s,
        'd': d,
        'enter': enter,
        'alt': alt,
        'n': n,
        'i': i,
        'op': open_box,
        'esc': esc,
        'shift': shift,
        'space': space,
    }
    await data.get(message.text, error)(message)
