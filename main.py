from functions import *
import lists




title('Sistema de Controle de Consumíveis')

while True:
    menu = menuAcess()
    if menu == False:
        break
    quit = userQuit('Deseja acessar mais alguma função?')
    if (quit == False):
        break
    print()
