import pytube

def downloadFromLink(link):
    SAVE_PATH = '/home/mias/Documentos/Github/Telegram Bots/Mias/Python/miasBot/Out'
    try:
        yt = pytube.YouTube(link)
        stream = yt.streams.filter(file_extension='mp4').first()
        stream.download(output_path=SAVE_PATH)
    except:
        return -1
    
    return yt
