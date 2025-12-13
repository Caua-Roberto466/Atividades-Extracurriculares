import tkinter as tk

janela = tk.Tk()
janela.geometry("350x400")
janela.title("Etapa 10")

#posição inicial
x = 5
y = 5

#tamanho cobra
tamanho_cobra = 10

canvas = tk.Canvas(janela, width=325, height=325, bg="black")
canvas.pack(pady=10)

cobra = canvas.create_rectangle(
    x, y,
    x + tamanho_cobra, y + tamanho_cobra,
    fill="green",
    outline="black",
    width=1
)

def mover():
    global x
    x += 1
    canvas.move(cobra, 5, 0)
    canvas.after(200, mover) #executa a função mover a cada 200 ms 

mover()
janela.mainloop()