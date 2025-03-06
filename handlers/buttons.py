import json
from random import randint

from telebot import types
from telebot.async_telebot import AsyncTeleBot

import base
import keyboards
from config import *
from meditation import meditation_stack

bot = AsyncTeleBot(TOKEN)

log = logging.getLogger(__name__)


async def menu_edit(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(call.message.chat.id,
                                        call.message.id,
                                        reply_markup=keyboards.start_keyboard())


async def menu_delete(call: types.CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.id)
    await bot.send_photo(call.message.chat.id,
                         'AgACAgEAAxkBAAIERme0NbdwmwEFyJJzTQABZB9ZJuLdHAACa64xG8wgoEUzA7ZU057smAEAAwIAA3kAAzYE',
                         '''Меня зовут *Анастасия Гунина* – магистр психологии, автор канала _«Включи реальность»_, создатель *Женской программы*, групповых наставничеств и мастермайндов, а также автор уникального интенсива *GUNA ИЗОБИЛИЯ*.

*Моя миссия – помочь вам:*
▫️Открыть ваш *уникальный путь* к изобилию и процветанию во всех сферах жизни.
▫️Научиться строить *глубокие и гармоничные отношения* с собой и окружающими, обрести истинную любовную близость с партнером. 
▫️Овладеть искусством *создания и приумножения благосостояния*, которое трансформирует всю вашу реальность.

*С ЧЕГО НАЧАТЬ?*
Познакомьтесь с моими медитациями в этом боте – выберите те, которые наиболее откликаются вашему запросу и станут первым шагом к красивой трансформации✨

*Если вы готовы к проявлению бОльшего в вашей жизни - создать изобильное бытие на экстраординарном уровне, я приглашаю вас войти в GUNA ИЗОБИЛИЯ 🎇*''',
                         reply_markup=keyboards.start_keyboard(),
                         parse_mode='markdown')


async def questions(call: types.CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.id)
    await bot.send_message(call.message.chat.id,
                           'Выберите что вас интересует...',
                           reply_markup=keyboards.questions_keyboard())


async def confirmation(call: types.CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    await bot.send_message(call.message.chat.id,
                           '''*Добро пожаловать в GUNA ИЗОБИЛИЯ!* 💫 
  
  Вы на пороге невероятного путешествия, где каждый следующий шаг проявит для вас изобильную, наполненную счастьем и реализацией, экстраординарную жизнь! 
  
  *В следующие 7 дней ежедневно, вы будете глобально расширять свое сознание, ресурсы и ресурсность, которые создадут новые энергонасыщенные горизонты, включающие возможность:*
  
  ▫️*Создать или улучшить все ваши отношения, наполнить безусловной любовью, проявить сексуальную близость и абсолютное доверие с партнером.*
  
  ▫️*Активировать женскую и сексуальную энергию, проявить новое изобильное, притягательное, притягивающее и всепроявляющее состояние Женщины* 👑 
  
  ▫️*Наполнить ваше сознание и тело здоровьем, энергией и лёгкостью.* 
  
  ▫️*Обрести новый путь к своей реализации (духовной и материальной), внутренней и внешней финансовой свободе, где каждый день приносит безграничную радость бытия и истинное вдохновение.* 
  
  *И самое главное, ответить на вопрос «Кто Я», ответ на который и создает невероятные, желаемые, масштабные сценарии преображения в вашей жизни!* 
  
  *GUNA ИЗОБИЛИЯ — это мощное пространство трансформации, вдохновения и многомерного изобилия!*   
  
  *Мы начинаем* ❤️
  *С любовью, Анастасия Гунина.*''',
                           reply_markup=keyboards.confirmation_keyboard(),
                           parse_mode='markdown')


async def payment_process(call: types.CallbackQuery):
    order_ids = await base.orders()
    user_order = randint(10_000_000, 99_000_000)
    while user_order in order_ids:
        user_order = randint(10_000_000, 99_000_000)
    await bot.delete_message(call.message.chat.id, call.message.id)
    await bot.send_invoice(chat_id=call.message.chat.id,
                           title='Интенсив GUNA ИЗОБИЛИЯ',
                           description='Готова войти в пространство глобальных трансформаций и создания новых жизненных сценариев',
                           invoice_payload=f'{user_order}',
                           provider_token=PAYMENT_TOKEN,
                           currency='RUB',
                           prices=[types.LabeledPrice(label='Цена', amount=100_00)],
                           max_tip_amount=50_00,
                           suggested_tip_amounts=[10_00, 20_00, 30_00, 40_00],
                           need_name=True,
                           need_email=True,
                           need_phone_number=True,
                           send_email_to_provider=True,
                           send_phone_number_to_provider=True,
                           provider_data=json.dumps(provider_data),
                           reply_markup=keyboards.payment_keyboard())


async def choose_meditation(call: types.CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    await bot.send_message(call.message.chat.id,
                           'Выберите медитацию: ',
                           reply_markup=keyboards.meditation_keyboard())


async def meditation(call: types.CallbackQuery):
    meditations = await meditation_stack()
    await meditations[int(call.data.split('_')[0])](call.message)


async def register_buttons_handlers(bot: AsyncTeleBot):
    bot.register_callback_query_handler(confirmation, func=lambda call: call.data == 'confirmation')
    bot.register_callback_query_handler(payment_process, func=lambda call: call.data == 'approve')
    bot.register_callback_query_handler(menu_edit, func=lambda call: call.data == 'menu_edit')
    bot.register_callback_query_handler(questions, func=lambda call: call.data == 'questions')
    bot.register_callback_query_handler(menu_delete, func=lambda call: call.data == 'menu_delete')
    bot.register_callback_query_handler(choose_meditation, func=lambda call: call.data == 'meditation')
    bot.register_callback_query_handler(meditation, func=lambda call: str(call.data).endswith('meditation-media'))
