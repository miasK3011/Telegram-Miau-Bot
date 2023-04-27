from ytDown import YoutubeDown
from telebot.types import BotCommand
import telebot
import os

DOWNLOADS_PATH = '/home/mias/Documentos/Github/Telegram Bots/Mias/Python/miasBot/Out'
BOT_TOKEN = open('/home/mias/Documentos/Github/Telegram Bots/telegramToken.txt')

bot = telebot.TeleBot(BOT_TOKEN.read(), parse_mode=None)

def sendFile(message, file, audio = False):
    if file == -1:
        bot.reply_to(message, "Por algum motivo não foi possivel baixar :p")
    else:
        bot.reply_to(message, "Download Feito!!")
        title = file.get('title', None)
        
        arq_list = os.listdir(DOWNLOADS_PATH)
        videoPath = ''
        
        for arq in arq_list:
            if arq.startswith(title):
                videoPath = os.path.join(DOWNLOADS_PATH, arq)
        
        if audio: 
            bot.send_audio(
                chat_id = message.chat.id,
                audio = open(videoPath, 'rb'),
                title = title
            )
            os.remove('/home/mias/Documentos/Github/Telegram Bots/Mias/Python/miasBot/Out/'+ title +'.m4a')
        else:
            bot.send_video(
                chat_id = message.chat.id,
                video = open(videoPath, 'rb'),
                caption=f'Título do vídeo: {title}\n'
            )
            os.remove('/home/mias/Documentos/Github/Telegram Bots/Mias/Python/miasBot/Out/'+ title +'.mp4')
            
        
commands = [
    BotCommand(command='/start', description='Iniciar o bot'),
    BotCommand(command='/help', description='Lista de comandos disponíveis'),
    BotCommand(command='/d', description='Baixar um vídeo'),
    BotCommand(command='/a', description='Baixar audio de um video')
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
    link = message.text
    link = link.split()[1]
    yt = YoutubeDown(link)
    file = yt.downloadVideo()
    sendFile(message, file)
    
    
@bot.message_handler(commands=['a'])
def download_only_audio(message):
    link = message.text
    link = link.split()[1]
    yt = YoutubeDown(link)
    file = yt.downloadAudio()
    sendFile(message, file, True)
    
bot.infinity_polling() 