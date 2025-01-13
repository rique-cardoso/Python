import io
import sys
def apresentacao():
    print('\033[0;37;42m='*33)  # Texto preto, fundo branco
    print('     SISTEMA DE AJUDA PYHELP     ')
    print(f'='*33)
    print('\033[m')  # Restaura a formatação
def cabecalho(nome_comando, comprimento_comando):
    valor_x = 30 + comprimento_comando + 10
    print('\033[0;37;44m='*valor_x)  # Texto preto, fundo branco
    print(f'     Acessando o manual do comando {nome_comando}     ')
    print(f'='*valor_x)
    print('\033[m')  # Restaura a formatação
def manual(comando):
    # Captura a saída do help em um buffer
    buffer = io.StringIO()
    sys.stdout = buffer
    help(comando)
    sys.stdout = sys.__stdout__  # Restaura o stdout
    # Obtém o conteúdo do buffer
    conteudo = buffer.getvalue()
    buffer.close()
    # Aplica a formatação no conteúdo capturado
    print('\033[1;34m')
    print(conteudo)
    print('\033[m')
def fim():
    print('\033[0;37;41m='*18)
    print('     ATÉ LOGO     ')
    print('='*18)
    print('\033[m')
while True:
    apresentacao()
    cmd = input('Função ou Biblioteca > ')
    if cmd.upper() == 'FIM':
        fim()
        break
    else:
        cabecalho(cmd, len(cmd))
        manual(cmd)