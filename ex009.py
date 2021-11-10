from tkinter import *

janela = Tk()
janela.geometry('400x300+200+200')

label1 = Label(janela, text='Side 1', background='white')
label2 = Label(janela, text='Side 2', background='red')
label3 = Label(janela, text='Anchor 1', background='white')
label4 = Label(janela, text='Anchor 2', background='red')

label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(anchor=NW)
label4.pack(anchor=SW)

janela["background"] = 'black'
janela.mainloop()
