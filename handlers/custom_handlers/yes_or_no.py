from loader import bot
from telebot.types import CallbackQuery
from handlers.custom_handlers.add import save_note



@bot.callback_query_handler(func=lambda call: call.data == "yes")
def yes_handler(call: CallbackQuery):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Введите текст новой заметки:")
    bot.register_next_step_handler(call.message, save_note)


@bot.callback_query_handler(func=lambda call: call.data == "no")
def no_handler(call: CallbackQuery):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Хорошо")
