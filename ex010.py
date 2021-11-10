from tkinter import *

janela = Tk()
janela.geometry('400x300+200+200')

label1 = Label(janela, text='Horizontal',  background='white')
label1.pack(side=TOP, fill=X)

label2 = Label(janela, text='', background='black')
label2.pack(side=LEFT, fill=Y)

label3 = Label(janela, text='', background='black')
label3.pack(side=RIGHT, fill=Y)

janela.mainloop()
