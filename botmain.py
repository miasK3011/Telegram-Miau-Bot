import os
import telebot
from dotenv import load_dotenv

from configs.cfg import BOT_COMMANDS, DOWNLOADS_PATH

from configs.setEnv import setEnvironment
from features.cardapio import Cardapio 
from features.catAPI import getCatImage
from features.dogAPI import getDogImage
from features.ytDown import YoutubeDown
from features.utils.sendFile import sendFile 

c = Cardapio()

bot = setEnvironment()
bot.set_my_commands(BOT_COMMANDS)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "E ai minha gatinha? Esse bot baixa videos do youtube :)).\nEm breve mais funcionalidades!!",
    )

@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(message, "/yt: Baixa um video de um link dado.")

@bot.message_handler(commands=["yt"])
def download_from_link(message):
    link = message.text
    link = link.split()[1]
    yt = YoutubeDown(link)
    file = yt.downloadVideo()
    sendFile(message, file, False, bot)

@bot.message_handler(commands=["a"])
def download_only_audio(message):
    link = message.text
    link = link.split()[1]
    yt = YoutubeDown(link)
    file = yt.downloadAudio()
    sendFile(message, file, True, bot)

@bot.message_handler(commands=["cardapio"])
def download_cardapio(message):
    bot.send_message(chat_id=message.chat.id, text="Resgatando cardápio de hoje!")
    filename, error = c.get()

    if error:
        print(error)
        bot.send_message(chat_id=message.chat.id, text=f"Erro ao resgatar cardápio :(")
        return

    if filename:
        with open(filename, "rb") as pdf_file:
            bot.send_document(
                chat_id=message.chat.id,
                document=pdf_file,
                caption="Cardápio de hoje no RU.",
            )
        os.remove(filename)

@bot.message_handler(commands=["gato"])
def send_cat_image(message):
    cat_url = getCatImage()
    if cat_url == None:
        bot.send_message(
            chat_id=message.chat.id, text="Gatinhos não tão afim de aparecer :("
        )
    else:
        bot.send_photo(chat_id=message.chat.id, photo=cat_url)

@bot.message_handler(commands=["cachorro"])
def send_dog_image(message):
    dog_url = getDogImage()
    if dog_url == None:
        bot.send_message(
            chat_id=message.chat.id, text="Cachorrinhos não tão afim de aparecer :("
        )
    else:
        bot.send_photo(chat_id=message.chat.id, photo=dog_url)

print("Bot rodando ;)...")
bot.infinity_polling()