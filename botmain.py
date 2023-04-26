from ytDown import downloadFromLink
from telebot.types import BotCommand
import telebot
import os

bot = telebot.TeleBot("1738497367:AAFB3hKYoPZr60m1fkCdFhOjVGFSktp80Dc", parse_mode=None)
updates = bot.get_updates()

commands = [
    BotCommand(command='/start', description='Iniciar o bot'),
    BotCommand(command='/help', description='Lista de comandos disponíveis'),
    BotCommand(command='/d', description='Baixar um vídeo')
]

bot.set_my_commands(commands)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "E ai minha gatinha? Esse bot baixa videos do youtube :)).\nEm breve mais funcionalidades!!")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "/d: Baixa um video de um link dado.")

@bot.message_handler(commands=['d'])
def download_from_link(message):
    downVideo = downloadFromLink(message.text)
    if downVideo == -1:
        bot.reply_to(message, "Por algum motivo não foi possivel baixar :p")
    else:
        bot.reply_to(message, "Download Feito!!")
        bot.send_video(chat_id= message.chat.id,
                       video = open('/home/mias/Documentos/Github/Telegram Bots/Mias/Python/miasBot/Out/'+ downVideo.title +'.mp4', 'rb'),
                       caption='Título do video: ' + downVideo.title + '\n')
        os.remove('/home/mias/Documentos/Github/Telegram Bots/Mias/Python/miasBot/Out/'+ downVideo.title +'.mp4')

bot.infinity_polling() 