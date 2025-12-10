import tkinter as tk
janela = tk.Tk()

janela.title("Essa é minha janela")
janela.geometry("400x300")

label = tk.Label(janela, text="Janela com tamanho definido").pack()

janela.mainloop()