soma_idade = 0
maior_idade = 0
nome_h_velho = ''
qtd_m_menor20 = 0
for c in range(0, 4):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ')
    soma_idade += idade
    if sexo.upper() == "M":
        if idade > maior_idade:
            maior_idade = idade
            nome_h_velho = nome
    else:
        if idade < 20:
            qtd_m_menor20 += 1
media_idade = soma_idade / 4
print('''
Média de idade: {}
Nome do homem mais velho: {}
Quantidade de mulheres com menos de 20 anos: {}
'''.format(media_idade, nome_h_velho, qtd_m_menor20))