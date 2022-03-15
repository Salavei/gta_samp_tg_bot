from aiogram.dispatcher.filters.builtin import CommandStart
from utils.func_async import *
from fsm.fsm import *


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет!Все комманды /help')


async def error(message: types.Message):
    await message.delete()

async def help(message: types.Message):
    command_all = """
    move - кнопки управления
    /enter - enter
    /alt - alt
    /n - n
    /i - i
    /op - открыть сундук с рулетками(должен быть в первом слоте)
    /esc - esc
    /cam - менять обзов камеры
    /cam1 - менять обзов камеры
    /q - выход
    /li - информация о том, подключились ли к серверу
    /rec - реконнект
    /f6 - написать в чат
    /f8 - сделать скрин
    """
    await message.answer(command_all)

@dp.message_handler(content_types=['text'])
async def command_start_text(message: types.Message):
    data = {
        'move': move,
        '/f8': send_screen,
        '/f6': start_fsm,
        '/rec': reconnect,
        '/li': login_info,
        '/q': quitgame,
        'w': w,
        'a': a,
        's': s,
        'd': d,
        '/enter': enter,
        '/alt': alt,
        '/n': n,
        '/i': i,
        '/op': open_box,
        '/esc': esc,
        'shift': shift,
        'space': space,
        '/cam': cam,
        '/cam1': cam1,
        '/help':help,
    }
    await data.get(message.text, error)(message)
