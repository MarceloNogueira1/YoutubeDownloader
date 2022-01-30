import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.tix import InputOnly
from turtle import width
from urllib import request
from PIL import Image, ImageTk
from pygame import image

from pytube import YouTube
import datetime
import time

import requests


# Cores -------------------------
preta = "#444466"  # Preta
branca = "#feffff"  # branca
azul = "#6f9fbd"  # azul
azul_marinho = "#38576b"  # valor
co4 = "#403d3d"   # letra
fundo = "#3b3b3b"

# Configurando Janela ------------
janela = Tk()
janela.title('YTDownloader')
janela.geometry('600x430')
janela.configure(bg=fundo)

# Dividindo janela ------------------
frame_cima = Frame(janela, width=600, height=240, bg=fundo, pady=5, padx=0)
frame_cima.grid(row=1, column=0)
frame_baixo = Frame(janela, width=600, height=300, bg=fundo, pady=12, padx=0)
frame_baixo.grid(row=2, column=0, sticky=NW)


# Imagem download--------------------
down = Image.open('D:\Python\Scripts\scripts\images_ytdownloader\download.png')
down = down.resize((50, 50), Image.ANTIALIAS)
down = ImageTk.PhotoImage(down)


# Frame cima ------------------------
logo = Image.open('D:\Python\Scripts\scripts\images_ytdownloader\yt.png')
logo = logo.resize((100, 90), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)

# Logo----
l_logo = Label(frame_cima, image=logo, compound=LEFT,
               bg=fundo, font=('Roboto 12 bold'), anchor='nw')
l_logo.place(x=250, y=10)

# Titulo----
l_name = Label(frame_cima, text='Youtube Downloader', width=32,
               compound=LEFT, bg=fundo, fg=branca, font=('Roboto 16 bold'), anchor='nw')
l_name.place(x=200, y=100)

# URL----
l_url = Label(frame_cima, text='LINK:', bg=fundo, fg=branca,
              font=('Roboto 12 bold'), anchor='nw')
l_url.place(x=60, y=178)

# Barra de pesquisa----
e_url = Entry(frame_cima, width=33, font=10, justify='left', relief=SOLID)
e_url.place(x=130, y=180)


# Textos pós pesquisa-------------------
titulo_video = Label(frame_baixo, text='', wraplength=300, compound=LEFT,
                     bg=fundo, fg=branca, font=('Roboto 14 bold'), anchor='nw')
titulo_video.place(x=250, y=0)

views_video = Label(frame_baixo, text='', bg=fundo,
                    fg=branca, font=('Roboto 10 bold'), anchor='nw')
views_video.place(x=250, y=110)

duracao_video = Label(frame_baixo, text='', bg=fundo,
                      fg=branca, font=('Roboto 10 bold'), anchor='nw')
duracao_video.place(x=250, y=134)

thumb_video = Label(frame_baixo, compound=LEFT, bg=fundo,
                    font=('Roboto 12 bold'), anchor='nw')
thumb_video.place(x=0, y=0)


def pesquisar():
    global img
    url = e_url.get()
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()  # Melhor qualidade
    titulo = yt.title  # Titulo do video
    visualizacoes = yt.views  # Views do video
    duracao = str(datetime.timedelta(seconds=yt.length))  # Duração do video
    foto = yt.thumbnail_url  # Thumbnail do video

    img = Image.open(requests.get(foto, stream=True).raw)
    img = img.resize((230, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    thumb_video['image'] = img
    titulo_video['text'] = "Titulo: " + titulo
    views_video['text'] = "Views: " + str('{:,}'.format(visualizacoes))
    duracao_video['text'] = "Duração: " + str(duracao)


def download_video():
    url = e_url.get()
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download()


# Botao pesquisar
b_buscar = Button(frame_cima, text='BUSCAR', command=pesquisar, width=10,
                  bg=azul_marinho, fg=branca, font=('Arial 10 bold'), relief=RAISED, overrelief=RIDGE)
b_buscar.place(x=440, y=178)

b_down = Button(frame_baixo, image=down, command=download_video,
                bg=fundo, relief=RAISED, overrelief=RIDGE)
b_down.place(x=500, y=100)


janela.mainloop()
