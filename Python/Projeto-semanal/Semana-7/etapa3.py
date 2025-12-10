import tkinter as tk
janela = tk.Tk()
janela.title("Etapa 3")

label1 = tk.Label(janela, text="Texto de cima").pack()

label2 = tk.Label(janela, text="Texto do meio").pack()

label3 = tk.Label(janela, text="Texto de baixo").pack()

janela.mainloop()