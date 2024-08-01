import tkinter as tk
import customtkinter as ct
from customtkinter import CTkTextbox, CTkScrollbar
from pytube import Playlist, YouTube
from threading import Thread
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox, scrolledtext

class AppYoutube(ct.CTk):
    def __init__(self):
        super().__init__()
        # .........Mise en forme
        self.title("Youtube_Downloader - Mvictor")
        self.iconbitmap("Img1.ico")

        largeur_ecran = self.winfo_screenwidth()
        hauteur_ecran = self.winfo_screenheight()
        x = (largeur_ecran - 475) // 2
        y = (hauteur_ecran - 500) // 2
        self.geometry("475x500+{}+{}".format(x,y))
        self.resizable(width=False,height=False)

        self.frame = ct.CTkFrame(self)
        self.frame.grid(row=0,column=0,columnspan=2)
        self.logo = Image.open("Youtube_logo.png")
        self.logo = self.logo.resize((100,100))
        self.logo = ImageTk.PhotoImage(self.logo)
        self.img = ct.CTkLabel(self.frame,image=self.logo,text=None)
        self.img.grid(row=0,column=0)
        self.Ymsg =ct.CTkLabel(self.frame,text="Youtube Downloader")
        font = ("Arial Bold",22,"bold")
        self.Ymsg.configure(font=font)
        self.Ymsg.grid(row=0,column=1)

        self.frame2 = ct.CTkFrame(self)
        self.frame2.place(x=0,y=160)
        self.frame2.grid(row=1,columnspan=2,column=0,ipadx=10,ipady=10,padx=15,pady=15)
        self.link = ct.CTkLabel(self.frame2,text="Lien de la Video/Playlist")
        self.entry_link = ct.CTkEntry(self.frame2,width=200)
        self.link.grid(row=0, column=0,columnspan=1)
        self.entry_link.grid(row=0,column=1,columnspan=1,ipadx=10,ipady=10)

        self.btn_download_video = ct.CTkButton(self.frame2,text="Télécharger Vidéo",command=self.download_video)
        self.btn_download_video.grid(row=2, column=0, pady=10)

        self.btn_download_playlist = ct.CTkButton(self.frame2,text="Télécharger Playlist",command=self.download_playlist)
        self.btn_download_playlist.grid(row=2, column=1, pady=10)

        self.progress_label = ct.CTkLabel(self,text="")
        self.progress_label.grid(row=4,column=0,columnspan=2,pady=5)

        self.output_text = CTkTextbox(self, width=450,height=200)
        self.output_text.grid(row=5,column=0,columnspan=2,padx=15)

    def download_video(self):
        url = self.entry_link.get()
        download_folder = filedialog.askdirectory()

        if download_folder and url:
            def on_download_progress(stream, chunk, bytes_remaining):
                byte = stream.filesize - bytes_remaining
                percent = byte * 100 / stream.filesize
                self.output_text.insert(ct.END, f"Progression_telechargement: {int(percent)}%\n")
                self.output_text.see(ct.END)
                
            try:
                youtube_video = YouTube(url)
                youtube_video.register_on_progress_callback(on_download_progress)
                stream = youtube_video.streams.get_highest_resolution()
                video_title = youtube_video.title
                self.ajuster_font_size(video_title)
                self.progress_label.configure(text="#~{}".format(video_title))
                
                def download():
                    stream.download(output_path=download_folder)
                    self.output_text.insert(ct.END, "Téléchargement Terminé!\n")
                
                download_thread = Thread(target=download)
                download_thread.start()
            except Exception as e:
                messagebox.showerror('Application Error', 'Une Erreur est survenue')
                self.output_text.insert(ct.END, f'[ERREUR]: {str(e)}')

    def download_playlist(self):
        url = self.entry_link.get()
        download_folder = filedialog.askdirectory()

        if download_folder and url:
            try:
                playlist = Playlist(url)
                self.output_text.insert(ct.END, f"Downloading playlist: {playlist.title}\n")
                self.output_text.see(ct.END)
                
                for video in playlist.videos:
                    def on_download_progress(stream, chunk, bytes_remaining):
                        byte = stream.filesize - bytes_remaining
                        percent = byte * 100 / stream.filesize
                        self.output_text.insert(ct.END, f"Progression_telechargement: {int(percent)}% - {video.title}\n")
                        self.output_text.see(ct.END)
                    
                    video.register_on_progress_callback(on_download_progress)
                    stream = video.streams.get_highest_resolution()
                    video_title = video.title
                    self.ajuster_font_size(video_title)
                    self.progress_label.configure(text="#~{}".format(video_title))

                    def download():
                        stream.download(output_path=download_folder)
                        self.output_text.insert(ct.END, f"Téléchargement Terminé pour: {video_title}\n")
                    
                    download_thread = Thread(target=download)
                    download_thread.start()
                    download_thread.join()  # Wait for the current video to finish downloading before starting the next one
            except Exception as e:
                messagebox.showerror('Application Error', 'Une Erreur est survenue')
                self.output_text.insert(ct.END, f'[ERREUR]: {str(e)}')

    def ajuster_font_size(self, video_title):
        text_length = len(video_title)
        font_size = max(14 - text_length // 5, 11)
        font = ("sans-serif", font_size, "normal")
        self.progress_label.configure(font=font, text="#~{}".format(video_title))

if __name__ == '__main__':
    app = AppYoutube()
    app.mainloop()
