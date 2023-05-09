import json
import sqlite3
import lists
import time
from columnar import columnar


connection = sqlite3.connect('controleConsumiveis\SQLite_Python.db')

cursor = connection.cursor()


def title(title):
    print('-' * (len(title)+4))
    print(f'  {title}')
    print('-' * (len(title)+4))



def lista_consumiveis():
    a = cursor.execute('select * from consumiveis ORDER BY quantidade')
    headers = ['ID', 'NOME', 'QUANTIDADE']
    data = []
    id = -1
    for i in a:
        id += 1
        a = []
        a.append(id)
        a.append(i[0])
        a.append(i[1])
        print()
        data.append(a)
    table = columnar(data, headers, no_borders=False, min_column_width=20)
    print(table)



def updateAmount(op, quant):
    lista = list(cursor.execute('select * from consumiveis'))
    quant += lista[op][1]
    alterar = lista[op][0]
    cursor.execute(f'update consumiveis set quantidade = {quant} where nome = "{alterar}"')
    connection.commit()


def delReg(op):
    lista = list(cursor.execute('select * from consumiveis'))
    alterar = lista[op][0]
    cursor.execute(f'DELETE FROM consumiveis WHERE nome = "{alterar}"')
    connection.commit()


def newReg():
    newName = input("Digite o 'nome' do novo consumível: ")
    while True:
        try:
            newAmount = int(input('Digite a quantidade do novo consumível: '))
            break
        except:
            print("Digite uma quantidade válida!")
            continue

    cursor.execute(f'INSERT INTO consumiveis VALUES ("{newName}",{newAmount})')
    connection.commit()


def chooseItem():
    lista = list(cursor.execute('select * from consumiveis'))
    while True:
            try:
                opcao = int(input('Selecione o item que deseja alterar: '))
                if opcao in list(lista.index(i) for i in lista):
                    break
                else:
                    print('Insira um valor válido!\n')
                    continue
            except:
                print('Insira um valor válido!\n')
                continue
    return opcao


#return break or continue
def userQuit(quest):
    while True:
        sair = input(f'\n{quest}?\n[s/n] > ')
        if sair in 'SsnN':
            break
        else:
            print('DIGITE UM VALOR VÁLIDO.\n')
            return True
    if sair in 'Ss':
        return True
    else:
        return False
    
            


def plusLess():
    while True:
        title('MENU DE ENTRADA') 
        lista_consumiveis()
        opcao = chooseItem()
        while True:
            try:
                quant = int(input('\n[+] Adicionar / [-] Subtrair\nDigite a quantidade para alterar: '))
                break
            except:
                print('Insira um valor válido!\n')
                continue
        updateAmount(opcao, quant)
        quit = userQuit('Adicionar algo mais?')
        if quit == False:
            break


    

def regChange():
    while True:
        try:
            opcao = input('[x] para sair\n[C]riar ou [R]emover registro: ')
            print()
            lista_consumiveis()
            if opcao in 'xX':
                break
            elif opcao in 'Rr':
                opcao = chooseItem()
                delReg(opcao)
                print()
            elif opcao in 'Cc':
                newReg()
                
        except:
            print('Insira um valor válido!\n')
            continue
    if opcao in 'xX':
        return False
    
    


def menuAcess():
    title('Menu de Acesso')
    for i in lists.mainMenu:
        print(f'{lists.mainMenu.index(i)} - {i}')
    print()
    while True:
        try:
            opcao = input('[x] para sair\nSelecione o menu que deseja acessar: ')
            print()
            if opcao in 'xX':
                break
            elif opcao in str(list(lists.mainMenu.index(i) for i in lists.mainMenu)):
                break
            else:
                print('Insira um valor válido!\n')
                continue
        except:
            print('Insira um valor válido!\n')
            continue
    if opcao in 'xX':
        return False
    if opcao == '0':
        lista_consumiveis()
        time.sleep(1)
        print()
    elif opcao == '1':
        plusLess()
        print()
    elif opcao == '2':
        regChange()
        print()
