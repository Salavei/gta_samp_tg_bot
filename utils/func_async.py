from main import *
from aiogram import types
import keyboard
import os
import time
import pyautogui
from keyboards.default.markup import keyboard_move


async def screenshots_(message: types.Message):
    pyautogui.press('f8')
    time.sleep(1)
    dirname = '/Users/andrewsalavei/Documents/GTA San Andreas User Files/SAMP/arizona/screens/'
    dir_screen = os.listdir(dirname)
    files = os.listdir(dirname + sorted(dir_screen, reverse=True)[0])
    await bot.send_photo(chat_id=message.chat.id,
                         photo=open(f"{dirname}/{sorted(dir_screen, reverse=True)[0]}/{sorted(files, reverse=True)[0]}",
                                    'rb'))


async def move(message: types.Message):
    await message.answer('Управление персонажем', reply_markup=keyboard_move)


async def send_screen(message: types.Message):
    await screenshots_(message)


async def reconnect(message: types.Message):
    keyboard.send('f6')
    pyautogui.write('/rec')
    keyboard.send('enter')
    ok = True
    dd = open('/Users/andrewsalavei/Documents/GTA San Andreas User Files/SAMP/chatlog.txt', 'w', encoding='cp1251')
    dd.close()
    await message.answer(text='Сделали реконнек')
    while ok:
        word = 'сервере есть инвентарь, используйте клавишу'
        with open('/Users/andrewsalavei/Documents/GTA San Andreas User Files/SAMP/chatlog.txt', 'r',
                  encoding='cp1251') as f:
            if word in f.read():
                ok = False
                keyboard.send('f8')
                time.sleep(1)
                dirname = '/Users/andrewsalavei/Documents/GTA San Andreas User Files/SAMP/arizona/screens/'
                dir_screen = os.listdir(dirname)
                files = os.listdir(dirname + sorted(dir_screen, reverse=True)[0])
                time.sleep(5)
                keyboard.send('enter')
                await bot.send_photo(chat_id=message.chat.id,
                                     photo=open(
                                         f"{dirname}/{sorted(dir_screen, reverse=True)[0]}/{sorted(files, reverse=True)[0]}",
                                         'rb'))



async def login_info(message: types.Message):
    word = 'Успешный вход. Приятной игры на сервере :)'
    with open('/Users/andrewsalavei/Documents/GTA San Andreas User Files/SAMP/chatlog.txt', 'r',
              encoding='cp1251') as f:
        if word in f.read():
            await message.answer(text='Подлючились к серверу')


async def open_box(message: types.Message):
    pyautogui.press('i')
    time.sleep(1)
    pyautogui.moveTo(860, 226)
    pyautogui.click()
    pyautogui.moveTo(860, 235)
    pyautogui.click()
    pyautogui.press('esc')
    pyautogui.press('f8')
    await screenshots_(message)


async def quitgame(message: types.Message):
    pyautogui.press('f6')
    pyautogui.write('/q')
    pyautogui.press('enter')
    await message.answer(text='Выход с сервера....')


async def w(message: types.Message):
    keyboard.press("ц")
    time.sleep(1)
    keyboard.release("ц")
    time.sleep(1)
    await screenshots_(message)
    await message.answer(text='w')


async def enter(message: types.Message):
    pyautogui.press("enter")
    time.sleep(1)
    await screenshots_(message)
    await message.answer(text='enter')


async def s(message: types.Message):
    pyautogui.moveTo(0, 360)
    keyboard.press("ц")
    time.sleep(1)
    keyboard.release("ц")
    await screenshots_(message)
    await message.answer(text='s')


async def a(message: types.Message):
    pyautogui.moveTo(260, 352)
    keyboard.press("ц")
    time.sleep(1)
    keyboard.release("ц")
    await screenshots_(message)
    await message.answer(text='a')


async def d(message: types.Message):
    pyautogui.moveTo(850, 352)
    keyboard.press("ц")
    time.sleep(1)
    keyboard.release("ц")
    await screenshots_(message)
    await message.answer(text='d')


async def cam(message: types.Message):
    await screenshots_(message)
    pyautogui.moveTo(572, 450)


async def cam1(message: types.Message):
    await screenshots_(message)
    pyautogui.moveTo(576, 300)


async def alt(message: types.Message):
    pyautogui.press("command")
    await screenshots_(message)
    await message.answer(text='command')


async def n(message: types.Message):
    pyautogui.press("n")
    await screenshots_(message)
    await message.answer(text='n')


async def i(message: types.Message):
    pyautogui.press("i")
    await screenshots_(message)
    await message.answer(text='i')


async def esc(message: types.Message):
    pyautogui.press("esc")
    await screenshots_(message)
    await message.answer(text='esc')


async def shift(message: types.Message):
    pyautogui.press("shift")
    await screenshots_(message)
    await message.answer(text='shift')


async def space(message: types.Message):
    pyautogui.press("space")
    await screenshots_(message)
    await message.answer(text='space')
