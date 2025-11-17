from keyboards.reply import gen_markup
from loader import bot


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.from_user.id,
        "Привет! Я бот для ваших заметок, вы можете легко управлять вашими заметками через меня.\n\n"
        "Чтобы узнать про мои команды выберите или введите /help",
        reply_markup=gen_markup(),
    )
