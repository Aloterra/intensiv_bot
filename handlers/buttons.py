import logging

from telebot import types
from telebot.async_telebot import AsyncTeleBot

import keyboards
from config import *

bot = AsyncTeleBot(TOKEN)

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


async def contacts(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(call.message.chat.id,
                                        call.message.id,
                                        reply_markup=keyboards.contact_keyboard())


async def menu(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(call.message.chat.id,
                                        call.message.id,
                                        reply_markup=keyboards.start_keyboard())


async def menu_questions(call: types.CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.id)
    await bot.send_message(call.message.chat.id, 'Приветственное сообщение', reply_markup=keyboards.start_keyboard())


async def questions(call: types.CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.id)
    await bot.send_message(call.message.chat.id,
                           'Выберите что вас интересует...',
                           reply_markup=keyboards.questions_keyboard())


async def answers(message: types.Message):
    await bot.delete_message(message.chat.id, message.id - 1)
    await bot.delete_message(message.chat.id, message.id)
    await bot.send_message(message.chat.id, 'Ответ', reply_markup=keyboards.answer_keyboard())


async def register_buttons_handlers(bot: AsyncTeleBot):
    bot.register_callback_query_handler(contacts, func=lambda call: call.data == 'contact')
    bot.register_callback_query_handler(menu, func=lambda call: call.data == 'menu')
    bot.register_callback_query_handler(questions, func=lambda call: call.data == 'questions')
    bot.register_callback_query_handler(menu_questions, func=lambda call: call.data == 'menu_questions')
    bot.register_message_handler(answers, func=lambda message: message.text[:6] == 'Вопрос')
