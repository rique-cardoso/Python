nome = input('Nome completo: ')
tem_silva = 'silva' in nome.lower()
if tem_silva:
    print('Tem SILVA no nome!')
else:
    print('Não tem SILVA no nome!')