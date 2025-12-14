import tkinter as tk

janela = tk.Tk()
janela.title("Movimento automático")
janela.geometry("350x350")
janela.resizable(False, False)

canvas = tk.Canvas(janela, width=325, height=325, bg="black")
canvas.pack(pady=13)

x = 5
y = 5
tamanho_cobra = 10

dx = 7
dy = 0

cobra = canvas.create_rectangle(
    x, y,
    x + tamanho_cobra, y + tamanho_cobra,
    fill="green",
    outline="black",
    width=1
)

def mover_automatico():
    global dx, dy
    global x, y

    x += dx
    y += dy

    canvas.move(cobra, dx, dy)

    janela.after(150, mover_automatico)

def mudar_direcao(event):
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

mover_automatico()

janela.bind("<KeyPress>", mudar_direcao)

janela.mainloop()