from lib import interface
caminho_arquivo = r'C:\Users\henri\Documents\estudos-tech\Python\exercicios\ex115'
def existe(nome):
    try:
        a = open(f'{caminho_arquivo}\{nome}', 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criar(nome):
    try:
        a = open(f'{caminho_arquivo}\{nome}', 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso')
def ler(nome):
    try:
        a = open(f'{caminho_arquivo}\{nome}', 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        interface.cabecalho('PESSOAS CADASTRADAS')
        print(a.read())