from tkinter import *

window = Tk()
window.title('Teste de fontes')
window.geometry('680x450+100+100')

label1 = Label(window, text='Testando font-family', font='diploma 40')
label1.grid(row=0, sticky=NW)

label2 = Label(window, text='Testando font-size', font='arial 50')
label2.grid(row=1, sticky=NW)

label3 = Label(window, text='Testando font-weigth', font='helvetica 40 bold')
label3.grid(row=2, sticky=NW)

label4 = Label(window, text='Testando font-style', font='comic_sans 40 normal italic')
label4.grid(row=3, sticky=NW)

label5 = Label(window, text='Testando text-decoration', font='Times 40 normal roman underline')
label5.grid(row=4, sticky=NW)

window.mainloop()
