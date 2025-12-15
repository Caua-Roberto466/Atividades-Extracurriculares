import tkinter as tk
import random

janela = tk.Tk()
janela.title("Fazendo a cobra crescer")
janela.geometry("350x350")
janela.resizable(False, False)

# Criando a cobra
cobra = []
x = 5
y = 5
tamanho = 10

dx = 7
dy = 0

x_com = random.randint(0, 313)
y_com = random.randint(0, 313)
tamanho_com = 10

# Canvas
canvas = tk.Canvas(janela, width=325, height=325, bg="black")
canvas.pack(pady=13)

cabeca = canvas.create_rectangle(
    x, y,
    x + tamanho, y + tamanho,
    fill="green",
    outline="black",
    width=1
)

cobra.append(cabeca)

comida = canvas.create_rectangle(
    x_com, y_com,
    x_com + tamanho_com, y_com + tamanho_com,
    fill="red"
)

# Funções
def comer():
    cobra_coords = canvas.coords(cabeca)
    comida_coords = canvas.coords(comida)

    if (
        cobra_coords[0] < comida_coords[2] and
        cobra_coords[2] > comida_coords[0] and
        cobra_coords[1] < comida_coords[3] and
        cobra_coords[3] > comida_coords[1]
    ):
        return True
    return False

def crescer():
    ultimo = cobra[-1]
    x1, y1, x2, y2 = canvas.coords(ultimo)

    novo = canvas.create_rectangle(
        x1, y1,
        x2, y2,
        fill="green",
        outline="black",
        width=1
    )

    cobra.append(novo)

    x_rand = random.randint(0, 313)
    y_rand = random.randint(0, 313)
    canvas.coords(
        comida,
        x_rand, y_rand,
        x_rand + tamanho_com,
        y_rand + tamanho_com
    )

def mover_auto():
    global x, y, dx, dy
    posicoes = [canvas.coords(parte) for parte in cobra]

    x += dx
    y += dy
    canvas.coords(
        cobra[0],
        x, y,
        x + tamanho, y + tamanho
    )

    for i in range(1, len(cobra)):
        canvas.coords(cobra[i], posicoes[i-1])
    
    if comer():
        crescer()

    janela.after(150, mover_auto)

def mudar_dir(event):
    global dx, dy
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