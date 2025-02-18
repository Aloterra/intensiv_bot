from telebot.async_telebot import AsyncTeleBot

import base
from config import *

bot = AsyncTeleBot(TOKEN)


async def day_1(user_id: int):
    await bot.send_message(user_id, '''*День 1: Активация многомерного видения

    Дорогие, добро пожаловать на первый день 
    GUNA ИЗОБИЛИЯ!* 🎉 

    Сегодня важный день ❤️
    Вы начинаете создание совершенно нового восприятия и взаимодействия со своим внутренним миром, которое рождает наилучшие сценарии, отношения, ресурсы и абсолютное изобилие в вашей жизни. 

    _Организационные моменты_: 

    ➡️ *Каждый день, в этот GUNA-бот, на протяжении 7 дней, вы будете получать ежедневные многомерные знания в изобилии: 

    Лекции-активации (в видео/аудио формате) и энергетические процессы- медитации, аудио-программирование.

    Это глубокая психотерапевтическая работа с бессознательным, энергией и сознанием. Медитация- это лишь часть, позволяющая расслабить ум, снять тревогу и создать глубокий внутренний контакт. Энергетические процессы - это глубинная активация многомерного видения, освобождающая от бессознательных ограничений ума, расширяющая сознание и создающая счастливую женскую судьбу и изобилие во всех его проявлениях. 

    Доступ к концентрации знаний GUNА ИЗОБИЛИЯ 3 месяца, со дня приобретения.*

    Итак…❤️
    *Сегодня на лекции, вы узнаете самую главную духовную истину, которая преображает всю материю!* 

    А сегодняшний энергетический процесс-медитация поможет вам выйти за пределы ограничивающих рамок и программ, активировать самую высокую вибрационную частоту - сердца и соединенности со всем миром, тотально погружая вас в идентификацию с Творцом, ведь в сути своей, вы и есть Творец всей своей реальности! 

    ❕*Помните, на протяжении всей этой недели важно давать поддержку телу - физические нагрузки (прогулки, растяжка, ходьба, тренировки, ванны с солью) необходимы для качественной интеграции изменений на всех уровнях - энергетическом, психическом и физическом, чтобы эмоциональный план был стабилен.* 

    Чудесного погружения в новое изобильное восприятие, дорогие! ❤️❤️❤️
    
    _Материалы интенсива будут приходить в этот бот ежедневно, в 3.00 по мск, чтобы каждое, даже самое раннее утро, вы начинали вместе с GUNA ИЗОБИЛИЯ ❤️_''',
                           parse_mode='markdown')
    await bot.send_photo(user_id,
                         '''AgACAgIAAxkBAAO7Z6XUuIJp-f-L7qnsnYtk3frEn6sAAo_pMRt5CgFJxyffGqiS_9MBAAMCAAN5AAM2BA''')
    await bot.send_video(user_id, '''BAACAgIAAxkBAAO9Z6XVEOscNlc8qD0kRiO0sK2dJ5IAAlFiAALTeHlIgxrO8Ju7Wo82BA''')
    await bot.send_video(user_id, '''BAACAgIAAxkBAAO_Z6XVIx9sV5n8MQqNKrfxCtQSZhAAAvNnAAInHaFIqdzqUx5OxiU2BA''')


async def day_2(user_id: int):
    await bot.send_message(user_id, '''*День 2: Женская и сексуальная энергия — источник изобилия.*

Добро пожаловать во второй день GUNA ИЗОБИЛИЯ! 💫

*Сегодня мы погружаемся в один из самых мощных источников изобилия — вашу женскую энергию и сексуальность.*

Этот день посвящён раскрытию вашей истинной дикой природы, соединению с внутренней Богиней, которая легко создаёт любовь, изобилие и гармонию в каждой сфере своей жизни! 

Вы узнаете, как ощущать лёгкость и радость, наполняя каждый день ощущением мягкой силы и красоты.

*Энергетический процесс позволит вам освободиться от ограничивающих программ и страхов, которые мешали раскрыть всепозволяющую энергию, и погрузиться в состояние единства с безграничным источником женской и сексуальной энергии.*

Женская энергия — это магия, и она уже внутри вас! 

Дорогая Богиня! 💎 
Свадхистана-женщина, это энергия Афродиты - изобилия, роскоши, творчества и любви! 

Настало время проявить великую красоту вашего бытия!''', parse_mode='markdown')
    await bot.send_photo(user_id,
                         '''AgACAgIAAxkBAAPBZ6XVZu7D455z0gO8rhtIaFb6S78AAv7lMRsFeAABSWmuKqAryKIdAQADAgADeQADNgQ''')
    await bot.send_video(user_id, '''BAACAgIAAxkBAAPCZ6XVZmUrsRVtFvUfDnMKtQtB7hsAAj1aAAInHZlIwQweFXKyEn42BA''')
    await bot.send_video(user_id, '''BAACAgIAAxkBAAPDZ6XVZr6WAj0j2zF7WESrXinqOhgAAuljAAInHaFIxXSuyO6AwsA2BA''')


async def day_3(user_id: int):
    await bot.send_message(user_id, '''*День 3: Деньги, ресурсы, изобилие.*

Добро пожаловать на третий день GUNA ИЗОБИЛИЯ! 💰 

*Сегодня мы говорим о том, что деньги — это не просто цифры, это система, которая имеет понятные законы и откликается на ваше внутреннее состояние.*

Вы узнаете, как ваши убеждения о деньгах влияют на ваш доход, и начнёте менять своё восприятие, чтобы ресурсы приходили стабильно и в большем обьеме. 

*Сегодняшний энергетический процесс процесс даст возможность ощутить настоящее изобилие и активировать внутренний и внешний поток энергонасыщенных состояний.*

Помните: Изобилие уже здесь, вокруг вас, вы и есть изобилие. 

*Всё, что нужно — это создать новое отношение с собой и окружающими людьми, новое расширяющее и отдающее состояние, выраженное в новых действиях.*

Мощнейшего и самого расширяющего погружения! ❤️‍🔥''', parse_mode='markdown')

    await bot.send_photo(user_id,
                         '''AgACAgIAAxkBAAPHZ6XWL7ZP-01jiwqlajtvd2nNQ6oAA-YxGwV4AAFJkSfYUsATw6QBAAMCAAN5AAM2BA''')
    await bot.send_video(user_id,
                         '''BAACAgIAAxkBAAPIZ6XWL7Tw-gWkuj1Dfjxn7WGFcDUAAi5mAAKD-KlIqzphlmQMS0k2BA''')
    await bot.send_video(user_id,
                         '''BAACAgIAAxkBAAPJZ6XWL57ZYgkDqc1eRAtY33pEBPcAAstjAAInHaFIrSWBV_Mn60M2BA''')


async def day_4(user_id: int):
    await bot.send_message(user_id, '''День 4: Активация счастливой женской судьбы

Добро пожаловать на четвёртый день GUNA ИЗОБИЛИЯ! 🌳 

*Сегодня мы погружаемся в создание новых изобильных жизненных сценариев. *

Лекция сегодня лаконичная, однако является максимально отрезвляющей и освобождающей от "бесконечных" проработок рода. 

Практика также дает возможность создать новые нейронные связи в отношении с женщинами (женская дружба, поддержка, без конкуренция, доверие) и дарит энергию благополучия, целостности, внутренней опоры для создания счастливой женской судьбы! ❤️

Если в вашей жизни есть сложности в отношениях, измены, любовные треугольники, сложности в отношениях с женщинами, вопросы с телом, красотой и уверенностью - особенно проникнитесь в сегодняшние знания. Выполните практику 3 раза и не забывайте про заботу о теле, чтобы не было так называемых «откатов» и эмоциональных качелей. 

Сегодня вы творите свою новую судьбу через тотальное принятие, прощение и создание новых отношений с главной женщиной в своей жизни - вашей матерью, и всеми женщинами своего рода. 

*Позвольте себе быть счастливой — сегодня, сейчас, отныне и навсегда!* ❤️‍🔥''', parse_mode='markdown')
    await bot.send_photo(user_id,
                         '''AgACAgIAAxkBAAPPZ6XWuGvlrXvLA3JkE8j3E9Sk9XYAAgHmMRsFeAABSQWzCQGFaYDRAQADAgADeQADNgQ''')
    await bot.send_video(user_id,
                         '''BAACAgIAAxkBAAPQZ6XWuFcjx0RgTPKUirY56fc6nKMAAupmAAKD-KlIJkqXdyhXza82BA''')
    await bot.send_audio(user_id,
                         '''CQACAgIAAxkBAAPRZ6XWuOGbXFMDrCZ9g6t-2DI3rUgAAls9AALkQllKhaG50Z6xzQs2BA''',
                         caption='''*ПРОЦЕСС-ПРОРАБОТКА ЖЕНСКИЙ РОД*

➡️

*ЦЕННОСТЬ. 
ВСТАТЬ В КАНАЛ БОГА. ПРОРАБОТКА ГОРДЫНИ/НИКЧЕМНОСТИ. СОЗДАНИЕ СЧАСТЛИВОЙ ЖЕНСКОЙ СУДЬБЫ.*

☝🏽На протяжении всего процесса-проработки мы глубоко дышим 🫁, 
не задерживаем дыхание 

Процесс длится 25 минут, что важно:

▫️Уединенное пространство 
▫️Наушники
▫️Воду во время практики не пьем ❗️
▫️Удерживаем концентрацию в процессе 

Успешного погружения и красивых трансформаций!''', parse_mode='markdown')


async def day_5(user_id: int):
    await bot.send_message(user_id, '''*День 5: Энергетически насыщенные богатые и сексуальные отношения*

Добро пожаловать на пятый день GUNA ИЗОБИЛИЯ! 🩷

*Сегодня мы открываем секрет создания гармоничных и вдохновляющих отношений, наполненных любовью и божественной близостью на всех уровнях.*

Вы узнаете, как повысить уровень энергии в отношениях, а это ключевой момент, чтобы они стали искрометным источником радости и вдохновения, влияющий на качество жизни, здоровья, отношений и реализации.

*Энергетический процесс сегодняшнего дня - это аудио программирование "Пробуждение Богини" невероятно ценный процесс создания нового ментального и энергетического профиля роскошной, желанной, изобильной и сексуальной женщины!*

Эти знания помогут вам создать пространство, где любовь, доверие и страсть соединяются в единое целое и проявляются вдохновляющим потоком в вашей жизни!

Помните: 💕
Отношения — это тотальное отражение вашей энергетики, именно об этом - GUNA Изобилия!''', parse_mode='markdown')
    await bot.send_photo(user_id,
                         '''AgACAgIAAxkBAAPWZ6XXKbTHLvivtZJPkUfN111CPZAAAgPmMRsFeAABScCN-cU2j6GxAQADAgADeQADNgQ''')
    await bot.send_video(user_id,
                         '''BAACAgIAAxkBAAPXZ6XXKcU62_Qp6WC90SzvuEBOF8IAArhnAAKD-LFIdri_rBvu4_o2BA''')
    await bot.send_video(user_id,
                         '''BAACAgIAAxkBAAPYZ6XXKSQZqtILwLI54kcwy7IJKmYAArJlAAKD-LFI9IZzDh2-Y_U2BA''')


async def day_6(user_id: int):
    await bot.send_message(user_id, '''*День 6: Создание здоровья:
Ментального 
Физического 
Энергетического*

Добро пожаловать на шестой день GUNA ИЗОБИЛИЯ! 💪🏽

Сегодня мы фокусируемся на вашем здоровье — физическом, эмоциональном и энергетическом.

*Вы узнаете, как внутреннее состояние влияет на тело и как восстановить баланс, чтобы здоровье стало естественным состоянием в вашей жизни.* 

Сегодня, предлагаю вам медитацию, которую важно включать перед сном, она наполнит вас жизненной силой, 
расширяя пространство для новых удивительных изобильных возможностей, создавая потрясающий контакт с телом.

Ваше тело — это отражение вашего уровня энергии и сознания. 

*Сегодня жизненно важная лекция-активация для создания вашего здоровья, молодости и красоты!* 

_🫂Дорогие, напоминаю о важности заботы о своем теле. Тело- наш храм. Чтобы интегрировать полученную информацию, 
энергию, необходимо быть в контакте с телом, и системно давать ему любовь и заботу в виде физической активности и 
расслабляющих водных процедур._''', parse_mode='markdown')
    await bot.send_photo(user_id,
                         '''AgACAgIAAxkBAAPcZ6XXWn7q76rf4BK6lJkvrE3tVD4AAgXmMRsFeAABSTaM6vtdjK-3AQADAgADeQADNgQ''')
    await bot.send_video(user_id,
                         '''BAACAgIAAxkBAAPdZ6XXWiJ0T222MV0IV9nPpv7fYwUAAhtrAAKD-KlI_52r1DtYmns2BA''')
    await bot.send_audio(user_id,
                         '''CQACAgIAAxkBAAPeZ6XXWiLLBP9X4He8ZhE8DD0DvCUAAmsvAAJowbhJjxMPgo8M8ek2BA''', caption='''💜ЭНЕРГОНАСТРОЙ НОЧЬ - 

Данную медитацию- энергонастрой, мы выполняем ЛЕЖА, перед сном 😴 вы засыпаете под этот процесс, здесь это намеренное погружение в сон👌🏽

Задача - максимальное расслабление и соединение с многомерностью.

Энергонастрой создает:

✔️Мощный контакт с телом, расслабление, и возможность больше сонастроиться со своей оргазмичностью и чувственностью

✔️Активацию интуиции и внутреннего видения (интуиция 👉🏽 напрямую связана с сексуальной энергией) 

✔️Снятие тревожности, беспокойного ума и мыслительной «жвачки»

Вы засыпаете💜, активируя данные интеграции и сонастройку со своим физическим телом и многомерным пространством. 

🫂Самой доброй ночи, Любимые💜🥰''', parse_mode='markdown')


async def day_7(user_id: int):
    await bot.send_message(user_id, '''*День 7: Материализация желаний и намерений*

Дорогие❤️ 
Добро пожаловать на финальный день GUNA ИЗОБИЛИЯ! 

*Сегодня мы погружаемся в самые важные ключи материализации желаний и усиляем энергонасыщенное состояние, которое важно сделать фоном всей вашей жизни!* 

Вы узнаете, как еще больше активировать энергонасыщенное состояние, которое привлекает исполнение самых смелых мечт! 

*Аудио-программирование "Активация пробуждения"- это мощнейшая концентрация пробуждения и формирования глубоких бессознательных программ творения и созидания изобильной и великолепной жизни, это состояние единения и единства, открывающее самые красивые возможности, где вы способны создать абсолютно всё!* 

Любимые! ❤️
Благодарю вас за вашу смелость и доверие! 

Отпустите ожидания, ведь все и всегда происходит самым лучшим образом, все здесь для вас и всегда вовремя. Наслаждайтесь процессом, в этом и есть смысл жизни. В развитии, расширении и наслаждении 🫂''',
                           parse_mode='markdown')
    await bot.send_photo(user_id,
                         '''AgACAgIAAxkBAAPiZ6XXkhbRQlyfcuUWMwS3XarhDHkAAgbmMRsFeAABSSiqHMZS1IQGAQADAgADeQADNgQ''')
    await bot.send_video(user_id,
                         '''BAACAgIAAxkBAAPjZ6XXkukZn44hAq4FaqW5rFTkFWkAAu1qAAKD-KlIypWr43DIQnU2BA''')
    await bot.send_video(user_id,
                         '''BAACAgIAAxkBAAPkZ6XXkjUiOqTnDYg2uTulM3yPzyUAAo5oAAKD-LFIEnMlC_4bc5k2BA''')
    await bot.send_message(user_id, '''Дорогие друзья! ❤️❤️❤️ 

*7 изобильных дней нашего погружения GUNA ИЗОБИЛИЯ подошли к завершению, но для вас интеграция всех процессов, масштабные изменения, трансформации и новое энергонасыщенное проявление  только вступают в свою силу и будут разворачиваться на протяжении нескольких месяцев!* 

*Доступ к материалам- 3 месяца.*

Рекомендую вам пересматривать лекции несколько раз, энергетические процессы выполнять по-вашему внутреннему отклику, а аудиопрограммирование слушать - ежедневно, чтобы новое изобильное бытие стало вашей сутью и красиво разворачивалось в вашей реальности. 

*Если вы хотите поделиться своими впечатлениями, после прохождения интенсива GUNA ИЗОБИЛИЯ, или выразить благодарность автору, вы можете написать лично https://t.me/AnastasiaGunina.*

С любовью, Анастасия Гунина. 
До новых встреч! ❤️''', parse_mode='markdown')


async def day_checker():
    func = [day_2, day_3, day_4, day_5, day_6, day_7]
    users = await base.all_users()
    for user in users:
        day = await base.user_day(user)
        if day <= 5 and not await base.user_is_block(user):
            await func[day](user)
            await base.update_day(user)
            return 1
