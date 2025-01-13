from lib import interface
from lib import arquivo
from time import sleep
nome_arquivo = 'cursoemvideo.txt'
if not arquivo.existe(nome_arquivo):
    arquivo.criar(nome_arquivo)
while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar um arquivo.
        arquivo.ler(nome_arquivo)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        interface.cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = interface.leiaInt('Idade: ')
        arquivo.cadastrar(nome_arquivo, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        interface.cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)