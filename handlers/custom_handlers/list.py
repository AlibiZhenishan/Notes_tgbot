from loader import bot
from telebot.types import Message
from database.db import list_notes
from keyboards.inline import delete_note_kb, yes_no


@bot.message_handler(commands=["list"])
def show_notes(message: Message):
    notes = list_notes(message.from_user.id)

    if not notes:
        bot.send_message(
            message.from_user.id ,
            "У вас еще нету заметок, хотите добавить?",
            reply_markup=yes_no())
        return

    for index, (note_id, query, created_at) in enumerate(notes, start=1):
        bot.send_message(
            message.chat.id,
            f"{index}) {query}",
            reply_markup=delete_note_kb(note_id)
        )
