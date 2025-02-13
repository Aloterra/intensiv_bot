from telebot import types
from telebot.async_telebot import AsyncTeleBot

import base
import days
import keyboards
from config import *

bot = AsyncTeleBot(TOKEN)

log = logging.getLogger(__name__)


async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    log.info('User Id: %s', pre_checkout_query.from_user.id)
    await bot.answer_pre_checkout_query(int(pre_checkout_query.id), True)


async def process_pay(message: types.Message):
    await bot.delete_message(message.chat.id, message.id - 1)
    await bot.send_message(message.chat.id,
                           f'Отлично, Id вашей оплаты: {message.successful_payment.invoice_payload}',
                           reply_markup=keyboards.menu_keyboard())
    await base.new_user(message.chat.id, message.successful_payment.invoice_payload)
    await days.day_1(message.chat.id)


async def register_payment_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(process_pay, content_types=['successful_payment'])
    bot.register_pre_checkout_query_handler(process_pre_checkout_query, func=lambda pre_checkout_query: True)
