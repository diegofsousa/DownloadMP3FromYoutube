# -*- coding: iso-8859-1 -*-

from urllib2 import urlopen
from threading import Thread
import youtube_dl
from bs4 import BeautifulSoup
from youtube_dl import DownloadError

def search_para_url(string):
    string = '+'.join(string.split())
    url = 'https://www.youtube.com/results?search_query=' + string
    print url
    try:
        request = urlopen(url)
        soup = BeautifulSoup(request.read(), 'html.parser')
        tag = soup.find('a', {'rel': 'spf-prefetch'})
        titulo = tag.string
        video_url = 'https://www.youtube.com' + tag.get('href')
        return titulo, video_url
    except AttributeError as e:
        return False, False

def baixar_musica(titulo, video_url,):
    try:
        ydl_opts = {
            'outtmpl': 'files/'+ titulo + '.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except DownloadError as e:
        return False
    return titulo