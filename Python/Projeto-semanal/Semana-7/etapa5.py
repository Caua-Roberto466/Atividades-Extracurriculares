import tkinter as tk

janela = tk.Tk()
janela.title("Etapa 5")
janela.geometry("400x300")

label = tk.Label(janela, text="Digite uma frase:").pack()
entrada = tk.Entry(janela)
entrada.pack()

def exibir():
    texto_digitado = entrada.get()
    print("Você digitou: ",texto_digitado)

botao = tk.Button(janela, text="Aperte para exibir", command=exibir).pack()

janela.mainloop()