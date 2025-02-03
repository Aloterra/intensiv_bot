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


async def menu_edit(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(call.message.chat.id,
                                        call.message.id,
                                        reply_markup=keyboards.start_keyboard())


async def menu_delete(call: types.CallbackQuery):
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


async def confirmation(call: types.CallbackQuery):
    await bot.edit_message_text('Описание Интенсива', call.message.chat.id, call.message.id)
    await bot.edit_message_reply_markup(call.message.chat.id,
                                        call.message.id,
                                        reply_markup=keyboards.confirmation_keyboard())


async def payment_process(call: types.CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.id)
    await bot.send_invoice(chat_id=call.message.chat.id,
                           title='Title',
                           description='description',
                           invoice_payload='intensive',
                           provider_token=TEST_PAYMENT_TOKEN,
                           currency='RUB',
                           prices=[types.LabeledPrice(label='Цена', amount=5000_00),
                                   types.LabeledPrice(label='Скидка', amount=-4000_00)],
                           max_tip_amount=50_00,
                           suggested_tip_amounts=[10_00, 20_00, 30_00, 40_00],
                           reply_markup=keyboards.payment_keyboard())


async def register_buttons_handlers(bot: AsyncTeleBot):
    bot.register_callback_query_handler(confirmation, func=lambda call: call.data == 'confirmation')
    bot.register_callback_query_handler(payment_process, func=lambda call: call.data == 'approve')
    bot.register_callback_query_handler(contacts, func=lambda call: call.data == 'contact')
    bot.register_callback_query_handler(menu_edit, func=lambda call: call.data == 'menu_edit')
    bot.register_callback_query_handler(questions, func=lambda call: call.data == 'questions')
    bot.register_callback_query_handler(menu_delete, func=lambda call: call.data == 'menu_delete')
    bot.register_message_handler(answers, func=lambda message: message.text[:6] == 'Вопрос')
