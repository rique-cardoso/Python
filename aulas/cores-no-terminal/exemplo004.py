nome1 = 'Marilena Chauí'
nome2 = 'Rodrigo Ramos'
nome3 = 'Tales de Mileto'
nome4 = 'Anaximandro de Mileto'
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'azul': '\033[34m', 
         'amarelo': '\033[33m', 
         'verde': '\033[32m'}
print('Olá, {}{}{}. Prazer em te conhecer!'.format(cores['vermelho'], nome1, cores['limpa']))
print('Olá, {}{}{}. Prazer em te conhecer!'.format(cores['azul'], nome2, cores['limpa']))
print('Olá, {}{}{}. Prazer em te conhecer!'.format(cores['amarelo'], nome3, cores['limpa']))
print('Olá, {}{}{}. Prazer em te conhecer!'.format(cores['verde'], nome4, cores['limpa']))