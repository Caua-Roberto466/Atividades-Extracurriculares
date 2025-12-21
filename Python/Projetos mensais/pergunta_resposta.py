#Jogo de pergunta e resposta com interface
import tkinter as tk

janela = tk.Tk()
janela.title("Perguntas e respostas")
janela.geometry("500x270")
janela.resizable(False, False)

#Cria o dicionário das perguntas
perguntas = {
    1:{'pergunta': 'Qual a cor do céu?',
        'A': 'A) Roxo', 
        'B': 'B) Azul', 
        'C': 'C) Verde'},
    2:{'pergunta': 'Quando foi declarado a pandemia da Covid?',
       'A': 'A) 2009',
       'B': 'B) 2019',
       'C': 'C) 2020'}
}

gabarito = ['B', 'C'] #Armazena a ordem correta das respostas

controle = 1 #váriavel de controle
controle_gabarito = 0 #controla os índices do gabarito

pergunta_label = tk.Label(janela, text=perguntas[controle]['pergunta'], font=("Helvetica", 15))
pergunta_label.pack(pady=16)

#alternativas
#a
alternativa_a = tk.Label(janela, text=perguntas[controle]['A'], font=("Arial", 10))
alternativa_a.place(x=3, y=50)
#b
alternativa_b = tk.Label(janela, text=perguntas[controle]['B'], font=("Arial", 10))
alternativa_b.place(x=3, y=70)
#c
alternativa_c = tk.Label(janela, text=perguntas[controle]['C'], font=("Arial", 10))
alternativa_c.place(x=3, y=90)

#Gerencia os pontos do jogador
pontos = 0
pontos_label = tk.Label(janela, text=f'Pontos: {pontos}')
pontos_label.place(x=3, y=1)

def adicionar():
    global controle
    if controle < len(perguntas):
        controle += 1
        pergunta_label.config(text=perguntas[controle]['pergunta'])
        alternativa_a.config(text=perguntas[controle]['A'])
        alternativa_b.config(text=perguntas[controle]['B'])
        alternativa_c.config(text=perguntas[controle]['C'])

botao = tk.Button(janela, text="Botão", command=adicionar)
botao.pack()

janela.mainloop()