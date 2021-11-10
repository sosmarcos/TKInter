from tkinter import *

window = Tk()
window.geometry('200x100+300+300')

label1 = Label(window, text='ESPAÇO', width='15', height=3, background='blue')
label_horizontal = Label(window, text='HORIZONTAL', background='yellow')
label_vertical = Label(window, text='VERTICAL', background='yellow')

label1.grid(row=0, column=0)
label_horizontal.grid(row=1, column=0, sticky=W)
label_vertical.grid(row=0, column=1, sticky=N)

window.mainloop()
