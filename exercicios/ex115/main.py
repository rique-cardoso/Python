from lib import interface
from time import sleep
while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoa', 'Sair do Sistema'])
    if resposta == 1:
        interface.cabecalho('Opção 1')
    elif resposta == 2:
        interface.cabecalho('Opção 2')
    elif resposta == 3:
        interface.cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)