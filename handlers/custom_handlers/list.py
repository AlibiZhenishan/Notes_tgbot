from telebot.types import Message

from database.db import list_notes
from keyboards.inline import nots, yes_no
from loader import bot


@bot.message_handler(commands=["list"])
def show_notes(message: Message):
    notes = list_notes(message.from_user.id)
    listt = "Ваши задачи: \n\n"

    if not notes:
        bot.send_message(
            message.from_user.id ,
            "У вас еще нету заметок, хотите добавить?",
            reply_markup=yes_no())
        return

    for index, (note_id, query, created_at) in enumerate(notes, start=1):
        listt += f"{index}) {query}\n"

    bot.send_message(message.chat.id, listt)

    bot.send_message(message.chat.id,
                     "Вы хотите изменить задачи?",
                     reply_markup=nots())
