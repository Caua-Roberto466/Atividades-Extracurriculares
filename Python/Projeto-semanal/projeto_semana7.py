#Jogo da cobrinha
import tkinter as tk # vai importar tk da biblioteca tkinter
import random
janela = tk.Tk() #vai criar a váriavel da janela
janela.title("Jogo da cobrinha") #da o nome da janela
janela.geometry("350x350") #tamanho da janela
janela.resizable(False, False)
jogo_ativo = True

cobra=[]
x=5
y=5
tamanho=10

dx = 7
dy = 0

x_c = random.randint(0, 313)
y_c = random.randint(0, 313)
tamanho_c = 8

#canvas
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
    x_c, y_c,
    x_c+tamanho_c, y_c+tamanho_c,
    fill="red"
)

#funções
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
        x_rand + tamanho_c, y_rand + tamanho_c
    )

def morrer_borda():
    global jogo_ativo
    if x < 0 or y < 0 or x + tamanho > 325 or y + tamanho > 325:
        jogo_ativo = False
        canvas.delete("all")
        canvas.create_text(162, 162, text="Fim de Jogo", fill="red", font=("Arial", 25, "bold"))

def mover_auto():
    global x, y
    if not jogo_ativo:
        return
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

    morrer_borda()
    janela.after(150, mover_auto)
    
def mudar_dir(event):
    global dx, dy
    if event.keysym == "Up":
        dx = 0
        dy = -7
    elif event.keysym == "Down":
        dx = 0
        dy = 7
    elif event.keysym == "Right":
        dx = 7
        dy = 0
    elif event.keysym == "Left":
        dx = -7
        dy = 0

mover_auto()
janela.bind("<KeyPress>", mudar_dir)

janela.mainloop() #inicia o loop que deixa a janela