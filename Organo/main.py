from tkinter import *
from functools import partial
from datetime import *
try:
    from functions import *
except ModuleNotFoundError:
    error_window = Tk()
    error_window.geometry('445x110+300+300')
    error_window.minsize(445, 110)
    error_window.maxsize(445, 110)
    error_window.title('Modulo não encontrado')
    error_window.iconbitmap('Organo.ico')
    
    error_label = Label(
        error_window, 
        text='Erro de modulo. A Biblioteca functions não foi encontrada',
        font='Arial 12'
    ).place(x=20, y=35)

    error_window.mainloop()


def enviar_cadastro(nomevar, sobrenomevar, idadevar, estadiavar):
    nome_cadastro = nomevar.get()
    sobrenome_cadastro = sobrenomevar.get()
    idade_cadastro = idadevar.get()
    estadia_cadastro = estadiavar.get()

    label1.grid_remove()
    entrada1.delete(0, len(nome_cadastro))
    entrada1.grid_remove()

    label2.grid_remove()
    entrada2.delete(0, len(sobrenome_cadastro))
    entrada2.grid_remove()

    label3.grid_remove()
    entrada3.delete(0, len(idade_cadastro))
    entrada3.grid_remove()

    label4.grid_remove()
    entrada4.delete(0, len(estadia_cadastro))
    entrada4.grid_remove()

    button4.grid_remove()

    if nome_cadastro == '' or sobrenome_cadastro == '' or idade_cadastro == '' or estadia_cadastro == '':
        fim['foreground'] = 'red'
        fim['text'] = 'Preencha todos os campos'
        fim.grid(row=9, column=0, columnspan=3, sticky=W + E)

    elif nome_cadastro.isnumeric() or sobrenome_cadastro.isnumeric():
        fim['foreground'] = 'red'
        fim['text'] = 'Nome ou sobrenome Invalido'
        fim.grid(row=9, column=0, columnspan=3, sticky=W + E)

    elif idade_cadastro.isalpha():
        fim['foreground'] = 'red'
        fim['text'] = 'Idade Invalido'
        fim.grid(row=9, column=0, columnspan=3, sticky=W + E)

    elif not data_valida(estadia_cadastro):
        fim['foreground'] = 'red'
        fim['text'] = 'Data Invalido'
        fim.grid(row=9, column=0, columnspan=3, sticky=W + E)

    else:
        arquivo_apend('Registros.txt',
                      nome_cadastro.lower(),
                      sobrenome_cadastro.lower(),
                      int(idade_cadastro),
                      estadia_cadastro)

        fim['foreground'] = 'black'
        fim['text'] = f'{nome_cadastro.title()} {sobrenome_cadastro.title()} registrado com sucesso'
        fim.grid(row=9, column=0, columnspan=3, sticky=W + E)


def enviar_login(nomevar, sobrenomevar):
    nome_login = nomevar.get()
    sobrenome_login = sobrenomevar.get()
    hospede = login('Registros.txt', f'{nome_login.lower()} {sobrenome_login.lower()}')

    label1.grid_remove()
    entrada1.delete(0, len(nome_login))
    entrada1.grid_remove()

    label2.grid_remove()
    entrada2.delete(0, len(sobrenome_login))
    entrada2.grid_remove()

    button3.grid_remove()                                        # Validações responsaveis pelas seguntes condições

    if nome_login == '' or sobrenome_login == '':                # Se faltar nome ou sobrenome
        fim['foreground'] = 'red'
        fim['text'] = 'Digite o nome e o sobrenome'
        fim.grid(row=9, column=0, columnspan=3, sticky=W + E)

    elif nome_login.isnumeric() or sobrenome_login.isnumeric():  # Se nome ou sobrenome forem numericos
        fim['foreground'] = 'red'
        fim['text'] = 'Nome ou sobrenome Invalido'
        fim.grid(row=9, column=0, columnspan=3, sticky=W + E)

    elif not hospede:                                            # Se o hospede não for encontrado
        fim['foreground'] = 'red'
        fim['text'] = f'{nome_login.title()} {sobrenome_login.title()} não foi encontrado'
        fim.grid(row=9, column=0, columnspan=3, sticky=W + E)

    else:                                   # Se estiver tudo ok, o programa irá retornar as informações do hospede
        button2.grid_remove()
        button1.grid_remove()

        fim['foreground'] = 'black'
        fim['text'] = 'Pagina do Hóspede\n'
        fim['font'] = 'Times 20'
        fim.grid(row=0, column=0, columnspan=3, sticky=W + E)
        gambiarra.grid(row=4, column=1, columnspan=2, sticky=W + E)

        window.title(f'Informações de {hospede.nome.title()} {hospede.sobrenome.title()}')
        margin_top.destroy()
        h1_margin.destroy()

        data_printer['text'] = f'\nCadastro realizado em {hospede.data}'
        nome_printer['text'] = f'{hospede.nome.title()} {hospede.sobrenome.title()}'
        idade_printer['text'] = f'{hospede.idade} anos'
        if data_count(data_convert(data_atual),data_convert(hospede.estadia)) == 0:
            estadia_printer['text'] = f'{hospede.data} - {hospede.estadia}'
        else :
            estadia_printer['text'] = f'{data_count(data_convert(data_atual),data_convert(hospede.estadia))} dias restantes'

        data_printer.pack()
        label1.grid(row=1, column=0, sticky=W)
        label3.grid(row=2, column=0, sticky=W)
        estadia_label.grid(row=3, column=0, sticky=W)

        nome_printer.grid(row=1, column=1, sticky=W)
        idade_printer.grid(row=2, column=1, sticky=W)
        estadia_printer.grid(row=3, column=1, sticky=W)
        event_label.grid(row=5, column=0, columnspan=3, sticky=W)

        if cheque_arquivo(f'eventos/{hospede.nome}_{hospede.sobrenome}_eve.txt'):
            eventos = return_events(f'eventos/{hospede.nome}_{hospede.sobrenome}_eve.txt')
            for evento in eventos:
                event_printer.insert(END, f'{evento}\n')
        else:
            event_printer.insert(END, 'Nenhum evento registrado\n')

        event_bar.grid(row=6, column=0, columnspan=3, sticky=W + E)
        
        button5['command'] = partial(  # Botão responsavel por iniciar a adição de eventos
            add_event, 
            hospede.nome, 
            hospede.sobrenome,
            label5, 
            entrada5,
            label6,
            entrada6,
            button6,
            button7,
            event_date,
            event_title,
            event_printer,
            retorno1
        )
        button5.grid(row=0, column=0, sticky=W + E)

        button7.grid(row=0, column=1, sticky=W + E)

        button8['command'] = partial(  # Botção responsavel por deletar
            delete_event,
            hospede.nome,
            hospede.sobrenome,
            label7,
            entrada7,
            event_choice,
            button9,
            button7,
            retorno1,
            event_printer
        )
        button8.grid(row=0, column=3, sticky=W + E)
        
        eventFrame.grid(row=7, column=0, columnspan=3, sticky=W + E)
        scroll_events.pack(side=RIGHT, fill=Y)
        event_printer.pack(side=LEFT)


# ===========================================|Variaveis|==================================================================

dia = f'{date.today().day}'; mes = f'{date.today().month}'; ano = f'{date.today().year}'

if len(dia) == 1: dia = f'0{date.today().day}'
if len(mes) == 1: mes = f'0{date.today().month}'

data_atual = f'{dia}/{mes}/{ano}'

if not cheque_arquivo('Registros.txt'):  # Checagem e criação de arquivos para registro
    criar_arquivo('Registros.txt')

cores = {
    'vermelhíssimo': '#d61e0a',
    'vermelho': '#81170C',
    'vermelhão': '#6B231B',
    'azulíssimo': '#087083',
    'azul': '#09444F',
    'azusão': '#142E33',
    'verdíssimo': '#1e8d31',
    'verde': '#09611C',
    'verdão': '#183F21'
}

# =============================================|head|===================================================================
window = Tk()
window.geometry('800x580+300+50')
window.minsize(800, 580)
window.title('Organo')
window.iconbitmap('Organo.ico')
window["background"] = cores['azulíssimo']

# =====================================|Body|===========================================================================
h1_margin = Frame(window, height=50, background=cores['azulíssimo'])
h1_principal = Label(
    h1_margin,
    text='Organo',
    background=cores['azulíssimo'],
    foreground=cores['vermelhíssimo'],
    font='Times 112 normal'
)

margin_top = Frame(window, height=50, background=cores['azulíssimo'])
mainFrame = Frame(  # Conteiner responsavel por representar a interface principar do programa
    window,
    borderwidth=20,
)

nome = StringVar()  # Bloco de entrada da variavel nome para o login e cadastro
label1 = Label(mainFrame, text='Nome:', font='Times 14 bold')
entrada1 = Entry(mainFrame, textvariable=nome, font='Helvetica 12')

sobrenome = StringVar()  # Bloco de entrada da variavel sobrenome para o login e cadastro
label2 = Label(mainFrame, text='Sobrenome:', font='Times 14 bold')
entrada2 = Entry(mainFrame, textvariable=sobrenome, font='Helvetica 12')

idade = StringVar()      # Bloco de entrada da variavel idade para o cadastro
label3 = Label(mainFrame, text='Idade:', font='Times 14 bold')
entrada3 = Entry(mainFrame, textvariable=idade, font='Helvetica 12')

estadia = StringVar()    # Bloco de entreda da variavel estadia para o cadastro
label4 = Label(mainFrame, text='Estadia: [00/00/0000]', font='Times 14 bold')
entrada4 = Entry(mainFrame, textvariable=estadia, font='helvetica 12')

fim = Label(mainFrame, font='Times 14 bold')

# Widgets responsaveis por retornar as informações do hóspede
gambiarra = Label(mainFrame, foreground='SystemButtonFace', text=f'{"_"*100}')
nome_printer = Label(mainFrame, font='Times 14')
idade_printer = Label(mainFrame, font='Times 14')
estadia_label = Label(mainFrame, font='Times 14 bold', text='Estádia:')
event_label = Label(mainFrame, borderwidth=10, text='Diario de eventos', font='Times 14 bold')
estadia_printer = Label(mainFrame, font='Times 14')
data_printer = Label(
    window,
    background=cores['azulíssimo'],
    foreground='white',
    font='Times 16'
)

# Janela de eventos
eventFrame = Frame(mainFrame, background='white', borderwidth=1, relief='solid')
scroll_events = Scrollbar(eventFrame)
event_printer = Text(
    eventFrame, 
    borderwidth=10,
    relief=FLAT, 
    background='white', 
    font='Times 14',
    width=60,
    height=4,
    wrap=NONE,
    yscrollcommand=scroll_events.set
)

event_bar = Frame(mainFrame, background=cores['azusão'])

# ==================================|Adição de Eventos|===================================================================

button5 = Button(  # Botão responsavel por iniciar o registro de novos eventos
    event_bar,
    width=21,
    text='Adicionar',
    borderwidth=0,
    font='Times 12 bold',
    background=cores['azusão'],
    foreground='white',
    activebackground=cores['vermelho'],
    activeforeground='white'
)

button6 = Button(  # Botão responsavel por registrar novos eventos
    mainFrame,
    text='Registrar Evento',
    borderwidth=0,
    font='Times 12 bold',
    background=cores['azusão'],
    foreground='white',
    activebackground=cores['vermelho'],
    activeforeground='white'
)

event_date = StringVar()  # Bloco de entrada da variavel data do evento
label5 = Label(mainFrame, text='Data do evento:', font='Times 14 bold')
entrada5 = Entry(mainFrame, width=11, justify='center', textvariable=event_date, font='Helvetica 12')

event_title = StringVar()  # Bloco de entrada da variavel titulo do evento
label6 = Label(mainFrame, text='Digite aqui um  evento com no maximo 50 caracteres:', font='Times 14 bold')
entrada6 = Entry(mainFrame, width=49, textvariable=event_title, font='Helvetica 12')

retorno1 = Label(mainFrame, foreground='red' ,font='Times 14 bold')

# ==================================|Botão de cancelamento|===============================================================

button7 = Button(
    event_bar,
    width=21,
    text='',
    borderwidth=0,
    font='Times 12 bold',
    background=cores['azusão'],
    foreground='white',
    activebackground=cores['vermelho'],
    activeforeground='white'
)

# ====================================|Deletar eventos|===================================================================

button8 = Button(
    event_bar,
    width=21,
    text='Excluir',
    borderwidth=0,
    font='Times 12 bold',
    background=cores['azusão'],
    foreground='white',
    activebackground=cores['vermelho'],
    activeforeground='white'
)

button9 = Button(  # Botão responsavel por deletar eventos
    mainFrame,
    text='Deletar',
    width=14,
    borderwidth=0,
    font='Times 12 bold',
    background=cores['azusão'],
    foreground='white',
    activebackground=cores['vermelho'],
    activeforeground='white'
)

event_choice = StringVar()  # Bloco de entrada da variavel titulo do evento
label7 = Label(mainFrame, text='Digite aqui o evento a ser deletado:', font='Times 14 bold')
entrada7 = Entry(mainFrame, width=49, textvariable=event_choice, font='Helvetica 12')

aberto1 = False
aberto2 = False
button3 = Button(
    mainFrame,
    text='Enviar',
    borderwidth=0,
    font='Times 12 bold',
    background=cores['azusão'],
    foreground='white',
    activebackground=cores['vermelho'],
    activeforeground='white',
    command=partial(enviar_login, nome, sobrenome)
)

button4 = Button(
    mainFrame,
    text='Enviar',
    borderwidth=0,
    font='Times 12 bold',
    background=cores['azusão'],
    foreground='white',
    activebackground=cores['vermelho'],
    activeforeground='white',
    command=partial(enviar_cadastro, nome, sobrenome, idade, estadia)
)

button1 = Button(  # Botão responsavel por direcionar o usuario para o login
    mainFrame,
    text='Login',
    width=20,
    borderwidth=0,
    font='Times 12 bold',
    background=cores['azusão'],
    foreground='white',
    activebackground=cores['vermelho'],
    activeforeground='white',
    command=partial(login_display, [aberto1, button3, label1, entrada1, label2, entrada2, fim])
)

margem_entre_botoes = Frame(mainFrame, width=10).grid(row=0, column=1)

button2 = Button(  # Botão responsavel por direcionar o usuario para o cadastro
    mainFrame,
    text='Cadastro',
    width=20,
    borderwidth=0,
    font='Times 12 bold',
    background=cores['azusão'],
    foreground='white',
    activebackground=cores['vermelho'],
    activeforeground='white',
    command=partial(cadastro_display,
                    [aberto2,
                     button4,
                     label1,
                     entrada1,
                     label2,
                     entrada2,
                     label3,
                     entrada3,
                     label4,
                     entrada4,
                     fim])
)

inicio(button1, button2)

margem_antes_do_botao_enviar = Frame(mainFrame, height=10).grid(row=8, column=0)

h1_margin.pack()
h1_principal.pack()
margin_top.pack()
mainFrame.pack()

window.mainloop()
