from loader import bot
from database.db import delete_note


@bot.callback_query_handler(func=lambda call: call.data.startswith("del_"))
def delete_note_callback(call):
    note_id = int(call.data.split("_")[1])
    delete_note(note_id)

    bot.answer_callback_query(call.id, "Заметка удалена!")
    bot.delete_message(call.message.chat.id, call.message.message_id)