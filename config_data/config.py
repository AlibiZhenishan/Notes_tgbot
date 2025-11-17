import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

DB_PATH = "database.db"
BOT_TOKEN = os.getenv("BOT_TOKEN")
DEFAULT_COMMANDS = (
    ("add ", "добавить новую задачу.\n"),
    ("list", "показать все текущие задачи\n"),
)

DATE_FORMAT = "%d.%m.%Y"




