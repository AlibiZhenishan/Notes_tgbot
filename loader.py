from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from dotenv import load_dotenv
from database.db import init_db

load_dotenv()

init_db()
BOT_TOKEN = "8386018708:AAGxHbaYoMLzU-VZrSn7v-uVphp650vYqmc"
storage = StateMemoryStorage()
bot = TeleBot(BOT_TOKEN, state_storage=storage,  use_class_middlewares=True)