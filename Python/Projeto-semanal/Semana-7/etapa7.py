import tkinter as tk

janela = tk.Tk()
janela.title("Etapa 7")
janela.geometry("300x200")

label1 = tk.Label(janela, text="Qual seu nome?", fg="blue").pack()
nome_entrada = tk.Entry(janela)
nome_entrada.pack()

label2 = tk.Label(janela, text="Qual sua idade", fg="Red").pack()
idade_entrada = tk.Entry(janela)
idade_entrada.pack()

resultado = tk.Label(janela, text="Aperte no botão", fg="green")
resultado.pack()

def exibir():
    nome = nome_entrada.get()
    idade = idade_entrada.get()
    resultado.config(text=(f"Olá {nome} você tem {idade} anos"))

botao = tk.Button(janela, text="Exibir", command=exibir).pack()

janela.mainloop()