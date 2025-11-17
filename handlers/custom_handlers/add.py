from telebot.types import Message
from database.db import add_note
from loader import bot
from keyboards.inline import yes_no

@bot.message_handler(commands=["add"])
def bot_add(message: Message):
    bot.send_message(message.chat.id, "Введите текст заметки: ")
    bot.register_next_step_handler(message, save_note)

def save_note(message: Message):
    add_note(message.from_user.id, message.text)
    bot.send_message(message.chat.id, "Заметка успешно сохранена! Хотите добавить еще заметок? ", reply_markup=yes_no())