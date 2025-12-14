import tkinter as tk
import random

janela = tk.Tk()
janela.title("Criando a comida")
janela.geometry("350x350")

#comida
x_comida = random.randint(0, 325)
y_comida = x_comida
tamanho_comida = 10

canvas = tk.Canvas(janela, width=325, height=325, bg="black")
canvas.pack(pady=13)

canvas.create_rectangle(
    x_comida, y_comida,
    x_comida + tamanho_comida, y_comida + tamanho_comida,
    fill="red",
    outline="blue",
    width=1
)

janela.mainloop()