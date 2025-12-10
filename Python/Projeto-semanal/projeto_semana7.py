#Jogo da cobrinha
import tkinter as tk # vai importar tk da biblioteca tkinter
janela = tk.Tk() #vai criar a váriavel da janela
janela.title("Jogo da cobrinha") #da o nome da janela
janela.geometry("400x300") #tamanho da janela

label = tk.Label(janela, text="Oi Python") #adiciona texto na janela
label.pack() #gerencia a geometria,  posiciona em posição relativa

janela.mainloop() #inicia o loop que deixa a janela