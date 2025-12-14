import tkinter as tk
import random

janela = tk.Tk()
janela.title("Comendo a comida")
janela.geometry("350x350")
janela.resizable(False, False)
janela.focus_set()

#Posição da cobra
x = 5
y = 5
tamanho_cobra = 10

#Posição da comida
x_comida = random.randint(0, 315)
y_comida = random.randint(0, 315)
tamanho_comida = 10

#Funções
#Função de comer
def comer():
    coordenadas_cobra = canvas.coords(cobra)
    coordenadas_comida = canvas.coords(comida)

    if (
        coordenadas_cobra[0] < coordenadas_comida[2] and
        coordenadas_cobra[2] > coordenadas_comida[0] and
        coordenadas_cobra[1] < coordenadas_comida[3] and
        coordenadas_cobra[3] > coordenadas_comida[1]
    ):
        return True
    return False

#Função de mover
def mover(event):
    global x
    global y
    if event.keysym == "Up":
        y -=7
        canvas.move(cobra, 0, -7)
    elif event.keysym == "Down":
        y +=7
        canvas.move(cobra, 0, 7)
    elif event.keysym == "Left":
        x -=7
        canvas.move(cobra, -7, 0)
    elif event.keysym == "Right":
        x +=7
        canvas.move(cobra, 7, 0)
    if comer():
        print("Comeu")


#canvas
canvas = tk.Canvas(janela, width=325, height=325, bg="black")
canvas.pack(pady=13)

#Criação da comida
comida = canvas.create_rectangle(
    x_comida, y_comida,
    x_comida + tamanho_comida, y_comida + tamanho_comida,
    fill="red",
    outline="blue",
    width=1
)

#Criacção da cobra
cobra = canvas.create_rectangle(
    x, y,
    x + tamanho_cobra, y + tamanho_cobra,
    fill="green",
    outline="black",
    width=1
)

#Detecta a tecla pressionada
janela.bind("<KeyPress>", mover)

janela.mainloop()