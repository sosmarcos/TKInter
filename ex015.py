from tkinter import *
from PIL import ImageTk  # Este modulo trabalha com imagens

window = Tk()
window.geometry('600x500+100+100')

# Aqui a imagem é declarada
imagem = ImageTk.PhotoImage(file='f274780032.png')

# Aqui a imagem é inserida em um label ou etiqueta
label = Label(window, image=imagem)

# Aqui o label é posicionado em window
label.pack(anchor=NW)

window.mainloop()
