from telebot import types


def start_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    courses_button = types.InlineKeyboardButton('Войти в GUNA ИЗОБИЛИЯ 🎇', callback_data='confirmation')
    meditation_button = types.InlineKeyboardButton('Все медитации канала 🧘🏻‍♀️', callback_data='meditation')
    questions_button = types.InlineKeyboardButton('Вопросы и ответы ❓', callback_data='questions')
    markup.add(courses_button, meditation_button, questions_button)
    manager_button = types.InlineKeyboardButton('Tех. Поддержка 🛠️', url='https://t.me/puertorcen')
    anna_button = types.InlineKeyboardButton('Анастасия Гун 💬', url='https://t.me/AnastasiaGunina')
    chanel_button = types.InlineKeyboardButton('Канал «Включи реальность» 💡', url='https://t.me/Anastasia_gun_in')
    markup.row(anna_button, manager_button)
    markup.add(chanel_button)
    return markup


def questions_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    first_button = types.KeyboardButton('Чем отличаются бесплатные медитации от интенсива GUNA ИЗОБИЛИЯ?')
    second_button = types.KeyboardButton('Какой формат у интенсива GUNA ИЗОБИЛИЯ?')
    third_button = types.KeyboardButton('Какая стоимость у интенсива GUNA ИЗОБИЛИЯ?')
    fourth_button = types.KeyboardButton('Сколько длится интенсив GUNA ИЗОБИЛИЯ и как долго доступны материалы?')
    markup.add(first_button, second_button, third_button, fourth_button)
    return markup


def answer_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    other_button = types.InlineKeyboardButton('Другой вопрос 🔁', callback_data='questions')
    menu_button = types.InlineKeyboardButton('Меню ≡', callback_data='menu_delete')
    markup.add(other_button, menu_button)
    return markup


def confirmation_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    confirmation_button = types.InlineKeyboardButton('Купить 👑', callback_data='approve')
    return_button = types.InlineKeyboardButton('Назад 🔙', callback_data='menu_delete')
    markup.add(confirmation_button, return_button)
    return markup


def payment_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    payment_button = types.InlineKeyboardButton('Оплатить 💸', pay=True)
    return_button = types.InlineKeyboardButton('Назад в меню 🔙', callback_data='menu_delete')
    markup.add(payment_button, return_button)
    return markup


def menu_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    return_button = types.InlineKeyboardButton('Назад в меню 🔙', callback_data='menu_delete')
    markup.add(return_button)
    return markup


def meditation_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    meditations_names = [
        "ДЫХАНИЕ ЖИЗНИ", "УВЕЛИЧЕНИЕ ЭНЕРГИИ", "МЕДИТАЦИЯ ЛЮБВИ", "ОТПУСКАНИЕ ЧУЖОЙ ЭНЕРГИИ",
        "ДОВЕРИЕ И БОЖЕСТВЕННАЯ СУТЬ", "РАССЛАБЛЕНИЕ ПЕРЕД СНОМ", "СОНАСТРОЙКА С ЭНЕРГИЯМИ ДНЯ", "ПОВЫШЕНИЕ ВИБРАЦИЙ",
        "РАБОТА С ВНУТРЕННИМ ДИАЛОГОМ", "СОНАСТРОЙКА НА ЭНЕРГИЮ", "ОСВОБОЖДЕНИЕ ОТ СТАРЫХ СВЯЗЕЙ",
        "СОЕДИНЕНИЕ С ИСТИННЫМ СОБОЙ"
    ]
    meditation_number = 0
    for i in meditations_names:
        button = types.InlineKeyboardButton(i, callback_data=f'{meditation_number}_meditation-media')
        meditation_number += 1
        markup.add(button)
    return_button = types.InlineKeyboardButton('Назад в меню 🔙', callback_data='menu_delete')
    markup.add(return_button)
    return markup
