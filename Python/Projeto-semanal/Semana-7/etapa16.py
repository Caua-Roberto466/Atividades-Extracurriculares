import tkinter as tk

janela = tk.Tk()
janela.title("Game Over")
janela.geometry("350x350")
janela.resizable(False, False)

x = 5
y = 5
tamanho_cobra = 10

dx = 7
dy = 0

canvas = tk.Canvas(janela, width=325, height=325, bg="black")
canvas.pack(pady=13)

cobra = canvas.create_rectangle(
    x, y,
    x + tamanho_cobra, y + tamanho_cobra,
    fill="green",
    outline="black",
    width=1
)

def game_over():
    canvas.delete("all")
    canvas.create_text(
        162, 162,
        text="Game Over",
        fil="red",
        font=("Arial", 36, "bold")
    )

def verificar_colisao():
    global x, y, tamanho_cobra
    if x < 0 or y < 0 or x + tamanho_cobra > 325 or y + tamanho_cobra > 325:
        game_over()

def mover():
    global dx, dy
    global x, y
    x += dx
    y += dy
    canvas.move(cobra, dx, dy)
    janela.after(150, mover)
    verificar_colisao()

mover()

janela.mainloop()