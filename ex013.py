from tkinter import *

window = Tk()
window.geometry('200x100+100+100')

label1 = Label(window, text='Login')
label1.grid(row=1, column=1)

login = Entry(window)
login.grid(row=1, column=2)

label2 = Label(window, text='Senha')
label2.grid(row=2, column=1)

senha = Entry(window)
senha.grid(row=2, column=2)

button = Button(window, text='Confirmar')
button.grid(row=3, column=2)

window.mainloop()
