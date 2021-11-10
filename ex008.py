from tkinter import *

janela = Tk()
janela.geometry('400x300+200+200')

label1 = Label(janela, text='Rigth', background='white')
label2 = Label(janela, text='Bottom', background='white')
label3 = Label(janela, text='Left', background='white')
label4 = Label(janela, text='Top', background='white')

label1.pack(side=RIGHT)
label2.pack(side=BOTTOM)
label3.pack(side=LEFT)
label4.pack(side=TOP)

janela["background"] = 'black'
janela.mainloop()
