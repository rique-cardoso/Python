from datetime import datetime
pessoa = {}
pessoa['nome'] = input('Nome: ')
ano_nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - ano_nascimento
ctps = int(input('CTPS (0 - Não tem): '))
if ctps != 0:
    pessoa['ctps'] = ctps
    ano_contratacao = int(input('Ano de contratação: '))
    pessoa['idade de aposentadoria'] = pessoa['idade'] + (ano_contratacao + 35) - datetime.now().year
    pessoa['salario'] = float(input('Salário: R$'))
else:
    pessoa['ctps'] = None
print('=' * 30)
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')