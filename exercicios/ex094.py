pessoa = dict()
pessoas = list()
mulheres = list()
nomes_mulheres = list()
idade_acima_media = list()
print('=' * 20)
print('CADASTO DE PESSOAS')
print('=' * 20)
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: [M/F]: ').upper()
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    pessoa.clear()
    resposta = input('Deseja continuar? [S/N]: ').upper()
    if resposta == 'N':
        break
print('=' * 20)
soma_idade = 0
for pessoa in pessoas:
    soma_idade += pessoa['idade']
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
media_idade = soma_idade / len(pessoas)
for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        idade_acima_media.append(pessoa['nome'])
print(f'  - Quantidade de pessoas cadastradas: {len(pessoas)}')
print(f'  - Média de idade da população: {media_idade:.0f}')
print(f'  - Mulheres cadastradas: {mulheres}')
print(f'  - Pessoas com idade acima da média: {idade_acima_media}')