# >>> from pytube import YouTube
# >>> YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
# >>> yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
# >>> yt.streams
# ... .filter(progressive=True, file_extension='mp4')
# ... .order_by('resolution')
# ... .desc()
# ... .first()
# ... .download()

from http.client import IncompleteRead
from urllib.error import URLError
from pytube import YouTube

# url = "https://www.youtube.com/watch?v=QQVkMSsB_9Q&list=PLrSOXFDHBtfED_VFTa6labxAOPh29RYiO&index=16&pp=iAQB"
# youtube_video = YouTube(url)

# for stream in youtube_video.streams.fmt_streams:
#     print(" ",stream)

# stream = youtube_video.streams.get_highest_resolution()
# print("TITRE: " + youtube_video.title)
# print("telechargement...")
# try:
#   stream.download()
# except ConnectionRefusedError:
#   print("la cannexion n'as pas pu être etablie")
# except IncompleteRead:
#    print("la connexion a été coupé")
# except URLError as u:
#    print("une connexion existante à dû être fermé")
# else:
#    print('Ok')

