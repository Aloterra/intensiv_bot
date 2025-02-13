from telebot import types
from telebot.async_telebot import AsyncTeleBot

import keyboards
from config import *

bot = AsyncTeleBot(TOKEN)

log = logging.getLogger(__name__)


async def start(message: types.Message):
    log.info('user_id: %s', message.chat.id)
    await bot.send_message(message.chat.id, '''Добро пожаловать в GUNA ИЗОБИЛИЯ! 💫 

Вы на пороге невероятного путешествия, где каждый следующий шаг проявит для вас изобильную, наполненную счастьем и 
реализацией, экстраординарную жизнь!

В следующие 7 дней ежедневно, вы будете глобально расширять свое сознание, ресурсы и ресурсность, которые создадут 
новые энергонасыщенные горизонты, включающие возможность:

▫️Создать или улучшить все ваши отношения, наполнить безусловной любовью, проявить сексуальную близость и абсолютное 
доверие с партнером.

▫️Активировать женскую и сексуальную энергию, проявить новое изобильное, притягательное, притягивающее и 
всепроявляющее состояние Женщины 👑

▫️Наполнить ваше сознание и тело здоровьем, энергией и лёгкостью. 

▫️Обрести новый путь к своей реализации (духовной и материальной), внутренней и внешней финансовой свободе, 
где каждый день приносит безграничную радость бытия и истинное вдохновение.

И самое главное, ответить на вопрос «Кто Я», ответ на который и создает невероятные, желаемые, масштабные сценарии 
преображения в вашей жизни!

GUNA ИЗОБИЛИЯ — это мощное пространство трансформации, вдохновения и многомерного изобилия!   

Мы начинаем ❤️
С любовью, Анастасия Гунина.''', reply_markup=keyboards.start_keyboard())


async def register_start_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(start, commands=['start'])
