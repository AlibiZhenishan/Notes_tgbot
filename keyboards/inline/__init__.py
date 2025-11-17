from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def delete_note_kb(note_id: int):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Удалить", callback_data=f"del_{note_id}"))
    return markup

def yes_no():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("Да",callback_data="yes"),
        InlineKeyboardButton("Нет",callback_data="no")
    )
    return markup