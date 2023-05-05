import consumiveis
import json
import sqlite3


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


def alterar():
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
    

