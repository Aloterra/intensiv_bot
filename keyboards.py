from telebot import types


def start_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    courses_button = types.InlineKeyboardButton('🎓 Интенсив', callback_data='confirmation')
    contact_button = types.InlineKeyboardButton('✉️ Контакты', callback_data='contact')
    markup.row(courses_button, contact_button)
    meditation_button = types.InlineKeyboardButton('🧘‍♀️ Медитации', callback_data='meditation')
    questions_button = types.InlineKeyboardButton('❓ Часто задаваемые вопросы', callback_data='questions')
    manager_button = types.InlineKeyboardButton('💬 Написать менеджеру', url='https://t.me/puertorcen')
    markup.add(meditation_button, questions_button, manager_button)
    return markup


def contact_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    chanel_button = types.InlineKeyboardButton('Telegram канал', callback_data='chanel')
    site_button = types.InlineKeyboardButton('Сайт', callback_data='site')
    manager_button = types.InlineKeyboardButton('Менеджер', url='https://t.me/puertorcen')
    menu_button = types.InlineKeyboardButton('В меню', callback_data='menu_edit')
    markup.row(chanel_button)
    markup.row(site_button, manager_button)
    markup.row(menu_button)
    return markup


def questions_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    first_button = types.KeyboardButton('Вопрос 1')
    second_button = types.KeyboardButton('Вопрос 2')
    third_button = types.KeyboardButton('Вопрос 3')
    fourth_button = types.KeyboardButton('Вопрос 4')
    fifth_button = types.KeyboardButton('Вопрос 5')
    markup.add(first_button, second_button, third_button, fourth_button, fifth_button)
    return markup


def answer_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    other_button = types.InlineKeyboardButton('Другой вопрос', callback_data='questions')
    menu_button = types.InlineKeyboardButton('≡ Меню', callback_data='menu_delete')
    markup.add(other_button, menu_button)
    return markup


def confirmation_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    confirmation_button = types.InlineKeyboardButton('Купить', callback_data='approve')
    return_button = types.InlineKeyboardButton('Назад', callback_data='menu_edit')
    markup.add(confirmation_button, return_button)
    return markup


def payment_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    payment_button = types.InlineKeyboardButton('Да, купить', pay=True)
    return_button = types.InlineKeyboardButton('Назад в меню', callback_data='menu_delete')
    markup.add(payment_button, return_button)
    return markup


def menu_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    return_button = types.InlineKeyboardButton('Назад в меню', callback_data='menu_edit')
    markup.add(return_button)
    return markup
