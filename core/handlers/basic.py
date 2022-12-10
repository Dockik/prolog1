import asyncio
import time
from core.setting import settings
from aiogram import Bot
from aiogram.types import Message
from core.keyboard.reply import TblK
from time import sleep
import random


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'И тебе привет лисичка')


async def get_start(message: Message, bot: Bot):
    await message.answer(f'Я создан делать приятно,если ты понимаешь о чем я)',
                        reply_markup=TblK)


async def send_msg(message: Message, bot: Bot):
    while True:
        lovemessage = random.choice(list(open('text.txt', encoding='utf-8')))
        await bot.send_message(-1001637966273, lovemessage)
        print(lovemessage)
        await asyncio.sleep(3600)









