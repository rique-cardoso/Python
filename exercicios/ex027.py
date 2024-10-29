nome = input('Nome completo: ')
primeiro_nome = nome.split()[0]
ultimo_nome = nome.split()[len(nome.split()) - 1]
print('Primeiro nome: {}\nÚltimo nome: {}'.format(primeiro_nome, ultimo_nome))