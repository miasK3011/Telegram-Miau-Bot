import os
import telebot
from configs.cfg import DOWNLOADS_PATH

def sendFile(message, file, audio=False, bot=telebot.TeleBot(token="", parse_mode=None)):
    if file == -1:
        bot.reply_to(message, 'Por algum motivo não foi possivel baixar :p')
    else:
        bot.reply_to(message, "Download Feito!!")
        title = file.get("title", None)

        arq_list = os.listdir(DOWNLOADS_PATH)
        videoPath = ""

        for arq in arq_list:
            if arq.startswith(title):
                videoPath = os.path.join(DOWNLOADS_PATH, arq)

        if audio:
            bot.send_audio(
                chat_id=message.chat.id, audio=open(videoPath, "rb"), title=title
            )
            os.remove(DOWNLOADS_PATH + title + ".mp3")
        else:
            bot.send_video(
                chat_id=message.chat.id,
                video=open(videoPath, "rb"),
                caption=f"Título do vídeo: {title}\n",
            )
            os.remove(DOWNLOADS_PATH + title + ".mp4")
