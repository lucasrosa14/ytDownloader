# -*- encoding: utf-8 -*
from tkinter.ttk import Progressbar

from pytube import YouTube
from tkinter import *
from tkinter import messagebox
import os

def valida_url():
    global url_video
    url_video = tb_url.get()
    #print(url_video)

def ytdownloader():
    if var.get() == 1:
        #print('Iniciando download do vídeo...')
        video = YouTube(url_video).streams.get_highest_resolution()
        video.download()
        #print('Download do vídeo concluído!')
        messagebox.showinfo(message='Download do vídeo concluído!')
        tb_url.delete(0, END)
        var.set(None)
    elif var.get() == 2:
        #print('Iniciando download do áudio...')
        audio = YouTube(url_video).streams.filter(only_audio=True)[0]
        downloaded_file = audio.download()
        title_mp3 = YouTube(url_video).title + '.mp3'
        os.rename(downloaded_file, title_mp3)
        #print('Download do áudio concluído!')
        messagebox.showinfo(message='Download do áudio concluído!')
        tb_url.delete(0, END)
        var.set(None)
    else:
        messagebox.showerror(message='Selecione um tipo de download, informe a URL e click em "Check URL"!')

tela = Tk()
tela.title('YT Downloader by Frog')
tela.geometry('300x195')
tela.resizable(False, False)
tela.eval('tk::PlaceWindow . center')
tela.configure(bg='darkgrey')

Label(tela, text='URL:',bg='darkgrey', fg='#000000').place(x=10, y=10)
lbl_url = StringVar()
tb_url = Entry(tela, textvariable=lbl_url)
tb_url.place(x=40, y=10, width=250, height=20)

def sel():
    global var
    if var.get() == 1:
       option = 'vídeo'
    else:
       option = 'áudio'
    selection = "Você selecionou: "+ str(option)
    label.config(text = selection)

var = IntVar()
R1 = Radiobutton(tela, text="Vídeo", variable=var, value=1,
                  command=sel, bg='darkgrey', fg='#000000')
R1.place(x=10, y=60)

R2 = Radiobutton(tela, text="Áudio", variable=var, value=2,
                  command=sel, bg='darkgrey', fg='#000000')
R2.place(x=10, y=80)

label = Label(tela,text="Escolha a forma de Download",bg='darkgrey', fg='#000000')
label.place(x=10, y=40)

label = Label(tela,bg='darkgrey', fg='#000000')
label.place(x=160, y=80)

btn_url = Button(tela, text='Check URL',  command=valida_url, bg='#000000', fg='#ffffff')
btn_url.place(x=210, y=40, width=80, height=20)

btn_download = Button(tela, text='Download',  command=ytdownloader, bg='#000000', fg='#ffffff')
btn_download.place(x=10, y=130, width=280, height=20)

btn_sair = Button(tela, text='Sair', command=tela.destroy, bg='#000000', fg='#ffffff')
btn_sair.place(x=10, y=160, width=280, height=20)

tela.mainloop()




