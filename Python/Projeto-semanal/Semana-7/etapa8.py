import tkinter as tk

janela = tk.Tk()
janela.title("Etapa 8")
janela.geometry("400x300")
janela.resizable(False, False)

label1 = tk.Label(janela, text="Oi")
label1.grid(row=0, column=0)

label2 = tk.Label(janela, text="Tudo bem?")
label2.grid(row=0, column=1)

nome_label = tk.Label(janela, text="Nome: ").grid(row=2, column=0)

entrada = tk.Entry(janela)
entrada.grid(row=2, column=1)

janela.mainloop()