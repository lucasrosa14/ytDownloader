# -*- encoding: utf-8 -*
from pytube import YouTube
from tkinter import *
from tkinter import messagebox

tela = Tk()
tela.title('YT Downloader by Frog')
tela.geometry('300x195')
tela.resizable(False, False)
tela.eval('tk::PlaceWindow . center')
tela.configure(bg='darkgrey')

Label(tela, text='URL:',bg='darkgrey', fg='#000000').place(x=10, y=10)
tb_url = Entry(tela)
tb_url.place(x=40, y=10, width=250, height=20)

btn_download = Button(tela, text='Download',  bg='#000000', fg='#ffffff')
btn_download.place(x=10, y=130, width=280, height=20)

btn_sair = Button(tela, text='Sair', command=tela.destroy, bg='#000000', fg='#ffffff')
btn_sair.place(x=10, y=160, width=280, height=20)

def sel():
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
label.place(x=10, y=100)

tela.mainloop()


