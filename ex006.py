from tkinter import *


def button_click():
    print('button_click')
    number1 = int(entrada1.get())
    number2 = int(entrada2.get())
    retorno["text"] = f'{number1} + {number2} = {number1 + number2}'


janela = Tk()
janela.geometry('300x300+200+200')

entrada1 = Entry(janela)
entrada1.place(x=100, y=100)

entrada2 = Entry(janela)
entrada2.place(x=100, y=130)

button = Button(janela, text='soma', width=20)
button["command"] = button_click
button.place(x=100, y=150)

retorno = Label(janela, text='resultado')
retorno.place(x=100, y=200)

janela.mainloop()
