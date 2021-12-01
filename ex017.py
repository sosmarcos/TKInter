from tkinter import *


def teste():
    print(check_variavel.get())
    label["text"] = nome.get()
    entrada.delete(0, len(nome.get()))
    if check_variavel.get():
        check['text'] = 'Ativado'
    else:
        check['text'] = 'Desativado'


window = Tk()
window.geometry('640x480+100+100')

button = Button(window)
button["cursor"] = 'cross'
button["text"] = 'Teste de botão'       # texto
button["foreground"] = 'white'          # Cor das letras
button["background"] = '#10009f'        # Cor de fundo
button["borderwidth"] = 0               # Largura da borda
button["activeforeground"] = 'blue'     # Cor das letras durante a ativação
button["activebackground"] = 'white'    # Cor de fundo durante a ativação
button["width"] = 10                    # Largura
button["height"] = 0                    # Altura
button["font"] = 'Times 40'             # Fonte
button["command"] = teste
button.pack(fill=X)

check_variavel = BooleanVar()          # Esta variavel irá conter o valor booleano do botão
check_variavel.set(False)              # Esta função determina o valor inicial do botão

check = Checkbutton(window, variable=check_variavel)
check["text"] = 'Teste de Botão'
check.pack()

radio_value = IntVar()                 # Esta variavel irá conter o valor numérico do botão
radio_value.set(1)                     # Esta função determina o valor inicial do botão

radio1 = Radiobutton(window, text='Opção 1', variable=radio_value, value=1, indicatoron=0).pack()
radio2 = Radiobutton(window, text='Opção 2', variable=radio_value, value=2, indicatoron=0).pack()
radio3 = Radiobutton(window, text='Opção 3', variable=radio_value, value=3, indicatoron=0).pack()

label = Label(window, text=radio_value.get())
label.pack()

nome = StringVar()

entrada = Entry(window)
entrada["foreground"] = 'red'
entrada["background"] = 'blue'
entrada["font"] = 'Times 12 bold'
entrada["borderwidth"] = 0
entrada["justify"] = 'center'
entrada["textvariable"] = nome
entrada.pack()

window.mainloop()
