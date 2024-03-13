from ytDown import YoutubeDown
from telebot.types import BotCommand, InputFile
from dotenv import load_dotenv
from cardapio import Cardapio
import telebot
import os

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
DOWNLOADS_PATH = os.path.join(ROOT_PATH, 'Download/')
c = Cardapio()

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

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
            os.remove(DOWNLOADS_PATH + title +'.mp3')
        else:
            bot.send_video(
                chat_id = message.chat.id,
                video = open(videoPath, 'rb'),
                caption=f'Título do vídeo: {title}\n'
            )
            os.remove(DOWNLOADS_PATH + title +'.mp4')
            
        
commands = [
    BotCommand(command='/start', description='Iniciar o bot'),
    BotCommand(command='/help', description='Lista de comandos disponíveis'),
    BotCommand(command='/d', description='Baixar um vídeo'),
    BotCommand(command='/a', description='Baixar audio de um video'),
    BotCommand(command='/cardapio', description='Cardápio atual do RU.')
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
    
@bot.message_handler(commands=['cardapio'])
def download_cardapio(message):
    bot.send_message(chat_id=message.chat.id, text="Resgatando cardápio de hoje!")
    url = c.get()
    bot.send_document(chat_id=message.chat.id, document=url, caption="Cardápio de hoje no RU.")
    
print("Bot rodando ;)...")
bot.infinity_polling() 