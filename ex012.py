from tkinter import *

window = Tk()
window.geometry('400x300+200+200')

label1 = Label(window, text='Label 1')
label1.grid(row=1, column=1)

label2 = Label(window, text='Label 2')
label2.grid(row=2, column=2)

window.mainloop()
