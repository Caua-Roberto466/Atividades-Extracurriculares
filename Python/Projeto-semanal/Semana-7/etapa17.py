import tkinter as tk
import random

janela = tk.Tk()
janela.title("Mudando a comida de posição")
janela.geometry("350x350")
janela.resizable(False, False)

#Crindo canvas
canvas = tk.Canvas(janela, width=325, height=325, bg="black")
canvas.pack(pady=13)

#Tamanho da cobra
x = 5
y = 5
tamanho_cobra = 10

dx = 7
dy = 0

#comida
x_comida = random.randint(0, 315)
y_comida = random.randint(0, 315)
tamanho_comida = 10

#desenhando cobra e comida
cobra = canvas.create_rectangle(
    x, y,
    x + tamanho_cobra, y + tamanho_cobra,
    fill="green",
    outline="black",
    width=1
)

comida = canvas.create_rectangle(
    x_comida, y_comida,
    x_comida + tamanho_comida, y_comida + tamanho_comida,
    fill="red"
)

#Funções
def crescer():
    global tamanho_cobra
    tamanho_cobra += 10
    canvas.coords(
        cobra,
        x, y,
        x + tamanho_cobra, y+tamanho_cobra
    )

def comer():
    cobra_coords = canvas.coords(cobra)
    comida_coords = canvas.coords(comida)

    if (
        cobra_coords[0] < comida_coords[2] and
        cobra_coords[2] > comida_coords[0] and
        cobra_coords[1] < comida_coords[3] and
        cobra_coords[3] > comida_coords[1]
    ):
        return True
    return False

def mover_auto():
    global x, y, dx, dy
    x += dx
    y += dy
    canvas.move(cobra, dx, dy)
    janela.after(150, mover_auto)
    if comer():
        crescer()
        x_rand = random.randint(0, 315)
        y_rand = random.randint(0, 315)
        canvas.coords(
            comida,
            x_rand, y_rand,
            x_rand + tamanho_comida,
            y_rand + tamanho_comida
        )

def mudar_dir(event):
    global dx, dy, tamanho_comida
    if event.keysym == "Up":
        dx = 0
        dy = -7
    elif event.keysym == "Down":
        dx = 0
        dy = 7
    elif event.keysym == "Left":
        dx = -7
        dy = 0
    elif event.keysym == "Right":
        dx = 7
        dy = 0

mover_auto()

janela.bind("<KeyPress>", mudar_dir)

janela.mainloop()