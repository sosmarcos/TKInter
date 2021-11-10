from tkinter import *
from functools import partial  # com essa função, podemos passar os parâmetros de uma outra função


def button_click(button):
    print(button["text"])


janela = Tk()
janela.geometry("300x300+200+200")

button1 = Button(janela, width=20, text="Botão 1")
button1["command"] = partial(button_click, button1)
button1.place(x=100, y=100)

button2 = Button(janela, width=20, text="Botão 2")
button2["command"] = partial(button_click, button2)
button2.place(x=100, y=130)

janela.mainloop()
