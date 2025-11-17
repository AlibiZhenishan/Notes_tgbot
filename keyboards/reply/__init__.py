from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

reply_markup = ReplyKeyboardRemove()

def gen_markup():
    button_1 = KeyboardButton(text="/add")
    button_2 = KeyboardButton(text="/list")
    button_3 = KeyboardButton(text="/help")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_1, button_2, button_3)
    return keyboard