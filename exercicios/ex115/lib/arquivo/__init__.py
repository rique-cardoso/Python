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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos.')
    finally:
        a.close()
def cadastrar(nome_arquivo, nome='desconhecido', idade=0):
    try:
        a = open(f'{caminho_arquivo}\{nome_arquivo}', 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
        finally:
            a.close()