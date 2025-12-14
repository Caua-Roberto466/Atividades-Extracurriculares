import tkinter as tk

#criando janela
janela = tk.Tk()
janela.title("Fazendo objeto se mover com tecla")
janela.geometry("350x350")
janela.resizable(False, False)
janela.focus_set()

#posição inicial
x = 5
y = 5
tamanho = 10

#função
def mover(event):
    global x
    global y
    if event.keysym == "Down":
        y +=7
        canvas.move(cobra, 0, 7)
    elif event.keysym == "Up":
        y -=7
        canvas.move(cobra, 0, -7)
    elif event.keysym == "Right":
        x +=7
        canvas.move(cobra, 7, 0)
    elif event.keysym == "Left":
        x -=7
        canvas.move(cobra, -7, 0)

#criando canvas para desenhar
canvas = tk.Canvas(janela, width=325, height=325, bg="black")
canvas.pack()

cobra = canvas.create_rectangle(
    x, y,
    x + tamanho, y + tamanho,
    fill="green",
    outline="black",
    width=1
)

janela.bind("<KeyPress>", mover)

janela.mainloop()