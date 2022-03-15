from aiogram import Bot, Dispatcher, executor
import logging
import environ
from aiogram.contrib.fsm_storage.memory import MemoryStorage

env = environ.Env()
environ.Env.read_env()
TOKEN = env('TOKEN')
logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

if __name__ == '__main__':
    print('Start bot...')
    from handlers.app import dp
    executor.start_polling(dp, skip_updates=True)