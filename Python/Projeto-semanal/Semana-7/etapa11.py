import tkinter as tk

janela = tk.Tk()
janela.title("Detectando teclas")
janela.geometry("350x350")
janela.resizable(False, False)

def pressionar(event):
    print(event.keysym)

janela.bind("<KeyPress>", pressionar)

janela.mainloop()