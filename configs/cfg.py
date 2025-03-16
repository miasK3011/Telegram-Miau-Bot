import os
from telebot.types import BotCommand

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
DOWNLOADS_PATH = os.path.join(ROOT_PATH, "Download/")

BOT_COMMANDS = [
    BotCommand(command="/start", description="Iniciar o bot"),
    BotCommand(command="/help", description="Lista de comandos disponíveis"),
    BotCommand(command="/yt", description="Baixar um vídeo do youtube"),
    BotCommand(command="/a", description="Baixar audio de um video"),
    BotCommand(command="/cardapio", description="Cardápio atual do RU."),
    BotCommand(command="/gato", description="Gato aleatorio"),
    BotCommand(command="/cachorro", description="Cachorro aleatorio"),
]