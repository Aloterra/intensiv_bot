from telebot import types
from telebot.async_telebot import AsyncTeleBot

import keyboards
from config import *

bot = AsyncTeleBot(TOKEN)

log = logging.getLogger(__name__)


async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    log.info('User Id: %s', pre_checkout_query.from_user.id)
    await bot.answer_pre_checkout_query(int(pre_checkout_query.id), True)


async def process_pay(message: types.Message):
    await bot.send_message(message.chat.id, 'Успешно', reply_markup=keyboards.menu_keyboard())


async def register_payment_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(process_pay, content_types=['successful_payment'])
    bot.register_pre_checkout_query_handler(process_pre_checkout_query, func=lambda pre_checkout_query: True)
