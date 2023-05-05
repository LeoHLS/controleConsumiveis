import json
import sqlite3
import lists
import time


connection = sqlite3.connect('controleConsumiveis\SQLite_Python.db')

cursor = connection.cursor()


def lista_consumiveis():
    a = cursor.execute('select * from consumiveis') 
    print('ID    NOME         QUANTIDADE\n')
    id = -1
    for i in a:
        id += 1
        print(f'{id}     {i[0]}          {i [1]}')


def adiciona(op, quant):
    lista = list(cursor.execute('select * from consumiveis'))
    quant += lista[op][1]
    alterar = lista[op][0]
    cursor.execute(f'update consumiveis set quantidade = {quant} where nome = "{alterar}"')
    connection.commit()


def updateTable(op, quant):
    lista = list(cursor.execute('select * from consumiveis'))
    quant += lista[op][1]
    alterar = lista[op][0]
    cursor.execute(f'update consumiveis set quantidade = {quant} where nome = "{alterar}"')
    connection.commit()

#return break or continue
'''def userQuit(quest):
    try:
        sair = input(f'{quest}? [S/N]')
        if sair in "nN":
            break
    except:
            print('DIGITE UM VALOR VÁLIDO.\n')
            continue'''
            


def alterar():
    while True:
        print('MENU DE ENTRADA\n')
        lista = list(cursor.execute('select * from consumiveis')) 
        lista_consumiveis()
        while True:
            try:
                opcao = int(input('Selecione o item que deseja adicionar: '))
                if opcao in list(lista.index(i) for i in lista):
                    break
                else:
                    print('Insira um valor válido!\n')
                    continue
            except:
                print('Insira um valor válido!\n')
                continue

        while True:
            try:
                quant = int(input('Quantidade para adicionar: '))
                break
            except:
                print('Insira um valor válido!\n')
                continue
        
        updateTable(opcao, quant)

        

    

def title(title):
    print('-' * (len(title)+2))
    print(title)
    print('-' * (len(title)+2))


def menuAcess():
    title('Menu de Acesso')
    for i in lists.mainMenu:
        print(f'{lists.mainMenu.index(i)} - {i}')
    print()
    while True:
        try:
            opcao = input('Selecione o menu que deseja acessar ou digite "S" para sair')
            print()
            if opcao in 'sS':
                break
            elif opcao in str(list(lists.mainMenu.index(i) for i in lists.mainMenu)):
                break
            else:
                print('Insira um valor válido!\n')
                continue
        except:
            print('Insira um valor válido!\n')
            continue
    if opcao == '0':
        lista_consumiveis()
        time.sleep(1)
        print()
    elif opcao == '1':
        alterar()
        print()
