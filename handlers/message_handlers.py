from telebot import types
from telebot.async_telebot import AsyncTeleBot

import keyboards
from config import *

bot = AsyncTeleBot(TOKEN)

log = logging.getLogger(__name__)


async def start(message: types.Message):
    log.info('user_id: %s', message.chat.id)
    await bot.send_photo(message.chat.id,
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


async def question_one(message):
    await bot.delete_message(message.chat.id, message.id - 1)
    await bot.delete_message(message.chat.id, message.id)
    await bot.send_message(message.chat.id,
                           '''Интенсив - это полноценная глубинная программа, которая позволяет создать кардинально новый уровень восприятия в сфере отношений, финансов, реализации и здоровья, демонстрирующая взаимодействие с авторским методом Анастасии Гуниной и открывающая ключи, как работает Вселенная, даруя истинную свободу, внутреннюю опору, самоценность, любовь к себе и новые изобильные жизненные сценарии!''',
                           reply_markup=keyboards.answer_keyboard())


async def question_two(message):
    await bot.delete_message(message.chat.id, message.id - 1)
    await bot.delete_message(message.chat.id, message.id)
    await bot.send_message(message.chat.id,
                           '''GUNA ИЗОБИЛИЯ - это концентрация самых сильных лекций, энергетических процессов,собранная из всех программ Анастасии Гуниной (Женская программа, наставничества, мастермайнды). Это бесценные знания, дающие ответ на главный вопрос "Кто я",  ответив на который, жизнь каждого человека преображается и становится экстраординарной! Интенсив полностью в записи. Интенсив не подразумевает обратной связи и нацелен на самостоятельное изучение. Вы смотрите лекции и выполняете медитации в любое удобное для вас время.''',
                           reply_markup=keyboards.answer_keyboard())


async def question_three(message):
    await bot.delete_message(message.chat.id, message.id - 1)
    await bot.delete_message(message.chat.id, message.id)
    await bot.send_message(message.chat.id,
                           '''Стоимость интенсива GUNA ИЗОБИЛИЯ - 4999 рублей. Оплата доступна только для российсикй карт. Если вы находитесь заграницей и желаете приобрести доступ, напишите Анастасии Гуниной лично.''',
                           reply_markup=keyboards.answer_keyboard())


async def question_four(message):
    await bot.delete_message(message.chat.id, message.id - 1)
    await bot.delete_message(message.chat.id, message.id)
    await bot.send_message(message.chat.id,
                           '''Интенсив проходит в этом боте, длится 7 дней, ежедневно присылая для вас лекции и энергетические процессы-медитации. Доступ к материалам 3 месяца, со дня приобретения.''',
                           reply_markup=keyboards.answer_keyboard())


async def register_start_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(start, commands=['start'])
    bot.register_message_handler(question_one, func=lambda message: str(message.text).startswith('Чем отличаются'))
    bot.register_message_handler(question_two, func=lambda message: str(message.text).startswith('Какой формат'))
    bot.register_message_handler(question_three, func=lambda message: str(message.text).startswith('Какая стоимость'))
    bot.register_message_handler(question_four, func=lambda message: str(message.text).startswith('Сколько длится'))
