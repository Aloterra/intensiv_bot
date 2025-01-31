import logging

from telebot import types
from telebot.async_telebot import AsyncTeleBot

import keyboards
from config import *

bot = AsyncTeleBot(TOKEN)

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


async def start(message: types.Message):
    log.info('user_id: %s', message.chat.id)
    await bot.send_message(message.chat.id,
                           'Приветственное сообщение',
                           reply_markup=keyboards.start_keyboard())


async def register_start_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(start, commands=['start'])
