from loader import bot
from database.db import list_notes
from telebot.types import CallbackQuery
from keyboards.inline import delete_note_kb
from handlers.custom_handlers.add import save_note



@bot.callback_query_handler(func=lambda call: call.data == "add")
def add_handler(call: CallbackQuery):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Введите текст новой заметки:")
    bot.register_next_step_handler(call.message, save_note)


@bot.callback_query_handler(func=lambda call: call.data == "delete")
def delete_handler(call: CallbackQuery):
    notes = list_notes(call.from_user.id)
    bot.answer_callback_query(call.id)
    for index, (note_id, query, created_at) in enumerate(notes, start=1):
        bot.send_message(
            call.message.chat.id,
            f"{index}) {query}",
            reply_markup=delete_note_kb(note_id)
        )
