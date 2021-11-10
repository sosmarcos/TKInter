from tkinter import *


def botão_click ():
    global contador
    print(f"{contador}º Click")
    texto["text"] = f"{contador}º Click"
    contador += 1
    

contador = 1

janela = Tk ()
janela.geometry("300x300+200+200")

# Vejá que o objeto botão recebe uma classe Button, e recebe os parametros Width, text e command, que é uma função
botão = Button (janela, width=20, text="ok", command=botão_click)
botão.place(x=90, y=100)

texto = Label (janela, text="Teste")
texto.place(x=110, y=150)


janela.mainloop()
