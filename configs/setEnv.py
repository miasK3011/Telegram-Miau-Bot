try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("Acho que esqueceu de instalar os requirements.txt?? :(")

def setEnvironment():
    import os
    import telebot
    from configs.cfg import DOWNLOADS_PATH, ROOT_PATH

    BOT_TOKEN = ""
    if os.getenv("ENV") == "prod":
        BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    else:
        BOT_TOKEN = os.getenv("BOT_TOKEN_DEV", "")

    bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)
    
    return bot