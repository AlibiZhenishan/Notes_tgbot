from loader import bot
from handlers.custom_handlers import nots, yes_or_no,add,delete,list
from telebot.custom_filters import StateFilter
from utils.set_bot_commands import set_default_commands




if __name__ == '__main__':
    set_default_commands(bot)
    bot.add_custom_filter(StateFilter(bot))
    bot.infinity_polling()