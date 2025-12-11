import tkinter as tk
janela = tk.Tk()
janela.title("Etapa 6")
janela.geometry("400x300")

label = tk.Label(janela, text="Digite um texto").pack()
entrada = tk.Entry(janela)
entrada.pack()

texto = tk.Label(janela, text="", fg="red")
texto.pack()

def alterar_texto():
    texto_digitado = entrada.get()
    texto.config(text=texto_digitado)

botao = tk.Button(janela, text="Exibir texto", command=alterar_texto).pack()

janela.mainloop()