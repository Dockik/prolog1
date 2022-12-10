import asyncio
import logging

import aiogram.filters
from aiogram import Dispatcher, Bot
from aiogram import F
from core.handlers.basic import get_hello
from core.setting import settings
from core.utils.commands import set_command
from core.handlers.basic import get_start
from core.handlers.basic import send_msg


async def start_bot(bot: Bot):
    await set_command(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот прекратил работу')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s -[%(levelname)s] - %(name)s -'
                        '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
                        )

    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()

    dp.message.register(send_msg)
    dp.message.register(get_hello, F.text == 'Привет')
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, aiogram.filters.Command(commands=['start', 'run']))



    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())


