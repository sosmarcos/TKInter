from tkinter import *

janela = Tk ()

lb = Label (janela, text='Olá Mundo!')
lb.place(x=100, y=100)

# Width x higth + left + top
janela.geometry("300x300+200+200")
janela.mainloop()
