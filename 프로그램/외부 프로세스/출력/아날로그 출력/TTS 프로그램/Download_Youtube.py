from pytube import YouTube
import os

def downloadYouTube(videourl, path):
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    real_path = path  + "\\" + yt.title
    if not os.path.exists(real_path):
        os.makedirs(real_path)
    yt.download(real_path)
    return yt.title
    
video_path = 'https://www.youtube.com/watch?v=VeLGRh_bB9k'
downloadYouTube(video_path, 'C:\\Users\\ssmma\\Documents\\신성민\\데이터\\TTS용 데이터\\유튜브 다운로더\\videos')