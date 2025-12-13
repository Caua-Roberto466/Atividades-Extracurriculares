import tkinter as tk

janela = tk.Tk()
janela.title("Criando Canvas")
janela.geometry("350x410")

canvas = tk.Canvas(janela, width=325, height=325, bg="black")
canvas.pack(pady=5)

canvas.create_rectangle(40, 40, 100, 100, fill="green")

janela.mainloop()