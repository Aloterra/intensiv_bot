from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from config import *
from keyboards import menu_keyboard

bot = AsyncTeleBot(TOKEN)


async def meditation_1(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_audio(message.chat.id,
                         r'CQACAgIAAxkBAAICPWevdKn8-V6XQKGoWoptnxdnkE4lAAJBFwACb_UBSMXrOAx_4zbXNgQ',
                         '''*ПРАКТИКА ДЫХАНИЕ ЖИЗНИ 🧘🏻‍♀️ 

▫️ Помогает убрать тревогу, беспокойные мысли, снять напряжение и суету

▫️Возвращает к себе, в свое тело, увеличивает чувствительность

Практику-медитацию можно выполнять в те моменты, когда необходимо убрать чувство тревоги и негативные эмоции. 

Данную практику можно повторять
любое количество раз.

Расслабленный мозг
– это приоритет в нашей жизни . Только в расслабленном состоянии мы можем получить доступ к женской энергии.*''',
                         parse_mode='markdown',
                         reply_markup=menu_keyboard())


async def meditation_2(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_audio(message.chat.id, 'CQACAgEAAxkBAAICQGevdczQTCHuef7E6WSVgISvy4UUAALjBQACjKGARbP-0LTwhr7VNgQ',
                         '''🔥🔥*МЕДИТАЦИЯ* 🔥🔥

*ЭНЕРГЕТИЧЕСКАЯ СОНАСТРОЙКА НА УЛУЧШЕНИЕ КАЧЕСТВА ВАШЕЙ ЭНЕРГЕТИКИ И МОЩНОЕ УВЕЛИЧЕНИЕ ЭНЕРГИИ*

⬇️⬇️⬇️''', parse_mode='markdown', reply_markup=menu_keyboard())


async def meditation_3(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_video(message.chat.id, 'BAACAgIAAxkBAAICQmevdvih4DtYeXeRYGng2Whof8ISAALtEgACW4LISL4q7Ned8mwcNgQ',
                         caption='''*МЕДИТАЦИЯ ЛЮБВИ*🤍

Избавление от страха, тревоги и напряжения

*СОЗДАНИЕ ЛЮБВИ ВНУТРИ И ВОВНЕ*''', parse_mode='markdown', reply_markup=menu_keyboard())


async def meditation_4(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_audio(message.chat.id, 'CQACAgEAAxkBAAICRGeveA4dVpjQURRDQCscKUVljy94AALkBQACjKGARVo8hENGn9kuNgQ',
                         caption='''*МЕДИТАЦИЯ РАССЛАБЛЕНИЯ, ОТПУСКАНИЯ БЛОКОВ И ЧУЖОЙ ЭНЕРГИИ В СВОЁМ ПРОСТРАНСТВЕ*
⬇️⬇️''', parse_mode='markdown', reply_markup=menu_keyboard())


async def meditation_5(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_audio(message.chat.id, 'CQACAgIAAxkBAAICRmeveFg2kwzmsVwO_aN2aqNDRF80AAKEFgACZ7YxS5apvgFMAAG-HDYE',
                         caption='''*МЕДИТАЦИЯ СОЗДАНИЕ ИСТИННОГО ДОВЕРИЯ И АКТИВАЦИЯ СВОЕЙ БОЖЕСТВЕННОЙ СУТИ*


⬇️⬇️⬇️''', parse_mode='markdown', reply_markup=menu_keyboard())


async def meditation_6(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_video(message.chat.id, 'BAACAgIAAxkBAAICSGevfPpzIF1_Cvz7t8NTLAw1r6z8AAKkEwACB1LQSA3wUmXpBsyQNgQ',
                         caption='''Друзья, отправляю вам новую медитацию «Создание внутренней свободы»

🧘🏻‍♀️ *МЕДИТАЦИЯ ПЕРЕД СНОМ* даст максимальное расслабление и поможет создать наилучшие варианты событий в новом дне, в вашей жизни💙
⬇️⬇️⬇️''', parse_mode='markdown', reply_markup=menu_keyboard())


async def meditation_7(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_video(message.chat.id, 'BAACAgEAAxkBAAICS2evfvkZIPsSY-T0N30I10-8zFNsAALnBQACjKGARb1syT7LrBQNNgQ',
                         caption='''Отправляю вам медитацию 

*СОНАСТРОЙКА С ЭНЕРГИЯМИ ДНЯ*

⬇️⬇️⬇️''', parse_mode='markdown', reply_markup=menu_keyboard())


async def meditation_8(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_video(message.chat.id, 'BAACAgIAAxkBAAICW2ev9izCu6_8fYfGILznaLt6Q6n2AAKmFQAC9k5xSQ93-vepNcgpNgQ',
                         caption='''Медитация

*ЭНЕРГЕТИЧЕСКИЕ ВИБРАЦИИ*''', parse_mode='markdown', reply_markup=menu_keyboard())


async def meditation_9(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_audio(message.chat.id, 'CQACAgIAAxkBAAICZ2ev95QGBmbJFas1AyYHg_DzQyBbAALYFwACFbsBSEq_TMR7aewZNgQ',
                         caption='''1️⃣ *МЕДИТАЦИЯ - ЭНЕРГЕТИЧЕСКАЯ ПРАКТИКА: РАБОТА С ВНУТРЕННИМИ ДИАЛОГАМИ*

▫️Эта практика-медитация поможет вам очистить внутреннее пространство от негативных энергий, мыслей и мыслеформ, навязчивых внутренних диалогов, тревоги. 

▫️Практика создает новые нейронные связи и расширяет возможность совершать новые выборы в своей жизни, получая новые результаты❤️‍🔥

▫️До выполнения практики выпишите 1-3 негативных убеждения, навязчивых мысли, которые вызывают у вас одинаковые неприятные, неэффективные эмоции и состояния. Далее, приступайте к выполнению медитации.

⬇️⬇️⬇️''', parse_mode='markdown', reply_markup=menu_keyboard())


async def meditation_10(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_audio(message.chat.id, 'CQACAgEAAxkBAAICaWev-flibuzFUy_S4O9qN-N2UWX2AAI7BgACjKGARXTb7-FUQxBzNgQ',
                         caption='''⬆️⬆️⬆️

*НОВАЯ ПРАКТИКА-МЕДИТАЦИЯ*
🔥🔥🔥

*«СОЗДАНИЕ ВНУТРЕННЕГО РЕСУРСА И УВЕЛИЧЕНИЕ ЭНЕРГИИ»*

*Энергия ребёнка - это внутренняя энергетическая часть ВАС 
(ваш образ или ощущение себя ребёнком 3-7 лет), которая даёт мощную энергию жизни, созидания, возможности и яркую потребность творить* 🪄 

*Соединение с Высшим Я* ❤️''',
                         parse_mode='markdown', reply_markup=menu_keyboard())


async def meditation_11(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_video(message.chat.id, 'BAACAgIAAxkBAAICbWev-t2bmRdV2FVLEtJZwUZVlU_fAAIQPAAC3ogYSt3MS5lVHoN7NgQ',
                         caption='''ПРОЦЕСС-МЕДИТАЦИЯ 

*ОСВОБОЖДЕНИЕ ОТ СТАРЫХ ДЕСТРУКТИВНЫХ СВЯЗЕЙ И СЛИВА ЭНЕРГИИ*

Данный процесс важно делать некоторое количество раз:

✔️При эмоциональной зависимости от партнера
✔️с бывшими партнерами 
✔️с людьми, с кем была половая связь 
✔️с людьми, с которыми были  напряженные отношения 
✔️с людьми, о которых вы думаете периодически, кто тянет с вас энергию в настоящий момент 

Когда вы думаете об этих людях- это значит, что энергетический контакт не закрыт и важно убрать каналы оттока вашей энергии. 
 
Данную практику можно выполнить на 1 человека (любое количество раз) при получении состояния нейтральности, равнодушия, пустоты и без эмоционального окраса.
 
Данный процесс может выполняться самостоятельно или после входа в новое женское состояние 🧘🏻‍♀️''',
                         parse_mode='markdown', reply_markup=menu_keyboard())


async def meditation_12(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_video(message.chat.id, 'BAACAgIAAxkBAAICWWevgUJtfrZKBdgjaAUMzoxnwMKRAAK_FQAC9k5xSXidPsp2OEPyNgQ',
                         caption='''Медитация

*СОЕДЕНЕНИЕ С СОБОЙ*''',
                         parse_mode='markdown', reply_markup=menu_keyboard())


async def meditation_stack():
    return [meditation_1, meditation_2, meditation_3, meditation_4, meditation_5, meditation_6, meditation_7,
            meditation_8, meditation_9, meditation_10, meditation_11, meditation_12]
