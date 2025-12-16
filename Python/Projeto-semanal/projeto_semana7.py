#Jogo da cobrinha
import tkinter as tk # vai importar tk da biblioteca tkinter
import random
janela = tk.Tk() #vai criar a váriavel da janela
janela.title("Jogo da cobrinha") #da o nome da janela
janela.geometry("350x350") #tamanho da janela
janela.resizable(False, False)
janela.focus_set()
jogo_ativo = True

cobra=[]
x=5
y=5
tamanho=10

dx = 11
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

crescer_proximo = False

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
    global crescer_proximo
    crescer_proximo = True
    x_rand = random.randint(0, 313)
    y_rand = random.randint(0, 313)
    canvas.coords(
        comida,
        x_rand, y_rand,
        x_rand + tamanho_c, y_rand + tamanho_c
    )

def colisao_corpo():
    global jogo_ativo
    cabeca_coords = canvas.coords(cobra[0])

    for parte in cobra[1:]:
        parte_coords = canvas.coords(parte)

        if (
            cabeca_coords[0] < parte_coords[2] and
            cabeca_coords[2] > parte_coords[0] and
            cabeca_coords[1] < parte_coords[3] and
            cabeca_coords[3] > parte_coords[1]
        ):
            jogo_ativo = False
            return True
    return False

def morrer_borda():
    global jogo_ativo
    if x < 0 or y < 0 or x + tamanho > 325 or y + tamanho > 325:
        jogo_ativo = False
        canvas.delete("all")
        canvas.create_text(162, 162, text="Fim de Jogo", fill="red", font=("Arial", 25, "bold"))

def mover_auto():
    global crescer_proximo
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
    
    if crescer_proximo:
        x1, y1, x2, y2 = posicoes[-1]

        novo = canvas.create_rectangle(
            x1, y1,
            x2, y2,
            fill="green",
            outline="black",
            width=1
        )

        cobra.append(novo)
        crescer_proximo = False

    
    if comer():
        crescer()

    if  colisao_corpo():
        canvas.delete("all")
        canvas.create_text(162, 162, text="Fim de Jogo", fill="red", font=("Arial", 25, "bold"))
        return

    morrer_borda()
    janela.after(150, mover_auto)

def reiniciar_jogo():
    global cobra, x, y, dx, dy, jogo_ativo, crescer_proximo, comida, cabeca

    canvas.delete("all")

    cobra = []
    x = 5
    y = 5
    dx = 11
    dy = 0
    crescer_proximo = False
    jogo_ativo = True

    # recriar cabeça
    cabeca = canvas.create_rectangle(
        x, y,
        x + tamanho, y + tamanho,
        fill="green",
        outline="black",
        width=1
    )
    cobra.append(cabeca)

    # recriar comida (IMPORTANTE)
    x_rand = random.randint(0, 313)
    y_rand = random.randint(0, 313)
    comida = canvas.create_rectangle(
        x_rand, y_rand,
        x_rand + tamanho_c, y_rand + tamanho_c,
        fill="red"
    )

    mover_auto()



def mudar_dir(event):
    global dx, dy

    if event.keysym == "space" and not jogo_ativo:
        reiniciar_jogo()
        return

    if event.keysym == "Up" and dy == 0:
        dx = 0
        dy = -11
    elif event.keysym == "Down" and dy == 0:
        dx = 0
        dy = 11
    elif event.keysym == "Right" and dx == 0:
        dx = 11
        dy = 0
    elif event.keysym == "Left" and dx == 0:
        dx = -11
        dy = 0

mover_auto()
janela.bind("<KeyPress>", mudar_dir)

janela.mainloop() #inicia o loop que deixa a janela