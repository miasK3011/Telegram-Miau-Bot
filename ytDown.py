import yt_dlp

class YoutubeDown():
    def __init__(self, link:str):
        self.link = link
        
        self.ydl_videoOptions = {
            'outtmpl': 'Out/%(title)s.%(ext)s',
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'
        }
        
        self.ydl_audioOptions = {
            'outtmpl': 'Out/%(title)s.%(ext)s',
            'format': 'bestaudio[ext=m4a]/mp4'
        }

    def downloadVideo(self):
        try:
            ydl = yt_dlp.YoutubeDL(self.ydl_videoOptions)
            ydl.download([self.link])
            info_video = ydl.extract_info(self.link, download=False)
        except:
            return -1
        
        return info_video
    
    def downloadAudio(self):
        try:
            ydl = yt_dlp.YoutubeDL(self.ydl_audioOptions)
            ydl.download([self.link])
            info_audio = ydl.extract_info(self.link, download=False)
        except:
            return -1
        
        return info_audio