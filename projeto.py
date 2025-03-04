import os
import sys
from random import *
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Progressbar

from paises import *
from PIL import Image, ImageTk

#cores
co0 = "#444466" #Preta
co1 = "#feffff" #branca
co2 = "#6f9fbd" #azul
co3 = "#38576b"
co4 = "#403d3d"
fundo_cima = "#2aa6a8"

fundo = co1
cor1 = "#f0ba4f"


janela = Tk()
janela.title("Qual o país")
janela.geometry("350x310")
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=172)
frame_cima = Frame(janela, width=350, height=60, bg=fundo_cima, relief="flat",
                    padx=0, pady=0)
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=350, height=300, bg=fundo, relief="flat",
                    padx=10, pady=12)
frame_baixo.grid(row=2, column=0, sticky=NW)
style = ttk.Style(janela)
style.theme_use("default")
style.configure("black.Horizontal.TProgressBar", background="#fcc058")
style.configure("TPrograssBar", tickness = 5)

global pontos, vida, nome_do_pais, img_bandeira

pontos = 0
vida = 3

app_nome = Label(frame_cima, text="QUAL O PAÍS", relief="flat", anchor="center", 
                    font=("Fixedsys 20"), bg=fundo_cima, fg=co1)
app_nome.place(x=15, y=15)

bar = Progressbar(frame_baixo, length=293,
                    style="black.Horizontal.TProgressbar")
bar.place(x=27, y=50)
bar["value"] = pontos

l_score = Label(frame_baixo, text=f"Pontuação: {str(pontos)}", 
                font=("System 17"), bg=fundo, fg=co0)
l_score.place(x=27, y=10)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#imagens vida
img_0 = Image.open(resource_path("img/0.png"))
img_0 = img_0.resize((30, 30))
img_0 = ImageTk.PhotoImage(img_0)

img_1 = Image.open(resource_path("img/1.png"))
img_1 = img_1.resize((30, 30))
img_1 = ImageTk.PhotoImage(img_1)

l_icon_1 = Label(frame_baixo, image=img_1, bg=fundo)
l_icon_1.place(x=229, y=10)

l_icon_2 = Label(frame_baixo, image=img_1, bg=fundo)
l_icon_2.place(x=259, y=10)

l_icon_3 = Label(frame_baixo, image=img_1, bg=fundo)
l_icon_3.place(x=289, y=10)

#labwel para pergunta

l_perguntas = Label(frame_baixo, text="Qual país pertence esta bandeira?",
                    pady=0, padx=0, relief="flat", anchor="center",
                    font=("Ivy 10 bold"), bg=co1, fg=co4)
l_perguntas.place(x=30, y=70)

e_resposta = Entry(frame_baixo, width=15, justify="center", font=("", 12),
                    relief=SOLID)
e_resposta.place(x=178, y=100)

def iniciar_jogo():
    global pontos, vida, nome_do_pais, l_icon_bandeira

    dados = dados_pais()
    nome_do_pais = dados[1]
    imagem = dados[0]
    print(imagem)
    #imagem da bandeira

    img_bandeira = Image.open(resource_path(imagem))
    img_bandeira = img_bandeira.resize((140, 100))
    img_bandeira = ImageTk.PhotoImage(img_bandeira)


    l_icon_bandeira = Label(frame_baixo, image=img_bandeira , bg=fundo, 
                            relief="solid")
    l_icon_bandeira.image = img_bandeira 
    l_icon_bandeira.place(x=30, y=100)

def reiniciar_jogo():
    global pontos, nome_do_pais, vida, img_0, img_1

    pontos = 0
    vida = 3
    bar['value'] = pontos
    l_score.configure(text=f"Pontuação: {str(pontos)}")
    l_icon_1['image'] = img_1
    l_icon_2['image'] = img_1
    l_icon_3['image'] = img_1

    iniciar_jogo()

def game_over():
    global pontos, nome_do_pais, vida, img_0, img_1

    pontos = 0
    vida = 3
    bar['value'] = pontos
    l_score.configure(text=f"Pontuação: {str(pontos)}")
    l_icon_1['image'] = img_1
    l_icon_2['image'] = img_1
    l_icon_3['image'] = img_1

    iniciar_jogo()

def verificar():
    global pontos, vida

    resposta = e_resposta.get()
    if resposta.lower() == nome_do_pais.lower():
        pontos += 10
        l_score.configure(text=f"Pontuação {str(pontos)}")
        bar["value"] = pontos
        e_resposta.delete(0, END)
        iniciar_jogo()
    else:
        messagebox.showerror("Erro", "Você errou")
        if vida == 3:
            l_icon_1["image"] = img_0
        if vida == 2:
            l_icon_2["image"] = img_0
        if vida == 1:
            l_icon_3["image"] = img_0
            messagebox.showerror("Erro", "Você Perdeu")
            game_over() 
        vida -= 1
        

b_resposta = Button(frame_baixo, text="Confirmar", width=10, height=1, bg=co1, 
                    fg=co4, font=("Ivy 8 bold"), relief=RAISED, 
                    overrelief=RIDGE, command=verificar)
b_resposta.place(x=210, y=150)

iniciar_jogo()

janela.mainloop()