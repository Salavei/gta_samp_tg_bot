from aiogram.types import KeyboardButton
from aiogram import types

btn_w = KeyboardButton("w")
btn_s = KeyboardButton("s")
btn_a = KeyboardButton("a")
btn_d = KeyboardButton("d")
btn_space = KeyboardButton("space")
btn_shift = KeyboardButton("shift")

keyboard_move = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_move.add(btn_space, btn_w, btn_shift, btn_a, btn_s, btn_d)
