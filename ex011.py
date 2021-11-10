from tkinter import *

janela = Tk()
janela.geometry('500x200+200+200')

label1 = Label(janela, text='Linha 1', background='blue')
label1.pack(side=TOP, fill=BOTH, expand=1)  # A palavra BOTH serve para preencher as duas direções

label2 = Label(janela, text='Linha 2', background='yellow')
label2.pack(side=TOP, fill=BOTH, expand=1)

label3 = Label(janela, text='Linha 3', background='blue')
label3.pack(side=TOP, fill=BOTH, expand=1)

label4 = Label(janela, text='linha 4', background='yellow')
label4.pack(side=TOP, fill=BOTH, expand=1)

janela.mainloop()
