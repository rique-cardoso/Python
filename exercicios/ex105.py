def notas(lista_notas, situacao=False):
    """
        -> Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma
    """
    qtd_notas = len(lista_notas)
    maior_nota = max(lista_notas)
    menor_nota = min(lista_notas)
    media_turma = sum(lista_notas) / len(lista_notas)
    dic_notas = {
        'qtd_notas': qtd_notas,
        'maior_nota': maior_nota,
        'menor_nota': menor_nota,
        'media_turma': media_turma
    }
    if situacao:
        if dic_notas['media_turma'] >= 7:
            dic_notas['situacao'] = 'BOA'
        elif dic_notas['media_turma'] >= 5:
            dic_notas['situacao'] = 'RAZOÁVEL'
        else:
            dic_notas['situacao'] = 'RUIM'
            
    return dic_notas
# Programa principal
notas_alunos = list()
sit = False
while True:
    notas_alunos.append(float(input('Digite a nota do aluno: ')))
    res = input('Deseja continuar? [S/N]: ').upper()
    if res == 'N':
        sit = True if input('Deseja mostrar a situação? [S/N]: ').upper() == 'S' else False
        break
if sit:
    print(notas(notas_alunos, sit))
else:
    print(notas(lista_notas=notas_alunos))
help(notas)