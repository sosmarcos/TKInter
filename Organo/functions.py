from tkinter import *
from datetime import *
from functools import partial


def inicio(button1, button2):
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=2)


def login_display(lista):
    lista[6].grid_remove()

    if not lista[0]:
        lista[2].grid(row=1, column=0, sticky=W)
        lista[3].grid(row=2, column=0, columnspan=3, sticky=W + E)
        lista[4].grid(row=3, column=0, sticky=W)
        lista[5].grid(row=4, column=0, columnspan=3, sticky=W + E)
        lista[1].grid(row=9, column=0, columnspan=3, sticky=W + E)

        lista[0] = True
    else:
        lista[2].grid_remove()
        lista[3].grid_remove()
        lista[4].grid_remove()
        lista[5].grid_remove()
        lista[1].grid_remove()
        lista[0] = False


def cadastro_display(lista):
    lista[10].grid_remove()

    if not lista[0]:
        lista[2].grid(row=1, column=0, sticky=W)
        lista[3].grid(row=2, column=0, columnspan=3, sticky=W + E)
        lista[4].grid(row=3, column=0, sticky=W)
        lista[5].grid(row=4, column=0, columnspan=3, sticky=W + E)
        lista[6].grid(row=5, column=0, sticky=W)
        lista[7].grid(row=6, column=0, sticky=W + E)
        lista[8].grid(row=5, column=2, sticky=W)
        lista[9].grid(row=6, column=2, sticky=W + E)
        lista[1].grid(row=9, column=0, columnspan=3, sticky=W + E)

        lista[0] = True
    else:
        lista[2].grid_remove()
        lista[3].grid_remove()
        lista[4].grid_remove()
        lista[5].grid_remove()
        lista[6].grid_remove()
        lista[7].grid_remove()
        lista[8].grid_remove()
        lista[9].grid_remove()
        lista[1].grid_remove()
        lista[0] = False


def add_event(nome, sobrenome, label1, entry1, label2, entry2, label3, entry3, button, var1, var2, var3, printer):
    dia = f'{date.today().day}'; mes = f'{date.today().month}'; ano = f'{date.today().year}'

    if len(dia) == 1: dia = f'0{date.today().day}'
    if len(mes) == 1: mes = f'0{date.today().month}'

    data = f'{dia}/{mes}/{ano}'
    print(printer.get('1.0', '1.24'))
    if not cheque_arquivo(f'eventos/{nome}_{sobrenome}_eve.txt'):
        criar_arquivo(f'eventos/{nome}_{sobrenome}_eve.txt')

    label1.grid(row=8, column=0, columnspan=2, sticky=W)
    entry1.grid(row=9, column=0, columnspan=3, sticky=W + E)

    label2.grid(row=10, column=0, columnspan=2, sticky=W)
    entry2.delete(0, len(entry2['textvariable']) + 3)
    entry2.insert(0, data)
    entry2.grid(row=10, column=0, columnspan=2)

    label3.grid(row=10, column=1, sticky=E)
    entry3.grid(row=10, column=1, columnspan=2, sticky=E)

    button['command'] = partial(
        evento_apend, f'eventos/{nome}_{sobrenome}_eve.txt', 
        var2, var3, var1, printer, {
            'entry1': entry1, 
            'entry2': entry2, 
            'entry3': entry3, 
            'label1': label1, 
            'label2': label2, 
            'label3': label3,
            'button': button
        }
    )
    button.grid(row=11, column=0, columnspan=3, sticky=W + E)


def data_valida(arg_data):
    data = arg_data
    if data.isnumeric() or len(data) != 10:
        print('DATA INVALIDA')
        return False
    else:
        teste = data.split('/')
        dia = int(teste[0])
        mes = int(teste[1])
        ano = int(teste[2])
        try:
            if teste[0].isnumeric() \
            and teste[1].isnumeric() \
            and teste[2].isnumeric() \
            and len(teste[0]) == 2 \
            and len(teste[1]) == 2 \
            and len(teste[2]) == 4:
                if mes > 12:
                    return False
                else:
                    meses = [
                        ['janeiro', 31],
                        ['fevereiro', 28],
                        ['março', 31],
                        ['abril', 30],
                        ['maio', 31],
                        ['junho', 30],
                        ['julho', 31],
                        ['agosto', 31],
                        ['setembro', 30],
                        ['outubro', 31],
                        ['novembro', 30],
                        ['dezembro', 31]
                    ]
                    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                        meses[1][1] = 29
                    if dia > meses[mes - 1][1]:
                        return False
                    elif ano != date.today().year:
                        return False
                    else:
                        return True
            else:
                print('DATA INVALIDA')
                return False
        except IndexError:
            print('DATA INVALIDA')


def data_convert(data_str):
    data = data_str.split('/')
    data_int = list()
    for index in enumerate(data):
        num = list()
        for c in range(0, len(index[1])):
            if index[1][c] == '0':
                num.append(0)
            elif index[1][c] == '1':
                num.append(1)
            elif index[1][c] == '2':
                num.append(2)
            elif index[1][c] == '3':
                num.append(3)
            elif index[1][c] == '4':
                num.append(4)
            elif index[1][c] == '5':
                num.append(5)
            elif index[1][c] == '6':
                num.append(6)
            elif index[1][c] == '7':
                num.append(7)
            elif index[1][c] == '8':
                num.append(8)
            elif index[1][c] == '9':
                num.append(9)
        for c in range(0, len(num)):
            if len(num) == 2:
                if c == 0:
                    num[0] = num[0] * 10
            else:
                if c == 0:
                    num[0] = num[0] * 1000
                elif c == 1:
                    num[1] = num[1] * 100
                elif c == 2:
                    num[2] = num[2] * 10
        if len(num) == 2:
            num = num[0] + num[1]
        else:
            num = num[0] + num[1] + num[2] + num[3]
        data_int.append(num)
    return data_int


def data_count(data_inicial, data_final):
    anos_total = data_final[2] - data_inicial[2] + 1
    mes_inicial = data_inicial[1]
    mes_final = data_final[1]
    dia_inicial = data_inicial[0]
    dia_final = data_final[0]
    dias = 0
    for anos in range(0, anos_total):
        ano_teste = data_inicial[2] + anos
        if ano_teste % 4 == 0 and ano_teste % 100 != 0 or ano_teste % 400 == 0:
            bissexto = True
        else:
            bissexto = False
        ano = [['janeiro', 31],
               ['fevereiro', 28],
               ['março', 31],
               ['abril', 30],
               ['maio', 31],
               ['junho', 30],
               ['julho', 31],
               ['agosto', 31],
               ['setembro', 30],
               ['outubro', 31],
               ['novembro', 30],
               ['dezembro', 31]]
        if bissexto:
            ano[1][1] = 29
        for mes in enumerate(ano):
            for dia in range(0, mes[1][1]):
                if anos_total == 1:
                    if mes_inicial == mes_final == mes[0] + 1:
                        if dia_inicial <= dia + 1 <= dia_final:
                            dias += 1
                    elif mes_final >= mes[0] + 1 >= mes_inicial:
                        if mes_inicial == mes[0] + 1 and dia_inicial <= dia + 1:
                            dias += 1
                        elif mes_final == mes[0] + 1 and dia_final >= dia + 1:
                            dias += 1
                        elif mes_final > mes[0] + 1 > mes_inicial:
                            dias += 1
                else:
                    if anos == 0:
                        if mes_inicial == mes[0] + 1:
                            if dia_inicial <= dia + 1:
                                dias += 1
                        elif mes_inicial < mes[0] + 1:
                            dias += 1
                    elif anos == anos_total - 1:
                        if mes_final == mes[0] + 1:
                            if dia_final >= dia + 1:
                                dias += 1
                        elif mes_final > mes[0] + 1:
                            dias += 1
                    elif 0 < anos < anos_total - 1:
                        dias += 1
    return dias


def cheque_arquivo(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('\033[1;31mERRO NA CRIAÇÃO DO ARQUIVO\033[m')
    else:
        print('Arquivo Criado Com Sucesso')


def evento_apend(arquivo, data, titulo, evento, printer, widgets):
    try:
        arquivo = open(arquivo, 'at')
    except:
        print('ERRO NA ABERTURA DO ARQUIVO')
    else:
        try:
            if data_valida(data.get()):
                arquivo.write(f'{data.get()};{titulo.get()};{evento.get()}\n')
            else:
                print('Data Invalida')
        except:
            print('ERRO NA ESCRITA')
        else:
            if printer.get('1.0', '1.24') == 'Nenhum evento registrado':
                printer.delete('1.0', END)
            printer.insert(END, f'{data.get()} - {titulo.get()}\n')

            widgets['entry1'].delete(0, len(evento.get()))
            widgets['entry2'].delete(0, len(data.get()))
            widgets['entry3'].delete(0, len(titulo.get()))

            for widget in widgets.values():
                widget.grid_remove()
    finally:
        arquivo.close()


def arquivo_apend(arquivo, nome='Desconhecido', sobrenome='Desconhecido', idade=0, estadia=''):
    dia = f'{date.today().day}'
    if len(dia) == 1:
        dia = f'0{date.today().day}'
    mes = f'{date.today().month}'
    if len(mes) == 1:
        mes = f'0{date.today().month}'
    ano = f'{date.today().year}'
    data = f'{dia}/{mes}/{ano}'
    try:
        arquivo = open(arquivo, 'at')
    except:
        print('\033[1;31mERRO NA ABERTURA DO ARQUIVO\033[m')
    else:
        try:
            arquivo.write(f'{nome};{sobrenome};{idade};{estadia};{data}\n')
        except:
            print('\033[1;31mERRO NA ESCRITA\033[m')
        else:
            print(f'{nome.capitalize()} {sobrenome.capitalize()} registrado com sucesso')
    finally:
        arquivo.close()


class Hospede:
    def __init__(self, nome='', sobrenome='', idade=0, estadia=0, data=0):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.estadia = estadia
        self.data = data


def login(arquivo, nome):
    try:
        arquivo = open(arquivo, 'rt')
    except:
        print('\033[1;31mERRO NA ABERTURA DO ARQUIVO\033[m')
    else:
        try:
            fnome = nome.split()[0]
            snome = nome.split()[1]
        except IndexError:
            print('Digite o nome e o sobrenome')
            return False
        else:
            dado = ''
            for linha in arquivo:
                dado = linha.split(';')
                dado[4] = dado[4].replace('\n', '')
                if fnome == dado[0] and snome == dado[1]:
                    pessoa = Hospede(dado[0], dado[1], int(dado[2]), dado[3], dado[4])
                    return pessoa
            if not fnome == dado[0] or not snome == dado[1]:
                print(f'{nome.title()} não foi encontrado')
                return False
    finally:
        arquivo.close()


def return_events(arquivo):
    try:
        arquivo = open(arquivo, 'rt')
    except:
        print('ERRO NA ABERTURA DE EVENTOS')
    else:
        eventos = []

        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            eventos.append(f'{dado[0]} - {dado[1].capitalize()}')

        return eventos
    finally:
        arquivo.close()
