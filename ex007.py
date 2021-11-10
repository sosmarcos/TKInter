from tkinter import *

janela = Tk()

label1 = Label(janela, text='Label 1', background='green')
label2 = Label(janela, text='Label 2', background='red')
label3 = Label(janela, text='Label 3', background='yellow')
label4 = Label(janela, text='Label 4', background='blue')

label1.pack()
label2.pack()
label3.pack()
label4.pack(side=BOTTOM)

janela.geometry('400x300+200+200')
janela.mainloop()
