import tkinter as tk
def clicar():
    print("Você clicou no botão")

janela = tk.Tk()
janela.title("Botão")

botao = tk.Button(janela, text="Clique no botão do Rafael", command=clicar).pack()

janela.mainloop()