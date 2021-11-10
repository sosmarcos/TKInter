from tkinter import *


def button_onclick():
    print(entrada.get())  # A função get retorna o valor digitado na caixa de entrada
    texto["text"] = entrada.get()


janela = Tk()

janela.geometry("300x300+300+300")

entrada = Entry(janela)
entrada.place(x=100, y=100)

button = Button(janela, width=20, text='ok')
button["command"] = button_onclick
button.place(x=100, y=150)

texto = Label(janela, text='label')
texto.place(x=100, y=200)

janela.mainloop()
